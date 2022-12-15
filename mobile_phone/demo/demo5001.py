from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from time import sleep

dc = {
    "automationName": "UiAutomator2",
    "platformName": "Android",
    "platformVersion": "8.0",
    "deviceName": "Aadroid Emulator",
    "app": "D:\\appium\\Apks\\app3-debug.apk",
    "appPackage": "com.example.myappdemo3",
    "appActivity": ".MainActivity",
    "unicodeKeyboard": True,
    "resetKryboard": True
}

# 实例化Remote对象，也就是发送HTTP请求给Appium Server来启动APP
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",dc)

# 这是“app3-debug.apk”的代码

# phone   第一种写法
p = driver.find_element(MobileBy.ID,"com.example.myappdemo3:id/editText4")
p.clear()
p.send_keys("15099998888")
sleep(2)
# phone   第二种写法
p = driver.find_element(MobileBy.ID,"editText4")
p.clear()
p.send_keys("13566667777")
sleep(2)
# email
e = driver.find_element(MobileBy.ID,"editText5")
e.clear()
e.send_keys("1212@qq.com")
sleep(2)
# address
a = driver.find_element(MobileBy.ID,"editText6")
a.clear()
a.send_keys("上海市浦东新区")
sleep(2)
# 用class_name定位，element后边要+s,最后边要加上索引号
s = driver.find_elements(MobileBy.CLASS_NAME,"android.widget.EditText")[1]
s.clear()
s.send_keys("2020@163.cn")

sleep(2)
driver.quit()
