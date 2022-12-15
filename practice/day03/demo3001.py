from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
# 启动WelcomePage
dc={}
dc["automationName"]="UiAutomator2"
dc["platformName"]="Android"
dc["platformVersion"]="6.0"
dc["deviceName"]="Android Emulator"
dc["app"]="D:\\Apks\\app-welcome.apk"
dc["appPackage"]="com.example.power.welcomepage"
dc["appActivity"]=".WelcomeActivity"
dc["unicodeKeyboard"]=True
dc["resetKeyboard"]=True
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",dc)
# 滑动
TouchAction(driver).press(x=709, y=576).move_to(x=54, y=568).release().perform()

TouchAction(driver).press(x=692, y=508).move_to(x=90, y=508).release().perform()

# 等待3秒
sleep(3)
# 关闭App
driver.quit()
