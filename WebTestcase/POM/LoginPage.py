from selenium.webdriver.common.by import By

class LoginPage():
    username=(By.XPATH,'//*[@id="username"]')#账户
    password=(By.XPATH,'//*[@id="password"]')#密码
    verification_code=(By.XPATH,'//*[@id="code"]')#验证码输入框
    verification_code_pic=(By.XPATH,'//*[@id="codeimg"]')#验证码图片
    #verification_code_pic = (By.XPATH, '// *[ @ id = "code"]')  # 验证码图片
    login_button=(By.XPATH,'//*[@id="myform"]/div[4]/button[1]')#登录按钮
    reset_button=(By.XPATH,'//*[@id="myform"]/div[4]/button[2]')#重置按钮