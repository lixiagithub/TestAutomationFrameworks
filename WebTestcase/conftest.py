print('这是webui自动化目录下的conftest，把登录拆分，1.根目录打开了浏览器被测网站2.登录过程')
import pytest,time
from WebTestcase.POM.HomePage import HomePage
from WebTestcase.POM.LoginPage import LoginPage
from untils.VerificationCode import VerificationCode
from log.log import logger

@pytest.fixture(scope='module')#只执行一次
def login(openbrowser):
    '''登录过程'''
    openbrowser.send_key_my(LoginPage.username,'9999')#输入用户名
    openbrowser.send_key_my(LoginPage.password,'PBAPP#321')#输入密码
    img = openbrowser.find_my(LoginPage.verification_code_pic)#验证码元素的位置
    if VerificationCode().image_str(img) is not None:
        openbrowser.send_key_my(LoginPage.verification_code, VerificationCode().image_str(img))#输入验证码
        openbrowser.click_my(LoginPage.login_button)#点击登录按钮
        openbrowser.is_iframe(HomePage.main_iframe)#切换iframe
        if openbrowser.element_visible_times(HomePage.assert_login_in) > 0:
            logger.info('登录成功')
            yield openbrowser
            assert True, '登录成功'
        else:
            logger.info('登录失败')
            yield False
            assert False, '登录失败'
    else:
        logger.info('验证码识别错误')
        yield False
        assert False, '验证码识别错误'
