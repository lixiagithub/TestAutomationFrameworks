print('这是webui自动化目录下的conftest，把登录拆分，1.根目录打开了浏览器被测网站2.登录过程')
import pytest,time
from WebTestcase.POM.HomePage import HomePage
from WebTestcase.POM.LoginPage import LoginPage
from untils.VerificationCode import VerificationCode

@pytest.fixture(scope='module')#只执行一次
def login(openbrowser):
    '''登录过程'''
    openbrowser.send_key_my(LoginPage.username,'9999')#输入用户名
    openbrowser.send_key_my(LoginPage.password,'PBAPP#321')#输入密码
    img = openbrowser.find_my(LoginPage.verification_code_pic)#验证码元素的位置
    openbrowser.send_key_my(LoginPage.verification_code, VerificationCode().image_str(img))#输入验证码
    openbrowser.click_my(LoginPage.login_button)#点击登录按钮

    if openbrowser.element_visible_times(HomePage.assert_user_name) > 0:
        yield openbrowser
        assert True, '登录成功'
    else:
        yield False
        assert False, '登录失败'
