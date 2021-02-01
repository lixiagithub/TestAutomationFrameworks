from selenium.webdriver.common.by import By
import pytest

class HomePage():
    '''
    管理页面所有的元素（定位方式，元素的值）
    管理操作这些元素的方法
    '''
    # search_input=(By.ID,'search-input')
    # Login_buttom=(By.XPATH,"//*[text()='登录'  and @class='am-btn-primary btn am-fl']")
    # search_button=(By.ID,'ai-topsearch')
    # gouwuche=(By.XPATH,'')
    #
    # sousuojieguo=(By.CLASS_NAME,'am-animation-scale-up') #搜索结果的元素

    #
    # def sosuo(self,openbrowser,value):
    #     openbrowser.send_key_my(HomePage.search_input, value)
    #     openbrowser.click_my(HomePage.search_button)

    assert_user_name=(By.XPATH, '// *[ @ id = "page-wrapper"] / div[1] / nav / div[2] / ul / li[3] / a / span')#右上角用户名
    #assert_user_name = (By.XPATH,'/ html / body / div[1] / div / div / div[2] / div[1] / h3 / text()')  #欢迎您登陆平台