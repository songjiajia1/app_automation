# 常见控件定位方法
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class TestAppElementLocation:

    def setup(self):
        casp = {}
        casp["platformName"] = "Android"
        casp["appPackage"] = "io.appium.android.apis"
        casp["appActivity"] = ".ApiDemos"
        casp["deviceName"] = "127.0.0.1:7555"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", casp)
        # 隐式等待一般在实例化 driver 之后再设置，它是一个全局的等待方式
        # 每一次调用 find_element 方法的时候，都会触发隐式等待
        self.driver.implicitly_wait(5)

    # id定位
    def test_id(self):
        self.driver.find_element(AppiumBy.ID, 'android:id/text1').click()

    # accessibility_id 定位
    def test_accessibility_id(self):
        ''' android 中 accessibility_id 对应的就是 content-desc 这个字段的值'''
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Animation').click()

    # XPATH 多属性定位
    def test_xpath(self):
        self.driver.find_element(AppiumBy.XPATH, "//*[@resource-id='android:id/text1' and @text='App']")


    '''Android 原生定位'''
    # android uiautomator 定位
    def test_uiautomator(self):
        ele = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                       'new UiSelector().resourceId("android:id/text1")')
        ele.click()

    # 组合定位，可以用多个条件一起定位
    def test_uiautomator2(self):
        ele = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                       'new UiSelector().resourceId("android:id/text1").text("App")')
        ele.click()

    # 模糊定位
    # 通过正则表达式来定位元素，textMatches("^xxx.*") 以 xxx开头的任意元素
    def test_uiautomator3(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textMatches("^xxx.*")')

    # 层级定位
    # 查找兄弟结点：要查找目标元素Text，先找App ，再用 fromParent() 方法查找兄弟结点
    def test_uiautomator4(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("App").fromParent(text("Text")')

    # 根据父结点查找子结点 / 子孙结点
    def test_uiautomator5(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.ListView").childSelector(text("Text")')

    # 滑动查找元素
    def test_uiautomator6(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("查找的元素文本").instance(0)')

