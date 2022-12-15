from appium import webdriver
from time import sleep
from appium.webdriver.common.mobileby import MobileBy
dc={
  "platformName": "Android",
  "platformVersion": "6.0",
  "deviceName": "Android Emulator",
  "app": "D:\\Apks\\ContactManager.apk",
  "appPackage": "com.example.android.contactmanager",
  "appActivity": ".ContactManager",
  "unicodeKeyboard": True,
  "resetKeyboard": True
}
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",dc)
# 点击按钮
an=driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'classNameMatches(".*Button")')
an.click()
# 向第一个文本框输入a
wbk1=driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'classNameMatches(".*EditText").instance(0)')
wbk1.send_keys("a")
# 向第二个文本框输入b
wbk2=driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'classNameMatches(".*EditText").instance(1)')
wbk2.send_keys("b")
# 向第三个文本框输入c
wbk3=driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'classNameMatches(".*EditText").instance(2)')
wbk3.send_keys("c")
sleep(3)
driver.quit()