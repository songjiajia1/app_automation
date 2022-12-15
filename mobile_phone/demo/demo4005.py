from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction

dc = {
    "automationName": "UiAutomator2",
    "platformName": "Android",
    "platformVersion": "8.0",
    "deviceName": "Aadroid Emulator",
    "app": "D:\\appium\\Apks\\app-welcome.apk",
    "appPackage": "com.example.power.welcomepage",
    "appActivity": ".WelcomeActivity",
    "unicodeKeyboard": True,
    "resetKryboard": True
}

# 实例化Remote对象，也就是发送HTTP请求给Appium Server来启动APP
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",dc)

# 这是“app-welcome.apk”的代码
TouchAction(driver).press(x=712, y=680).move_to(x=51, y=675).release().perform()

TouchAction(driver).press(x=709, y=827).move_to(x=56, y=841).release().perform()

sleep(3)
driver.quit()
