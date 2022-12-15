from appium import webdriver
from time import sleep
dc={
    "platformName":"Android",
    "platformVersion":"6.0",
    "deviceName":"Android Emulator",
    "appPackage":"com.example.tarena.myappdemo2",
    "appActivity":".MainActivity2",
    "unicodeKeyboard":True,#--可选项，用于支持中文或特殊符号的输入。
    "resetKeyboard":True#--可选项，一般搭配unicodeKeyboard一起使用，用于重置输入法。
}
driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",dc)
sleep(3)
driver.quit()
