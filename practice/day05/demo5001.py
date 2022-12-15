from appium import webdriver
from time import sleep
from appium.webdriver.common.mobileby import MobileBy
dc={
  "platformName": "Android",
  "platformVersion": "6.0",
  "deviceName": "Android Emulator",
  "appPackage": "com.android.calculator2",
  "appActivity": ".Calculator",
  "unicodeKeyboard": True,
  "resetKeyboard": True
}
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",dc)
# 2
n2=driver.find_element(MobileBy.ID,"digit_2")
n2.click()
# 3   resource-id属性值包含3
# xpath  //*[contains(@resource-id,'3')]
n3=driver.find_element(MobileBy.XPATH,"//*[contains(@resource-id,'3')]")
n3.click()
# 8   text属性值等于8
# xpath  //*[@text='8']
n8=driver.find_element(MobileBy.XPATH,"//*[@text='8']")
n8.click()
# 7   8前面跟它同级同父节点的元素（哥哥节点）
# xpath //*[@text='8']/preceding-sibling::*
n7=driver.find_element(MobileBy.XPATH,"//*[@text='8']/preceding-sibling::*")
n7.click()
# x   8的父节点的弟弟节点的第3个子节点
# xpath //*[@text='8']/../following-sibling::*/*[3]
ch=driver.find_element(MobileBy.XPATH,"//*[@text='8']/../following-sibling::*/*[3]")
ch.click()
# 5
# text("5")
# new UiSelector().text("5")
n5=driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("5")')
n5.click()
# 3
n3=driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'classNameMatches(".*Button.*").text("3")')
n3.click()
# =
# 两个条件组合：resourceIdMatches、description
# resource-id	com.android.calculator2:id/eq
# content-desc	等于
dy=driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'resourceIdMatches(".*eq.*").description("等于")')
dy.click()
# 满足条件的元素有多个的情况,默认操作第1个
a=driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'classNameMatches(".*Button.*")')
a.click()
# 按钮里的第3个
b=driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'classNameMatches(".*Button.*").index(2)')
b.click()
# 第2组里的第3个（也就是整个Layout中的索引号为14的那个），乘号
c=driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'classNameMatches(".*Button").instance(14)')
c.click()
# -   先定位父节点，然后再定位它
jh=driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'resourceIdMatches(".*pad_operator").childSelector(description("减"))')
jh.click()
# 4  通过兄弟关系来查找
n3=driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("6").fromParent(text("4"))')
n3.click()
# =  通过任意一个兄弟找到它
dh=driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("8").fromParent(description("等于"))')
dh.click()
sleep(3)
driver.quit()