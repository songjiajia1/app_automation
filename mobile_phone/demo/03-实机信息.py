from appium import webdriver
from time import sleep

dc = {
    "automationName": "UiAutomator",
    "platformName": "Android",
    "platformVersion": "5.1",
    "deviceName": "Aadroid Emulator",
    "udid": "YLQ4OJU899999999",
    "appPackage": "com.android.mms",
    "appActivity": ".ui.ConversationList",
    "unicodeKeyboard": True,
    "resetKryboard": True
}

# 实例化Remote对象，也就是发送HTTP请求给Appium Server来启动APP
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",dc)

# 这是“实机信息”的代码

sleep(3)
driver.quit()
