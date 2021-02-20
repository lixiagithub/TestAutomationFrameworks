print('根目录的conftest,所有用例执行之前,初始化浏览器，')
from untils.initBrowser import browsertype, BrowserInit
import pytest, time
from untils import gird_module

# def setup_module():
#     print("所有用例开始前只打开一次浏览器")
#     openbrowser()

# def teardown_module():
#     print("所有用例结束只最后关闭浏览器")

# from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# import time, os.path
# import gird_module
# for host, browser in gird_module.grid().items():
#     driver = webdriver.Remote(
#         command_executor=host,
#         desired_capabilities={
#             'platform': 'ANY',
#             'browserName': browser,
#             'version': '',
#             'javascriptEnabled': True
#         }
#     )
#     driver.get("http://www.baidu.com")
#     driver.find_element_by_id("kw").send_keys(u"中国")
#     driver.find_element_by_id("su").click()
#     time.sleep(3)
#     if driver.title == u"中国_百度搜索":
#         print("title匹配！")
#     else:
#         print("title不匹配！")
#     driver.close()


# @pytest.mark.parametrize("host,browser",
#                             [("132.138.7.182:5588/wd/hub", "firefox"), ("132.134.10.126:5577/wd/hub", "chrome")])

# 声明使用request测试固件
@pytest.fixture(scope='session')#只执行一次
def openbrowser():
    '''初始化浏览器方法'''
    # driver=browsertype()#返回浏览器对象
    # return driver
    driver = browsertype()
    browser = BrowserInit(driver)
    yield browser
    print('所有用例执行完毕,后置操作')
    driver.quit()


# def openbrowser(request):
#     '''初始化浏览器方法'''
#     # driver=browsertype()#返回浏览器对象
#     # return driver
#     for host, browser in gird_module.grid().items():
#         driver = browsertype(host,browser)
#         browser = BrowserInit(driver)
#         # yield browser
#         # print('所有用例执行完毕,后置操作')
#         # driver.quit()
#
#         def fin():
#             # 后置操作teardown
#             print('所有用例执行完毕,后置操作')
#             driver.quit()
#
#         request.addfinalizer(fin)
#         # 返回前置操作的变量
#         return browser


# def test_openbrowser(host,browser):
#     openbrowser(host, browser)
#
#     @classmethod
#     def setUpClass(self):
#         '''浏览器设置'''
#         self.browser=BrowserInit(self.browserName,self.url)
#     @classmethod
#     def tearDownClass(self):
#         "关闭浏览器"
#         self.browser.quit()

from untils.initAPP import apptype, Initapp


@pytest.fixture()
def openapp():
    '''初始化app'''
    # app=apptype()
    # yield app

    app = Initapp(apptype())
    yield app