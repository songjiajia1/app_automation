'''雪球 app 搜索功能点自动化测试实战'''

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

'''------用例设计------
打开【雪球】应用首页
点击搜索框（点击之前，判断搜索框的是否可用,并查看搜索框 name 属性值，并获取搜索框坐标，以及它的宽高）
向搜索框输入:alibaba
判断【阿里巴巴】是否可见
如果可见，打印“搜索成功”
如果不可见，打印“搜索失败
'''

'''------用例编写思路------
pytest 测试框架编写
添加隐式等待
添加 setup teardown
添加断言
'''

class TestXueQiu:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '10'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        desired_caps['noReset'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        element = self.driver.find_element(MobileBy.ID,"com.xueqiu.android:id/tv_search")
        search_enabled = element.is_enabled()
        print(f"搜索框的文本：{element.text}，搜索框的坐标：{element.location}，搜索框的size：{element.size}")

        if search_enabled == True:
            element.click()
            self.driver.find_element(MobileBy.ID,
                                     "com.xueqiu.android:id/search_input_text").\
                send_keys("alibaba")
            alibaba_element = self.driver.find_element(MobileBy.XPATH, "//*[@text='阿里巴巴']")
            # alibaba_element.is_displayed()
            displayed = alibaba_element.get_attribute("displayed")
            assert displayed == "true"
        else:
          assert False
