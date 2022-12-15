from appium import webdriver
from time import sleep
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction


dc={
  "platformName": "Android",
  "platformVersion": "6.0",
  "deviceName": "Android Emulator",
  "app": "D:\\Apks\\app-welcome.apk",
  "appPackage": "com.example.power.welcomepage",
  "appActivity": ".WelcomeActivity",
  "unicodeKeyboard": True,
  "resetKeyboard": True
}
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",dc)
# 获得屏幕宽度和高度（屏幕分辨率、尺寸）
s=driver.get_window_size()
print(s)# 字典类型，key有两个：width宽度、height高度
w=s["width"]
h=s["height"]

for i in range(1,4):
    # 滑动（从右侧向左侧）
    # 起点：x=700-->w*0.9,y=600-->h*0.5
    # 终点：x=50-->w*0.1,y=600-->h*0.5
    # 步骤1：实例化TouchAction对象
    ta=TouchAction(driver)
    # 步骤2：制定动作计划：先按下起点，等待，移动到终点，等待，释放（抬起手指）
    ta.press(x=w*0.9,y=h*0.5).wait(500).move_to(x=w*0.1,y=h*0.5).wait(500).release()
    # 步骤3：重要：一定要执行这一系列的操作动作来完成滑动效果！！！！！！！！！！
    ta.perform()#perform：执行
    # 等待1秒
    sleep(1)
sleep(3)
driver.quit()