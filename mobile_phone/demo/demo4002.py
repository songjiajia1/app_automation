from appium import webdriver
from time import sleep
from appium.webdriver.common.appiumby import AppiumBy

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
el1 = driver.find_element(AppiumBy.ID, "com.example.tarena.myappdemo2:id/name")
el1.clear()
el1.send_keys("lisi")


sleep(2)
driver.quit()
