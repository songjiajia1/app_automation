from appium import webdriver
from time import sleep
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
dc={
    "platformName": "Android",
    "platformVersion": "6.0",
    "deviceName": "Android Emulator",
    "app": "D:\\Apks\\de.penguindevelopers.paint_2.0_liqucn.com.apk",
    "appPackage": "de.penguindevelopers.paint",
    "appActivity": ".main",
    "unicodeKeyboard": True,
    "resetKeyboard": True
}
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",dc)
# 获得屏幕宽度和高度
s=driver.get_window_size()
w=s["width"]
h=s["height"]
# 画竖线
# 提示：起点  x=w*0.5   y=h*0.3
#       终点  x=w*0.5   y=h*0.8
ta=TouchAction(driver)
ta.press(x=w*0.5,y=h*0.3).wait(300).move_to(x=w*0.5,y=h*0.8).wait(300).release()
ta.perform()
# 连续滑动
# 画L型折线,在原来的竖线左侧
# 起点：x=w*0.2,y=h*0.4
# 中间转折点：x=w*0.2,y=h*0.7
# 终点：x=w*0.4,y=h*0.7
ta2=TouchAction(driver)
ta2.press(x=w*0.2,y=h*0.4).wait(300).move_to(x=w*0.2,y=h*0.7).wait(300).move_to(x=w*0.4,y=h*0.7).wait(300).release()
ta2.perform()
# 连续滑动
# 画Z型折线,在原来的竖线右侧，与L位置对称
# 起点：x=w*0.6,y=h*0.4
# 转折点1：x=w*0.8,y=h*0.4
# 转折点2：x=w*0.6,y=h*0.7
# 终点：x=w*0.8,y=h*0.7
ta3=TouchAction(driver)
ta3.press(x=w*0.6,y=h*0.4).wait(300).move_to(x=w*0.8,y=h*0.4).wait(300).move_to(x=w*0.6,y=h*0.7).wait(300).move_to(x=w*0.8,y=h*0.7).wait(300).release()
ta3.perform()
sleep(3)
driver.quit()