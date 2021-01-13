print('根目录的conftest,所有用例执行之前,初始化浏览器，')
from untils.initBrowser import browsertype, BrowserInit
import pytest, time

# def setup_module():
#     print("所有用例开始前只打开一次浏览器")
#     openbrowser()

# def teardown_module():
#     print("所有用例结束只最后关闭浏览器")

@pytest.fixture(scope='module')
def openbrowser():
    '''初始化浏览器方法'''
    # driver=browsertype()#返回浏览器对象
    # return driver
    driver = browsertype()
    browser = BrowserInit(driver)
    yield browser
    print('所有用例执行完毕,后置操作')
    driver.quit()




    # @classmethod
    # def setUpClass(self):
    #     '''浏览器设置'''
    #     self.browser=BrowserInit(self.browserName,self.url)
    # @classmethod
    # def tearDownClass(self):
    #     "关闭浏览器"
    #     self.browser.quit()

from untils.initAPP import apptype, Initapp


@pytest.fixture()
def openapp():
    '''初始化app'''
    # app=apptype()
    # yield app

    app = Initapp(apptype())
    yield app