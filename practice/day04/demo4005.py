from appium import webdriver
from time import sleep
from appium.webdriver.common.mobileby import MobileBy
# 启动计算器
dc={
  "platformName": "Android",
  "platformVersion": "6.0",
  "deviceName": "Android Emulator",
  "appPackage": "com.android.calculator2",
  "appActivity": ".Calculator",
  "unicodeKeyboard": True,
  "resetKeyboard": True
}
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",dc)
# 8
n8=driver.find_elements(MobileBy.CLASS_NAME,"android.widget.Button")[1]
n8.click()
# +
jh=driver.find_elements(MobileBy.CLASS_NAME,"android.widget.Button")[16]
jh.click()
# 3
n3=driver.find_elements(MobileBy.CLASS_NAME,"android.widget.Button")[8]
n3.click()
# =
dh=driver.find_elements(MobileBy.CLASS_NAME,"android.widget.Button")[11]
dh.click()
# +
jh=driver.find_element_by_accessibility_id("加")
jh.click()
# 5
n5=driver.find_element(MobileBy.ID,"digit_5")
n5.click()
# =
dh=driver.find_element(MobileBy.ACCESSIBILITY_ID,"等于")
dh.click()
# *
ch=driver.find_element(MobileBy.ACCESSIBILITY_ID,"乘")
ch.click()
# 4
n4=driver.find_element(MobileBy.XPATH,"//*[@*='3' and @text='4']")
n4.click()
# =
dh=driver.find_element(MobileBy.XPATH,"//*[contains(@resource-id,'eq')]")
dh.click()
sleep(3)
driver.quit()