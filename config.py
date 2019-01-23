# coding=utf-8

# 设备名称 通过 adb devices -l 获取
DEVICE_NAME = 'vivo_X7'
PLATFORM = 'Android'

# Appium地址
DRIVER_SERVER = 'http://localhost:4723/wd/hub'

# 等待元素加载时间
TIMEOUT = 100

# MongoDB配置
MONGO_URL = 'localhost'
MONGO_DB = 'dangdang'
MONGO_COLLECTION = 'content'

# 滑动点
# 起始点的x轴坐标、y轴坐标
FLICK_START_X = 300
FLICK_START_Y = 278

# 每次滑动的距离
FLICK_DISTANCE = 700

# 每次滑动的时间间隔
SCROLL_SLEEP_TIME = 1

# 搜索关键字
KEY_WORD = 'Python'