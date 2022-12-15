from appium import webdriver
from time import sleep
from appium.webdriver.common.mobileby import MobileBy
dc={
    "platformName": "Android",
    "platformVersion": "6.0",
    "deviceName": "Android Emulator",
    "app": "D:\\Apks\\app2-debug.apk",
    "appPackage": "com.example.tarena.myappdemo2",
    "appActivity": ".MainActivity2",
    "unicodeKeyboard": True,
    "resetKeyboard": True
}
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",dc)
# 点击OK
ok=driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("OK")')
ok.click()
# 点击Bigger
b=driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'textContains("igg")')
b.click()
sleep(3)
driver.quit()