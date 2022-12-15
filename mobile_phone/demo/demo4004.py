from appium import webdriver
from time import sleep
from appium.webdriver.common.appiumby import AppiumBy

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

# 实例化Remote对象，也就是发送HTTP请求给Appium Server来启动APP
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",dc)

# 这是“android的自带计算器”的代码
el1 = driver.find_element(AppiumBy.ID, "com.android.calculator2:id/digit_8")
el1.click()
el2 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "加")
el2.click()
el3 = driver.find_element(AppiumBy.ID, "com.android.calculator2:id/digit_5")
el3.click()
el4 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "等于")
el4.click()


sleep(2)
driver.quit()
