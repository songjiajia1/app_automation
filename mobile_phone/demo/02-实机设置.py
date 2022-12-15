from appium import webdriver
from time import sleep

dc = {
    "automationName": "UiAutomator",
    "platformName": "Android",
    "platformVersion": "5.1",
    "deviceName": "Aadroid Emulator",
    "udid": "YLQ4OJU899999999",
    "appPackage": "com.android.settings",
    "appActivity": "com.oppo.settings.SettingsActivity",
    "unicodeKeyboard": True,
    "resetKryboard": True
}

# 实例化Remote对象，也就是发送HTTP请求给Appium Server来启动APP
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",dc)

# 这是“实机设置”的代码
el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.view.View[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[9]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView")
el1.click()
el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.view.View[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[6]/android.widget.LinearLayout/android.widget.RelativeLayout")
el2.click()
el3 = driver.find_element_by_id("android:id/up")
el3.click()
el4 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.view.View[1]/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.RelativeLayout")
el4.click()
el5 = driver.find_element_by_id("android:id/up")
el5.click()
el6 = driver.find_element_by_id("android:id/up")
el6.click()


sleep(3)
driver.quit()
