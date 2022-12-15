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
# 点击复选框
fxk=driver.find_element_by_class_name("android.widget.CheckBox")
fxk.click()
# 点击按钮
an=driver.find_element(MobileBy.CLASS_NAME,"android.widget.Button")
an.click()
# 输入123---向第1个文本框输入
wbk=driver.find_element(MobileBy.CLASS_NAME,"android.widget.EditText")
wbk.send_keys("123")
# 输入456---向第2个文本框输入
wbk2=driver.find_elements(MobileBy.CLASS_NAME,"android.widget.EditText")[1]
wbk2.send_keys("456")
# 输入789---向第3个文本框输入
wbk3=driver.find_elements(MobileBy.CLASS_NAME,"android.widget.EditText")[2]
wbk3.send_keys("789")
sleep(3)
driver.quit()