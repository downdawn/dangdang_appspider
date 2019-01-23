# coding=utf-8

from appium import webdriver
# from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from dangdang.config import *
from time import sleep


class Action(object):
    def __init__(self):
        """
        初始化
        """
        # 驱动配置
        self.desired_caps = {
            'platformName': PLATFORM,  # 平台名称
            'deviceName': DEVICE_NAME,  # 设备名称
            'appPackage': 'com.dangdang.buy2',  # APP包
            'appActivity': 'com.dangdang.buy2.StartupActivity'  # App入口
        }
        self.driver = webdriver.Remote(DRIVER_SERVER, self.desired_caps)
        self.wait = WebDriverWait(self.driver, TIMEOUT)

    def content(self):
        # 点击进入搜索页面
        sure = self.wait.until(EC.presence_of_element_located((By.ID, 'com.dangdang.buy2:id/index_search')))
        sure.click()
        # 输入搜索文本
        box = self.wait.until(EC.presence_of_element_located((By.ID, 'com.dangdang.buy2:id/search_edit_input')))
        box.send_keys(KEY_WORD)
        sleep(2)
        # 点击搜索按钮
        button = self.wait.until(EC.presence_of_element_located((By.ID, 'com.dangdang.buy2:id/search_btn_search')))
        button.click()
        sleep(2)

    def scroll(self):
        while True:
            # 模拟拖动
            print("comein")
            str1 = self.driver.page_source
            self.driver.swipe(FLICK_START_X, FLICK_START_Y + FLICK_DISTANCE, FLICK_START_X, FLICK_START_Y)
            sleep(SCROLL_SLEEP_TIME)
            str2 = self.driver.page_source
            if str1 == str2:
                print('到底了')
                break
            print('继续滑动')

    def main(self):
        red_packet = self.wait.until(EC.presence_of_element_located((By.ID, 'com.dangdang.buy2:id/dialog_cancel_tv')))
        # 判断是否出现红包事件
        if red_packet:
            red_packet.click()
            self.content()
        else:
            self.content()
        self.scroll()


if __name__ == '__main__':
    action = Action()
    action.main()
