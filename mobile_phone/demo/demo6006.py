import unittest
from appium import webdriver
from time import sleep
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.mobileby import MobileBy
import pytest

class MyTestCase(unittest.TestCase):
    def setUp(self):
        # 启动计算器
        dc = {
            "automationName": "UiAutomator2",
            "platformName": "Android",
            "platformVersion": "8.0",
            "deviceName": "Aadroid Emulator",
            "appPackage": "com.android.calculator2",
            "appActivity": ".Calculator",
            "unicodeKeyboard": True,
            "resetKryboard": True
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",dc)


    def test_1(self):
        # 点击3
        n3 = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("3")')
        n3.click()
        # 检查结果
        res = self.driver.find_element(MobileBy.ID,"com.android.calculator2:id/formula")
        r = res.text
        print(r)
        self.assertEqual(r, "3")

    def test_2(self):
        # 点击4
        n4 = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR, 'text("4")')
        n4.click()
        # 检查结果
        res = self.driver.find_element(MobileBy.ID, "com.android.calculator2:id/formula")
        r = res.text
        print(r)
        self.assertEqual(r, "4")


    def terDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
