from appium import webdriver
from time import sleep
# 启动MyAppDemo3
dc={
    "platformName":"Android",
    "platformVersion":"6.0",
    "deviceName":"Android Emulator",
    "app":"D:\\Apks\\app3-debug.apk",
    "appPackage":"com.example.myappdemo3",
    "appActivity":".MainActivity",
    "unicodeKeyboard":True,
    "resetKeyboard":True
}
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",dc)

el1 = driver.find_element_by_accessibility_id("手机号输入框")
el1.clear()
el1.send_keys("13012345678")
el2 = driver.find_element_by_id("com.example.myappdemo3:id/editText5")
el2.clear()
el2.send_keys("jack@163.com")
el3 = driver.find_element_by_id("com.example.myappdemo3:id/female")
el3.click()
el4 = driver.find_element_by_id("com.example.myappdemo3:id/sports")
el4.click()

# 等待3秒
sleep(3)
# 关闭App
driver.quit()