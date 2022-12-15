from appium import webdriver
from time import sleep
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

dc = {
    "automationName": "UiAutomator2",
    "platformName": "Android",
    "platformVersion": "8.0",
    "deviceName": "Aadroid Emulator",
    "app": "D:\\appium\\Apks\\de.penguindevelopers.paint_2.0_liqucn.com.apk",
    "appPackage": "de.penguindevelopers.paint",
    "appActivity": ".main",
    "unicodeKeyboard": True,
    "resetKryboard": True
}

# 这是“de.penguindevelopers.paint_2.0_liqucn.com.apk”的代码

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",dc)
# 获得屏幕分辨率
f = driver.get_window_size()
w = f["width"]
h = f["height"]
print(w,h)  # 768,1184
# 从上向下画一条竖线（居中）
ta = TouchAction(driver)
ta.press(x=w*0.5,y=h*0.3).wait(500).move_to(x=w*0.5,y=h*0.8).wait(500).release()
ta.perform()
# 左侧画7的形状
ta1 = TouchAction(driver)
ta1.press(x=w*0.2,y=h*0.4).wait(500).move_to(x=w*0.4,y=h*0.4).wait(500).move_to(x=w*0.4,y=h*0.7).wait(500).release()
ta1.perform()


sleep(2)
driver.quit()
