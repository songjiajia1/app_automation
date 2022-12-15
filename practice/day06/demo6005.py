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
            "app": "D:\\Apks\\app3-debug.apk",
            "appPackage": "com.example.myappdemo3",
            "appActivity": ".MainActivity",
            "unicodeKeyboard": True,
            "resetKeyboard": True
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", dc)

    def test_something(self):
        # 检查男单选按钮默认被选中
        nan=self.driver.find_element(MobileBy.ID,"male")
        zt=nan.get_attribute("checked")
        print(zt)
        print(type(zt))# str
        self.assertEqual(zt,"true")
        # 点击取消
        qx=self.driver.find_element(MobileBy.ID,"cancel")
        qx.click()
        # 检查界面跳转到取消理由填写页
        a=self.driver.current_activity
        print(a)
        self.assertEqual(a,".CancelActivity")


    def tearDown(self):
        sleep(3)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
