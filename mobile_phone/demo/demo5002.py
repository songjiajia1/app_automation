from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from time import sleep

# 计算器
dc = {
    "automationName": "UiAutomator2",
    "platformName": "Android",
    "platformVersion": "8.0",
    "deviceName": "Aadroid Emulator",
    "appPackage": "com.android.calculator2",
    "appActivity": ".Calculator",
    "unicodeKeyboard": True,
    "resetKryboard": True
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",dc)
# 定位3
n3 = driver.find_element(MobileBy.XPATH,"//android.widget.Button[9]")
n3.click()
# 定位7
n7 = driver.find_element(MobileBy.XPATH,"//android.widget.LinearLayout[@content-desc='数字和基本操作']/android.view.ViewGroup[1]/android.widget.Button[1]")
n7.click()
# 定位DEL
n3 = driver.find_element(MobileBy.XPATH,"//android.widget.Button[@content-desc='删除']")
n3.click()
# 定位 +
jh = driver.find_element(MobileBy.XPATH,"//android.widget.Button[@content-desc='加']")
jh.click()
# 定位1
y = driver.find_element(MobileBy.XPATH,"//android.widget.Button[@text='1']")
y.click()

sleep(2)
driver.quit()
