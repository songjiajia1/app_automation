from appium import webdriver
from time import sleep
from appium.webdriver.common.mobileby import MobileBy
# 启动ContactManager(联系人管理器)
dc={
    "platformName":"Android",
    "platformVersion":"6.0",
    "deviceName":"Android Emulator",
    "app":"D:\\Apks\\ContactManager.apk",
    "appPackage":"com.example.android.contactmanager",
    "appActivity":".ContactManager",
    "unicodeKeyboard":True,
    "resetKeyboard":True
}
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",dc)
# 点击复选框   content-desc
fxk=driver.find_element(MobileBy.ACCESSIBILITY_ID,"Show Invisible Contacts (Only)")
fxk.click()
# 点击按钮
an=driver.find_element(MobileBy.ACCESSIBILITY_ID,"Add Contact")
an.click()
sleep(3)
driver.quit()