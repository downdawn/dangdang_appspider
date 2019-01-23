# coding=utf-8

from pymongo import MongoClient
# from dangdang.config import *
import json

MONGO_URL = 'localhost'
MONGO_DB = 'dangdang'
MONGO_COLLECTION = 'content'

def response(flow):
    # 初始化MongoDB数据库
    client = MongoClient(MONGO_URL)
    db = client[MONGO_DB]
    dangdang_book_collection = db[MONGO_COLLECTION]

    request = flow.request
    response = flow.response
    url = 'http://search.mapi.dangdang.com/'
    # 过滤请求的URL
    if url in request.url:
        data = json.loads(response.text.encode('utf-8'))
        # 书籍
        products = data.get('products') or None
        product_datas = []
        for product in products:
            product_id = product.get('id')  # ID
            product_name = product.get('name')  # 名称
            product_price = product.get('price')  # 价格
            authorname = product.get('authorname')  # 作者
            publisher = product.get('publisher')  # 出版社
            product_datas.append({
                'product_id': product_id,
                'product_name': product_name,
                'product_price': product_price,
                'authorname': authorname,
                'publisher': publisher
            })
        # dangdang_book_collection.insert(product_datas)  # 直接插入数据
        for i in product_datas:
            print(i)
            dangdang_book_collection.update({'product_id': i["product_id"]}, i, True)  # 用ID来过滤更新
            print('成功插入数据')
