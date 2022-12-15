from appium import webdriver
from time import sleep
# 启动MyAppDemo2
dc={}
dc["automationName"]="UiAutomator2"
dc["platformName"]="Android"
dc["platformVersion"]="6.0"
dc["deviceName"]="Android Emulator"
dc["app"]="D:\\Apks\\app2-debug.apk"
dc["appPackage"]="com.example.tarena.myappdemo2"
dc["appActivity"]=".MainActivity2"
dc["unicodeKeyboard"]=True
dc["resetKeyboard"]=True
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",dc)

el1 = driver.find_element_by_id("com.example.tarena.myappdemo2:id/name")
el1.clear()
el1.send_keys("达内")
el2 = driver.find_element_by_id("com.example.tarena.myappdemo2:id/OK")
el2.click()
el3 = driver.find_element_by_id("com.example.tarena.myappdemo2:id/bigger")
el3.click()

sleep(3)
driver.quit()