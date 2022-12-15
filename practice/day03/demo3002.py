from appium import webdriver
from time import sleep
# 启动计算器
dc={
    "platformName":"Android",
    "platformVersion":"6.0",
    "deviceName":"Android Emulator",
    "appPackage":"com.android.calculator2",
    "appActivity":".Calculator",
    "unicodeKeyboard":True,
    "resetKeyboard":True
}
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",dc)
# 3+5=
el1 = driver.find_element_by_id("com.android.calculator2:id/digit_3")
el1.click()
el2 = driver.find_element_by_accessibility_id("加")
el2.click()
el3 = driver.find_element_by_id("com.android.calculator2:id/digit_5")
el3.click()
el4 = driver.find_element_by_accessibility_id("等于")
el4.click()
# 7x9=
el1 = driver.find_element_by_id("com.android.calculator2:id/digit_7")
el1.click()
el2 = driver.find_element_by_accessibility_id("乘")
el2.click()
el3 = driver.find_element_by_id("com.android.calculator2:id/digit_9")
el3.click()
el4 = driver.find_element_by_accessibility_id("等于")
el4.click()
# 等待3秒
sleep(3)
# 关闭App
driver.quit()