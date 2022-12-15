from appium import webdriver
from time import sleep

dc = {
    "automationName": "UiAutomator",
    "platformName": "Android",
    "platformVersion": "5.1",
    "deviceName": "Aadroid Emulator",
    "udid": "YLQ4OJU899999999",
    "appPackage": "com.i2finance.shexpress",
    "appActivity": "com.pingan.fstandard.activity.MainActivity",
    "unicodeKeyboard": True,
    "resetKryboard": True
}

# 实例化Remote对象，也就是发送HTTP请求给Appium Server来启动APP
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",dc)

# 这是“实机上行快线”的代码

sleep(3)
driver.quit()
