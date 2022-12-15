from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class TestAppDemo:

    def setup(self):
        # 创建一个字典，desired_capabilities
        caps = {}
        # android 包名和页面名
        caps["platformName"] = "Android"
        caps["appPackage"] = "io.appium.android.apis"
        caps["appActivity"] = ".ApiDemos"
        # 设备名，任意取名都可以
        caps["deviceName"] = "127.0.0.1:7555"
        # 创建driver，与appium server 建立连接，返回一个session 对象
        # 实例化Remote对象，也就是发送HTTP请求给Appium Server来启动APP
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # 上边的 driver 加上self 后，就由局部变量变成了实例变量，在其他方法中就可以调用了
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_input(self):
        el2 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "OS")
        el2.click()
        el3 = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Morse Code")
        el3.click()
        el4 = self.driver.find_element(AppiumBy.ID, "io.appium.android.apis:id/text")
        el4.send_keys("ceshiren.com")
        self.driver.back()
        self.driver.back()
        self.driver.back()
        # 断言
        text = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Accessibility').text
        assert text == 'Accessibility'


