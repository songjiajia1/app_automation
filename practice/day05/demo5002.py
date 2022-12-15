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
# 点击复选框
# text   Show Invisible Contacts (Only)
# fxk=driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'textContains("visi")')
# fxk=driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'textStartsWith("Show")')
# fxk=driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'textMatches(".*ow.*")')
# class	android.widget.CheckBox
# fxk=driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'className("android.widget.CheckBox")')
fxk=driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'classNameMatches(".*Check.*")')
fxk.click()
# 点击按钮  content-desc  Add Contact
# an=driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'descriptionContains("Add")')
# an=driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'descriptionStartsWith("Add")')
an=driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'descriptionMatches("^Add.*")')
an.click()
sleep(2)
# 输入姓名Name
# resource-id	com.example.android.contactmanager:id/contactNameEditText
n=driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'resourceId("com.example.android.contactmanager:id/contactNameEditText")')
n.send_keys("lisi")
# 清空姓名Name
n=driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'resourceIdMatches(".*contactName.*")')
n.clear()
# 输入电话号：123
# resource-id	com.example.android.contactmanager:id/contactPhoneEditText
d=driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'resourceId("com.example.android.contactmanager:id/contactPhoneEditText")')
d.send_keys("123")
# 输入邮箱：abc
# resource-id	com.example.android.contactmanager:id/contactEmailEditText
y=driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'resourceIdMatches(".*contactEmail.*")')
y.send_keys("abc")
sleep(3)
driver.quit()
