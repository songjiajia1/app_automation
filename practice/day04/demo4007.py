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
fxk=driver.find_element(MobileBy.XPATH,"//android.widget.CheckBox")
fxk.click()
# 点击按钮
an=driver.find_element(MobileBy.XPATH,"//android.widget.Button")
an.click()
sleep(2)
# 输入Name：jack
wbk1=driver.find_element(MobileBy.XPATH,"//android.widget.TableRow[4]/android.widget.EditText[1]")
wbk1.send_keys("jack")
# 输入Phone:123
wbk2=driver.find_element(MobileBy.XPATH,"//android.widget.TableRow[6]/android.widget.EditText[1]")
wbk2.send_keys("123")
# 输入邮箱：a@b.com

sleep(3)
driver.quit()