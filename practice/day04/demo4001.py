from appium import webdriver
from time import sleep
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

el1 = driver.find_element_by_accessibility_id("Show Invisible Contacts (Only)")
el1.click()
el2 = driver.find_element_by_accessibility_id("Add Contact")
el2.click()
el3 = driver.find_element_by_id("com.example.android.contactmanager:id/contactNameEditText")
el3.send_keys("jack")
el4 = driver.find_element_by_id("com.example.android.contactmanager:id/contactPhoneEditText")
el4.send_keys("13012345678")
el5 = driver.find_element_by_id("com.example.android.contactmanager:id/contactEmailEditText")
el5.send_keys("jack@163.com")
el6 = driver.find_element_by_id("com.example.android.contactmanager:id/contactEmailTypeSpinner")
el6.click()
el7 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.ListView/android.widget.CheckedTextView[2]")
el7.click()

# 等待3秒
sleep(3)
# 关闭App
driver.quit()