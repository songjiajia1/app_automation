from appium import webdriver
from time import sleep
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
dc={
    "platformName": "Android",
    "platformVersion": "8.0",
    "deviceName": "Android Emulator",
    "app": "D:\\Apks\\app8-debug.apk",
    "appPackage": "com.example.app8",
    "appActivity": ".MainActivity",
    "unicodeKeyboard": True,
    "resetKeyboard": True
}
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",dc)
# 获得屏幕宽度和高度
s=driver.get_window_size()
w=s['width']
h=s['height']
# 多点触控（多根手指同时操作）
# 缩小（两根手指同时向图片中心点方向滑动）
# 第一根手指操作（滑动）
#   起点：x=w*0.2,y=h*0.2
#   终点：x=w*0.4,y=h*0.4
ta1=TouchAction(driver)
ta1.press(x=w*0.2,y=h*0.2).wait(300).move_to(x=w*0.4,y=h*0.4).wait().release()
# 第二根手指操作（滑动）
#   起点：x=w*0.8,y=h*0.8
#   终点：x=w*0.6,y=h*0.6
ta2=TouchAction(driver)
ta2.press(x=w*0.8,y=h*0.8).wait(300).move_to(x=w*0.6,y=h*0.6).wait(300).release()
# 同时执行两根手指的滑动操作
ma1=MultiAction(driver)
ma1.add(ta1,ta2)
ma1.perform()

sleep(2)
#
# # 放大（两根手指同时分别向图片左上角和右下角方向滑动）
# # 第一根手指操作（滑动）
# #   起点：x=w*0.4,y=h*0.4
# #   终点：x=w*0.2,y=h*0.2
# ta3=TouchAction(driver)
# ta3.press(x=w*0.4,y=h*0.4).wait(300).move_to(x=w*0.2,y=h*0.2).wait().release()
# # 第二根手指操作（滑动）
# #   起点：x=w*0.6,y=h*0.6
# #   终点：x=w*0.8,y=h*0.8
# ta4=TouchAction(driver)
# ta4.press(x=w*0.6,y=h*0.6).wait(300).move_to(x=w*0.8,y=h*0.8).wait(300).release()
# # 同时执行两根手指的滑动操作
# ma2=MultiAction(driver)
# ma2.add(ta3,ta4)
# ma2.perform()

# 点击右下角“放大”按钮里的一个坐标位置
ta5=TouchAction(driver)
ta5.tap(x=650,y=1150)
ta5.perform()

sleep(3)
driver.quit()