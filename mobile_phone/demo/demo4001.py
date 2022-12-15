from appium import webdriver
from time import sleep

dc = {
    "automationName": "UiAutomator2",
    "platformName": "Android",
    "platformVersion": "8.0",
    "deviceName": "Aadroid Emulator",
    "app": "D:\\appium\\Apks\\ContactManager.apk",
    "appPackage": "com.example.android.contactmanager",
    "appActivity": ".ContactManager",
    "unicodeKeyboard": True,
    "resetKryboard": True
}

# 实例化Remote对象，也就是发送HTTP请求给Appium Server来启动APP
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",dc)

# 这是“ContactManager.apk”的代码

sleep(2)
driver.quit()
