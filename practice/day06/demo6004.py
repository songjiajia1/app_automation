import unittest
from appium import webdriver
from time import sleep
from appium.webdriver.common.mobileby import MobileBy
import warnings

class MyTestCase(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore",ResourceWarning)
        dc={
            "platformName": "Android",
            "platformVersion": "8.0",
            "deviceName": "Android Emulator",
            "app": "D:\\Apks\\app4-debug.apk",
            "appPackage": "com.example.app4",
            "appActivity": ".MainActivity",
            "unicodeKeyboard": True,
            "resetKeyboard": True
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", dc)

    def test_something(self):
        # 输入第一个数20
        wbk1=self.driver.find_element(MobileBy.ID,"num1")
        wbk1.send_keys("20")
        # 输入第二个数30
        wbk2 = self.driver.find_element(MobileBy.ID, "num2")
        wbk2.send_keys("30")
        # 点击“计算”按钮
        js=self.driver.find_element(MobileBy.ID,"button1")
        js.click()
        # 检查结果文本框中计算结果是50
        wbk3=self.driver.find_element(MobileBy.ID,"result")
        # 说明：获得文本框里的文本只需要使用元素的text属性就可以获得。
        jsjg=wbk3.text
        self.assertEqual(jsjg, "50")

    def tearDown(self):
        sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
