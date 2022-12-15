from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from time import sleep

dc = {
    "automationName": "UiAutomator2",
    "platformName": "Android",
    "platformVersion": "8.0",
    "deviceName": "Aadroid Emulator",
    "app": "D:\\appium\\Apks\\app2-debug.apk",
    "appPackage": "com.example.tarena.myappdemo2",
    "appActivity": ".MainActivity2",
    "unicodeKeyboard": True,
    "resetKryboard": True
}

# 实例化Remote对象，也就是发送HTTP请求给Appium Server来启动APP
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",dc)

# 这是“app2-debug.apk”的代码
# OK
o = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("OK")')
o.click()
# BIGGER(包含IGG)
b = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'textContains("IGG")')
b.click()
# BIGGER(以BI开头)
b = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'textStartsWith("BI")')
b.click()

sleep(3)
driver.quit()
