from appium import webdriver
from time import sleep
# 1.启动MyAppDemo2
# （1）新建DesiredCapabilities对象
dc={}
dc["automationName"]="UiAutomator2"
dc["platformName"]="Android"# ---必填
dc["platformVersion"]="6.0"# ---必填
dc["deviceName"]="Android Emulator"# ---必填,但是该值不影响识别设备，是指一个业务意义的设备名称，主要用于维护代码时查看，类似于注释的作用
dc["app"]="D:\\Apks\\app2-debug.apk"# ---可选，但是一般建议有安装包的情况下，指定该值。
dc["appPackage"]="com.example.tarena.myappdemo2"# --- 被测App的包名，对于Android应用来说是必填项。重要！！！
dc["appActivity"]=".MainActivity2"# --- 被测App中活动名，代表哪个界面，对于Android应用来说是必填项。重要！！！
# 注意：与包名相同的那段字符串可以省略，但是开头的点不能省略。

# （2）发送HTTP请求，也就是实例化Remote类对象
# 构造函数参数：第1个是HTTP请求地址，第2个是前面所准备好的dc对象
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",dc)
# 2.操作和检查
sleep(3)
# 3.关闭App
driver.quit()