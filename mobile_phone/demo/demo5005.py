from appium import webdriver
from time import sleep
from appium.webdriver.common.mobileby import MobileBy

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

# 点击复选框，使用descriptionContains方法包含‘visi’定位
# fxk = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'descriptionContains("visi")')
# 用className定位复选框
# fxk = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'className("android.widget.CheckBox")')
# class和content-desc组合使用定位复选框
fxk = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'className("android.widget.CheckBox").descriptionContains("visi")')
fxk.click()

# 点击按钮，使用descriptionStartsWith方法以‘Add’开头定位
# an = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'descriptionStartsWith("Add")')
# 使用classNameMatches定位按钮
an = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'classNameMatches(".*Button$")')
an.click()

# ContactName   使用resourceId精确定位
name = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'resourceId("com.example.android.contactmanager:id/contactNameEditText")')
name.send_keys("张三")

# ContactPhone  使用resourceIdMatches模糊定位(包含PhoneEd)
# com.example.android.contactmanager:id/contactPhoneEditText
phone = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'resourceIdMatches(".*PhoneEd.*")')
phone.send_keys("0311-12121234")

# ContactEmail(以EmailEditText结尾)
# com.example.android.contactmanager:id/contactEmailEditText
Email = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'resourceIdMatches(".*EmailEditText$")')
Email.send_keys("zhangsan@qq.com")

sleep(2)
driver.quit()

