from appium import webdriver
from time import sleep
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction

dc = {
    "automationName": "UiAutomator2",
    "platformName": "Android",
    "platformVersion": "8.0",
    "deviceName": "Aadroid Emulator",
    "app": "D:\\appium\\Apks\\app-welcome.apk",
    "appPackage": "com.example.power.welcomepage",
    "appActivity": ".WelcomeActivity",
    "unicodeKeyboard": True,
    "resetKryboard": True
}

# 实例化Remote对象，也就是发送HTTP请求给Appium Server来启动APP
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",dc)

# 这是“app-welcome.apk”的代码
# 从右向左滑动
ta = TouchAction(driver)
ta.press(x=720,y=600).wait(500).move_to(x=80,y=600).wait(500).release()
ta.perform()
sleep(1)

# 从右向左滑动2次
for i in range(1,3):
    print("从右向左第",i,"次滑动")
    ta = TouchAction(driver)
    ta.press(x=720,y=600).wait(500).move_to(x=80,y=600).wait(500).release()
    ta.perform()
    sleep(1)

# 从左向右做3次滑动
for i in range(1,4):
    print("从左向右第",i,"次滑动")
    # 案例：WebcomtPage从左向右滑动，起点（在右侧中间位置，坐标值x=80,y=600,终点（在左侧中间位置，坐标值x=720,y=600））
    ta1 = TouchAction(driver)
    ta1.press(x=80,y=600).wait(500).move_to(x=720,y=600).wait(500).release()
    ta1.perform()
    ta1.perform()

sleep(2)
driver.quit()
