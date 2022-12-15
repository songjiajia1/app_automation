from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from time import sleep

# 计算器
dc = {
    "automationName": "UiAutomator2",
    "platformName": "Android",
    "platformVersion": "8.0",
    "deviceName": "Aadroid Emulator",
    "appPackage": "com.android.calculator2",
    "appActivity": ".Calculator",
    "unicodeKeyboard": True,
    "resetKryboard": True
}
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",dc)
# *用于/或//后边，代表任意标记名称
# 3   resourceIdMatches .*3$, text 3
n3 = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'resourceIdMatches(".*3$").text("3")')
n3.click()
# 5
n5 = driver.find_element(MobileBy.XPATH,"//*[@text='5']")
n5.click()
# 6
n6 = driver.find_element(MobileBy.XPATH,"//*[@index='5']")
n6.click()
# 8
n8 = driver.find_element(MobileBy.XPATH,"//*[@text='7']/../*[2]")
n8.click()
# 7
n7 = driver.find_element(MobileBy.XPATH,"//*[@text='8']/preceding-sibling::*")  # 哥哥节点（preceding-sibling::）
n7.click()                                                                      # 弟弟节点（following-sibling::）
# *用于@后边，代表任意属性名称
# android.widget.Button[@*='5']  --- 找到5和6

# Android_UIautomator框架里边的UISelector类中的定位方法：

### text方法
# 3
# n3 = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'new.UiSelector().text("3")')
n3 = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'text("3")')
n3.click()
# DEL                                                 # 这个是包含文本值，一般用于text属性值过长的时候，用包含来定位
dl1 = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'textContains("E")')
dl1.click()
# textStartsWith()方法是：某个文本以什么开头
# textMatches()方法是：.*e .*表示：e的前边有任意字符串，e的后边也有任意字符串  --描述的是字符串的正则表达式规则

### description方法:   content-desc属性值等于某值
# .  content-desc 小数点
xsd = driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,'description("小数点")')
xsd.click()

# descriptionContains方法：content-desc的属性值包含某值，参数是该属性值的一部分字符串
# descriptionStartsWith方法：content-desc的属性值以某字符串开头
# descriptionMatches方法：content-desc的属性值符合某字符串规则，参数是正则表达式
##  示例： 以‘小’开头，以‘点’结束:  'descriptionMatches("^小.*点$")'   ^表示开头，$表示结尾


sleep(2)
driver.quit()

