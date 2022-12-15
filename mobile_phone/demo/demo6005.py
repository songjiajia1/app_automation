from tkinter import W

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
    "app": "D:\\appium\\Apks\\app8-debug.apk",
    "appPackage": "com.example.app8",
    "appActivity": ".MainActivity",
    "unicodeKeyboard": True,
    "resetKryboard": True
}
# 这是“app8-debug.apk”的代码
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",dc)
f = driver.get_window_size()
w = f["width"]
h = f["height"]
print(w,h)  #768,1184

## 缩小图片
'''
多点触控：
一根手指从左上角(x=w*0.2,y=h*0.2)向中心点(x=w*0.4,y=h*0.4)滑动
另一根手指从右下角(x=w*0.8,y=h*0.8)向中心点(x=w*0.6,y=h*0.6)滑动
'''
ta = TouchAction(driver)
ta.press(x=w*0.2,y=h*0.2).wait(500).move_to(x=w*0.4,y=h*0.4).wait(500).release()  # 这里先不调用perform()
ta2 = TouchAction(driver)
ta2.press(x=w*0.8,y=h*0.8).wait(500).move_to(x=w*0.6,y=h*0.6).wait(500).release()  # 这里先不调用perform()
ma = MultiAction(driver)   # 新建MultiAction对象
ma.add(ta,ta2)             # 将TouchAction对象加入到MultiAction的对象集合中
ma.perform()               # 同时执行

sleep(2)
driver.quit()
