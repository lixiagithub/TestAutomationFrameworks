print('这是webui自动化目录下的conftest，把登录拆分，1.根目录打开了浏览器被测网站2.登录过程')
import pytest,time
from WebTestcase.POM.HomePage import HomePage
from WebTestcase.POM.LoginPage import LoginPage
from untils.VerificationCode import VerificationCode

@pytest.fixture(scope='module')
def login(openbrowser):
    '''登录过程'''
    openbrowser.send_key_my(LoginPage.username,'9999')#输入用户名
    openbrowser.send_key_my(LoginPage.password,'PBAPP#321')#输入密码
    img = openbrowser.find_my(LoginPage.verification_code_pic)#验证码元素的位置
    VerificationCode().image_str(img)
    openbrowser.send_key_my(LoginPage.verification_code, VerificationCode().image_str(img))#输入验证码
    openbrowser.click_my(LoginPage.login_button)#点击登录按钮
    # try:
    #     if openbrowser.element_visible_times(HomePage.user_name)>0:#验证右上角登录名是否存在，存在代表登录成功
    #         yield openbrowser,True
    # except Exception as e:
    #     yield openbrowser,False

    if openbrowser.element_visible_times(HomePage.user_name) > 0:
        yield openbrowser, True
    else:
        yield openbrowser, False

