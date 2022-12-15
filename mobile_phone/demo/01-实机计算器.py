from appium import webdriver


# 新建DesiredCapabilities对象
dc = {
    "automationName": "UiAutomator",    # 如果是安卓7.0以下的版本就写：UiAutomator
    "platformName": "Android",
    "platformVersion": "5.1",
    "deviceName": "Aadroid Emulator",   # 如果是真机就写手机的型号
    "udid": "XPL0220707013022",         # 如果是真机就在cmd中输入：adb devices,找到手机的设备号，比如：XPL0220707013022
    # "app": "D:\\Apks\...\...apk",     # 如果是本地就写本地的安装包路径，如果是真机就写安装包的路径
    "appPackage": "com.android.calculator2",    # 这是应用的包名
    "appActivity": ".Calculator",
    "unicodeKeyboard": True,            # 是否使用unicode输入法来支持中文和特殊字符输入，它是布尔值,一般填True
    "resetKryboard": True               # 重置输入法，搭配unicodeKeyboard一起使用
}
# 实例化Remote对象，也就是发送HTTP请求给Appium Server来启动APP
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",dc)

# 这是“实机计算器”的代码
el1 = driver.find_element_by_id("com.android.calculator2:id/digit8")
el1.click()
el2 = driver.find_element_by_id("com.android.calculator2:id/plus")
el2.click()
el3 = driver.find_element_by_id("com.android.calculator2:id/digit2")
el3.click()
el4 = driver.find_element_by_id("com.android.calculator2:id/minus")
el4.click()
el5 = driver.find_element_by_id("com.android.calculator2:id/digit5")
el5.click()
el6 = driver.find_element_by_id("com.android.calculator2:id/equal")
el6.click()

# 等待3秒
sleep(3)
# 关闭App，调用quit函数
driver.quit()
