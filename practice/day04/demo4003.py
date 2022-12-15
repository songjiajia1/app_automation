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
n8=driver.find_element(MobileBy.ID,"digit_8")
n8.click()
# +
jh=driver.find_element(MobileBy.ID,"op_add")
jh.click()
# 3
n3=driver.find_element(MobileBy.ID,"com.android.calculator2:id/digit_3")
n3.click()
# =
dh=driver.find_element(MobileBy.ID,"com.android.calculator2:id/eq")
dh.click()
sleep(3)
driver.quit()