from appium import webdriver
from time import sleep
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction

dc = {
    "automationName":"UiAutomator2",
    "platformName":"Android",
    "platformVersion":"8.0",
    "deviceName":"Android Emulator",
    "app":"D:\\appium\\Apks\\app3-debug.apk",
    "appPackage":"com.example.myappdemo3",
    "appActivity":".MainActivity",
    "unicodekeyboard":"True",
    "resetkeyboard": "True",
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",dc)
wbk1 = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'resourceId("com.example.myappdemo3:id/editText4")')
wbk1.clear()
wbk1.send_keys("13011112222")
wbk2 = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'resourceIdMatches(".*editText5$")')
wbk2.clear()
wbk2.send_keys("112233")
wbk3 = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'classNameMatches(".*EditText$").resourceIdMatches(".*editText6$")')
wbk3.clear()
wbk3.send_keys("上海浦东")

# 轻触确定
# 实例化TouchAction
ta = TouchAction(driver)
ta.tap(x=300,y=890)
ta.perform()  # 这个方法的作用是把动作执行下去
# 轻触取消
ta2 = TouchAction(driver)
ta2.tap(x=500,y=900)
ta2.perform()

sleep(3)
driver.quit()
