# coding = utf-8
# Author:李昰 
# Date：2021/5/20 9:33
from selenium.webdriver.common.by import By


class AirTrafficControlMicroVisionClassifyPage():
    atcmvcinfor_tab_close_button = (By.XPATH, '/html/body/div[2]/div/div[2]/nav/div/a[2]/i')  # 空管微视页面关闭
    atcmvcinfor_iframe = (By.XPATH, '//*[@id="content-main"]/iframe[2]')  # 空管微视页面iframe
    assert_atcmvcinfor_page_text = (By.XPATH, '/html/body/div[1]/div/div/div[3]/div[1]/div[1]/span[1]')  # 空管微视类型
    atcmvcinfor_classify = (By.XPATH, '//*[@id="treeDemo"]/li/ul/li')  # 左侧树形空管微视分类

    '''顶级栏目新增'''
    atcmvcinfor_add_topcol_button = (By.XPATH, "//*[text()='添加顶级栏目']")  # 添加顶级栏目按钮
    assert_atcmvcinfor_add_topcol_page_text = (By.CLASS_NAME, 'layui-layer-title')  # 空管微视主栏目新增文本title校验
    atcmvcinfor_add_topcol_page_close_button = (By.XPATH, '/html/body/div[5]/span[1]/a')  # 拖动新增顶级栏目界面上方的标题栏
    atcmvcinfor_add_topcol_name = (By.XPATH, '//*[@id="cat_name"]')  # 空管微视主栏目名称
    atcmvcinfor_add_topcol_submit_button = (By.XPATH, "//*[text()='提交']")  # 空管微视主栏目新增提交按钮
    atcmvcinfor_add_topcol_cancel_button = (By.XPATH, "//*[text()='取消']")  # 空管微视主栏目新增取消按钮
    assert_atcmvcinfor_add_topcol_message_text = (By.CLASS_NAME, 'layui-layer-padding')  # 主栏目添加是否成功文本
    atcmvcinfor_table_all = (By.CLASS_NAME, 'unread')  # 获取所有栏目
    atcmvcinfor_table_topcal_name = 'td:nth-child(1)'  # 栏目名称

    '''顶级栏目修改'''
    atcmvcinfor_update_table_topcol_button = 'td:nth-child(8) >a.btn.blue.btn-xs.btn-outline'  # 编辑顶级栏目按钮
    assert_atcmvcinfor_updage_topcol_page_text = (By.CLASS_NAME, 'layui-layer-title')  # 顶级栏目编辑文本title校验
    atcmvcinfor_update_topcol_page_close_button = (By.XPATH, '/html/body/div[5]/span[1]/a')  # 拖动修改顶级栏目界面上方的标题栏
    atcmvcinfor_update_topcal_name = (By.XPATH, '//*[@id="cat_name"]')  #修改界面顶级栏目名称
    assert_page_atcmvcinfor_update_text = (By.XPATH, '/html/body/div[5]/div[1]')  # 顶级栏目编辑文本title校验
    atcmvcinfor_update_submit_button = (By.XPATH, "//*[text()='提交']")  # 顶级栏目编辑提交按钮
    atcmvcinfor_update_cancel_button = (By.XPATH, "//*[text()='取消']")  # 顶级栏目编辑取消按钮
    assert_atcmvcinfor_update_message_text = (By.CLASS_NAME, 'layui-layer-padding')  # 顶级栏目编辑是否成功文本

    '''顶级栏目停用'''
    atcmvcinfor_block_up_table_topcol_button = 'td:nth-child(8) >a.btn.red.btn-xs.btn-outline'  # 停用顶级栏目按钮
    assert_atcmvcinfor_block_up_topcol_alert_text = (By.CLASS_NAME, 'layui-layer-content')  # 停用顶级栏目提示框文本校验
    atcmvcinfor_block_up_topcol_alert_submit_button = (By.CLASS_NAME, 'layui-layer-btn0')  # 停用顶级栏目确定按钮
    atcmvcinfor_block_up_topcol_alert_cancel_button = (By.CLASS_NAME, 'layui-layer-btn1')  # 停用顶级栏目取消按钮
    assert_atcmvcinfor_block_up_topcol_message_text = (By.CLASS_NAME, 'layui-layer-content')  # 停用顶级栏目是否成功文本

    '''顶级栏目启用'''
    atcmvcinfor_start_using_table_topcol_button = 'td:nth-child(8) >a.btn.green.btn-xs.btn-outline'  # 启用顶级栏目按钮
    assert_atcmvcinfor_start_using_topcol_alert_text = (By.CLASS_NAME, 'layui-layer-content')  # 启用顶级栏目提示框文本校验
    atcmvcinfor_start_using_topcol_alert_submit_button = (By.CLASS_NAME, 'layui-layer-btn0')  # 启用顶级栏目确定按钮
    atcmvcinfor_start_using_topcol_alert_cancel_button = (By.CLASS_NAME, 'layui-layer-btn1')  # 启用顶级栏目取消按钮
    assert_atcmvcinfor_start_using_topcol_message_text = (By.CLASS_NAME, 'layui-layer-content')  # 启用顶级栏目是否成功文本

    '''子栏目新增'''
    atcmvcinfor_add_table_soncol_button = 'td:nth-child(8) > a.btn.yellow-p5.btn-xs.btn-outline'  # 添加子栏目按钮
    assert_atcmvcinfor_add_soncol_page_text = (By.CLASS_NAME, 'layui-layer-title')  # 空管微视子栏目新增文本title校验
    atcmvcinfor_add_soncol_page_close_button = (By.XPATH, '/html/body/div[5]/span[1]/a')  # 拖动新增子栏目界面上方的标题栏
    atcmvcinfor_add_soncol_name = (By.XPATH, '//*[@id="cat_name"]')  # 空管微视子栏目名称
    atcmvcinfor_add_soncol_submit_button = (By.XPATH, "//*[text()='提交']")  # 空管微视子栏目新增提交按钮
    atcmvcinfor_add_soncol_cancel_button = (By.XPATH, "//*[text()='取消']")  # 空管微视子栏目新增取消按钮
    assert_atcmvcinfor_add_soncol_message_text = (By.CLASS_NAME, 'layui-layer-padding')  # 子栏目添加是否成功文本

    '''栏目删除'''
    atcmvcinfor_delete_button = 'td:nth-child(8) > a.btn.red.btn-xs.btn-outline'  # 栏目删除按钮
    assert_atcmvcinfor_delete_alert_text = (By.CLASS_NAME, 'layui-layer-content')  # 栏目删除提示框文本校验
    atcmvcinfor_delete_alert_submit_button = (By.CLASS_NAME, 'layui-layer-btn0')  # 栏目删除确定按钮
    atcmvcinfor_delete_alert_cancel_button = (By.CLASS_NAME, 'layui-layer-btn1')  # 栏目删除取消按钮
    assert_delete_message_text = (By.CLASS_NAME, 'layui-layer-content')  # 栏目删除是否成功文本

    def click_atcmvcinfor_tab_close_button(self, openbrowser):
        '''封装点击关闭按钮'''
        openbrowser.click_my(AirTrafficControlMicroVisionClassifyPage.atcmvcinfor_tab_close_button)

    def into_atcmvcinfor_iframe(self, openbrowser):
        '''封装进入iframe'''
        openbrowser.is_iframe(AirTrafficControlMicroVisionClassifyPage.atcmvcinfor_iframe)

    def assert_atcmvcinfor_page_textcontent(self, openbrowser):
        '''封装判断页面文本是否一致,来判断是否进入空管微视页面'''
        res = openbrowser.is_text_in_element(AirTrafficControlMicroVisionClassifyPage.assert_atcmvcinfor_page_text,
                                             "空管智慧党建平台")  # 空管微视类型
        return res

    def random_atcmvcinfor_classify(self, openbrowser):
        '''封装随机选择左侧树形空管微视分类'''
        res = openbrowser.random_click_node(AirTrafficControlMicroVisionClassifyPage.atcmvcinfor_classify)
        return res

    '''封装顶级栏目新增'''

    def click_atcmvcinfor_add_topcol_button(self, openbrowser):
        '''封装点击新增按钮'''
        openbrowser.click_my(AirTrafficControlMicroVisionClassifyPage.atcmvcinfor_add_topcol_button)

    def assert_atcmvcinfor_add_topcol_page_textcontent(self, openbrowser):
        '''封装判断添加页面文本是否一致'''
        res = openbrowser.is_text_in_element(
            AirTrafficControlMicroVisionClassifyPage.assert_atcmvcinfor_add_topcol_page_text, "栏目编辑")
        return res

    def atcmvcinfor_add_topcol_name_input(self, openbrowser, input_text):
        '''封装输入顶级栏目名'''
        openbrowser.send_key_my(AirTrafficControlMicroVisionClassifyPage.atcmvcinfor_add_topcol_name, input_text)

    def drag_atcmvcinfor_add_topcol_page_text(self, openbrowser):
        '''拖动空管微视界面上方的标题栏'''
        openbrowser.mouse_drag_drop(AirTrafficControlMicroVisionClassifyPage.assert_atcmvcinfor_add_topcol_page_text,
                                    AirTrafficControlMicroVisionClassifyPage.atcmvcinfor_add_topcol_page_close_button)

    # def click_atcmvcinfor_add_topcol_page_text(self, openbrowser):
    #     '''点击空管微视界面上方的标题栏'''
    #     openbrowser.click_my(AirTrafficControlMicroVisionClassifyPage.atcmvcinfor_add_topcol_page_text)

    def atcmvcinfor_add_topcol_submit_button_click(self, openbrowser):
        '''封装提交按钮点击'''
        openbrowser.click_my(AirTrafficControlMicroVisionClassifyPage.atcmvcinfor_add_topcol_submit_button)

    def atcmvcinfor_add_topcol_cancel_button_click(self, openbrowser):
        '''封装取消按钮点击'''
        openbrowser.click_my(AirTrafficControlMicroVisionClassifyPage.atcmvcinfor_add_topcol_cancel_button)

    def atcmvcinfor_topcol_add(self, openbrowser, topcol_name):
        '''封装空管微视顶栏目添加'''
        openbrowser.driver.switch_to.frame(0)  # 进入第二层新增iframe
        self.atcmvcinfor_add_topcol_name_input(openbrowser, topcol_name)  # 输入主栏目名称
        openbrowser.driver.switch_to.parent_frame()
        self.drag_atcmvcinfor_add_topcol_page_text(openbrowser)  # 拖动界面上方框，显示出提交按钮
        openbrowser.driver.switch_to.frame(0)
        self.atcmvcinfor_add_topcol_submit_button_click(openbrowser)  # 点击提交按钮

    def assert_atcmvcinfor_topcol_add_message_textcontent(self, openbrowser):
        '''封装判断添加成功'''
        openbrowser.driver.switch_to.parent_frame()
        res = openbrowser.is_text_in_element(
            AirTrafficControlMicroVisionClassifyPage.assert_atcmvcinfor_add_topcol_message_text, "保存成功")
        return res

    '''封装顶级栏目修改'''

    def click_atcmvcinfor_update_topcol_button(self, openbrowser, topcol_name):
        '''封装点击编辑按钮'''
        openbrowser.table_button_click(AirTrafficControlMicroVisionClassifyPage.atcmvcinfor_table_all,
                                       AirTrafficControlMicroVisionClassifyPage.atcmvcinfor_table_topcal_name,
                                       AirTrafficControlMicroVisionClassifyPage.atcmvcinfor_update_table_topcol_button,
                                       topcol_name)

    def get_update_atcmvcinfor_topcol_name(self, openbrowser):
        '''获取修改页面顶级栏目名称'''
        my_text = openbrowser.get_vlaue(AirTrafficControlMicroVisionClassifyPage.atcmvcinfor_update_topcal_name)
        return my_text

    def assert_atcmvcinfor_update_textcontent(self, openbrowser, topcol_name):
        '''封装编辑内容检查'''
        openbrowser.driver.switch_to.frame(0)  # 进入第二层修改iframe
        page_topcol_name = self.get_update_atcmvcinfor_topcol_name(openbrowser)

        message = "编辑回显内容："
        flag = True
        if page_topcol_name == topcol_name:
            message += "栏目名称{0}与新增的数据{1}一致".format(page_topcol_name, topcol_name)
        else:
            message += "栏目名称{0}与新增的数据{1}不一致".format(page_topcol_name, topcol_name)
            flag = False
        return flag, message

    def assert_page_atcmvcinfor_update_textcontent(self, openbrowser):
        '''封装判断修改页面文本是否一致'''
        res = openbrowser.is_text_in_element(AirTrafficControlMicroVisionClassifyPage.assert_page_atcmvcinfor_update_text, "栏目编辑")
        return res

    def drag_atcmvcinfor_update_topcol_page_text(self, openbrowser):
        '''拖动空管微视界面上方的标题栏'''
        openbrowser.mouse_drag_drop(AirTrafficControlMicroVisionClassifyPage.assert_atcmvcinfor_updage_topcol_page_text,
                                    AirTrafficControlMicroVisionClassifyPage.atcmvcinfor_update_topcol_page_close_button)

    def atcmvcinfor_update_topcol_submit_button_click(self,openbrowser):
        '''封装修改提交按钮点击'''
        openbrowser.click_my(AirTrafficControlMicroVisionClassifyPage.atcmvcinfor_update_submit_button)

    def atcmvcinfor_topcol_update(self, openbrowser):
        '''封装修改提交按钮点击'''
        openbrowser.driver.switch_to.parent_frame()
        self.drag_atcmvcinfor_update_topcol_page_text(openbrowser)  # 拖动界面上方框，显示出提交按钮
        openbrowser.driver.switch_to.frame(0)
        self.atcmvcinfor_update_topcol_submit_button_click(openbrowser)  # 点击提交按钮

    def assert_update_message_textcontent(self, openbrowser):
        '''封装判断修改成功'''
        openbrowser.driver.switch_to.parent_frame()
        res = openbrowser.is_text_in_element(AirTrafficControlMicroVisionClassifyPage.assert_atcmvcinfor_update_message_text, "保存成功")
        return res

    '''封装顶级栏目停用'''

    def atcmvcinfor_block_up_table_topcol_button_click(self, openbrowser, topcol_name):
        '''封装点击停用'''
        openbrowser.table_button_click(AirTrafficControlMicroVisionClassifyPage.atcmvcinfor_table_all,
                                       AirTrafficControlMicroVisionClassifyPage.atcmvcinfor_table_topcal_name,
                                       AirTrafficControlMicroVisionClassifyPage.atcmvcinfor_block_up_table_topcol_button,
                                       topcol_name)

    def assert_atcmvcinfor_block_up_topcol_alert_textcontent(self, openbrowser):
        '''封装判断页面文本是否一致,来判断弹出停用对话框'''
        res = openbrowser.is_text_in_element(AirTrafficControlMicroVisionClassifyPage.assert_atcmvcinfor_block_up_topcol_alert_text, "确定停用此栏目吗？")
        return res

    def atcmvcinfor_block_up_topcol_alert_submit_button_click(self, openbrowser):
        '''封装点击确定'''
        openbrowser.click_my(AirTrafficControlMicroVisionClassifyPage.atcmvcinfor_block_up_topcol_alert_submit_button)  # 点击确定按钮

    def assert_atcmvcinfor_block_up_topcol_message_textcontent(self, openbrowser):
        '''封装判断页面文本是否一致,来判断停用成功'''
        res = openbrowser.is_text_in_element(AirTrafficControlMicroVisionClassifyPage.assert_atcmvcinfor_block_up_topcol_message_text, "停用成功")
        return res

    '''封装顶级栏目启用'''

    def atcmvcinfor_start_using_table_topcol_button_click(self, openbrowser, topcol_name):
        '''封装点击启用'''
        openbrowser.table_button_click(AirTrafficControlMicroVisionClassifyPage.atcmvcinfor_table_all,
                                       AirTrafficControlMicroVisionClassifyPage.atcmvcinfor_table_topcal_name,
                                       AirTrafficControlMicroVisionClassifyPage.atcmvcinfor_start_using_table_topcol_button,
                                       topcol_name)

    def assert_atcmvcinfor_start_using_topcol_alert_textcontent(self, openbrowser):
        '''封装判断页面文本是否一致,来判断是否弹出启用对话框'''
        res = openbrowser.is_text_in_element(AirTrafficControlMicroVisionClassifyPage.assert_atcmvcinfor_start_using_topcol_alert_text, "确定启用此栏目吗？")
        return res

    def atcmvcinfor_start_using_topcol_alert_submit_button_click(self, openbrowser):
        '''封装点击确定按钮'''
        openbrowser.click_my(AirTrafficControlMicroVisionClassifyPage.atcmvcinfor_start_using_topcol_alert_submit_button)  # 点击确定按钮

    def assert_atcmvcinfor_start_using_topcol_message_textcontent(self, openbrowser):
        '''封装判断页面文本是否一致,来判断启用成功'''
        res = openbrowser.is_text_in_element(AirTrafficControlMicroVisionClassifyPage.assert_atcmvcinfor_start_using_topcol_message_text, "启用成功")
        return res

    '''封装子栏目新增'''

    def click_atcmvcinfor_add_soncol_button(self, openbrowser,topcol_name):
        '''封装点击子栏目新增按钮'''
        openbrowser.table_button_click(AirTrafficControlMicroVisionClassifyPage.atcmvcinfor_table_all,
                                       AirTrafficControlMicroVisionClassifyPage.atcmvcinfor_table_topcal_name,
                                       AirTrafficControlMicroVisionClassifyPage.atcmvcinfor_add_table_soncol_button,
                                       topcol_name)

    def assert_atcmvcinfor_add_soncol_page_textcontent(self, openbrowser):
        '''封装判断添加页面文本是否一致'''
        res = openbrowser.is_text_in_element(
            AirTrafficControlMicroVisionClassifyPage.assert_atcmvcinfor_add_soncol_page_text, "栏目编辑")
        return res

    def atcmvcinfor_add_soncol_name_input(self, openbrowser, input_text):
        '''封装输入顶级栏目名'''
        openbrowser.send_key_my(AirTrafficControlMicroVisionClassifyPage.atcmvcinfor_add_soncol_name, input_text)

    def drag_atcmvcinfor_add_soncol_page_text(self, openbrowser):
        '''拖动空管微视界面上方的标题栏'''
        openbrowser.mouse_drag_drop(AirTrafficControlMicroVisionClassifyPage.assert_atcmvcinfor_add_soncol_page_text,
                                    AirTrafficControlMicroVisionClassifyPage.atcmvcinfor_add_soncol_page_close_button)

    # def click_atcmvcinfor_add_topcol_page_text(self, openbrowser):
    #     '''点击空管微视界面上方的标题栏'''
    #     openbrowser.click_my(AirTrafficControlMicroVisionClassifyPage.atcmvcinfor_add_topcol_page_text)

    def atcmvcinfor_add_soncol_submit_button_click(self, openbrowser):
        '''封装提交按钮点击'''
        openbrowser.click_my(AirTrafficControlMicroVisionClassifyPage.atcmvcinfor_add_soncol_submit_button)

    def atcmvcinfor_add_soncol_cancel_button_click(self, openbrowser):
        '''封装取消按钮点击'''
        openbrowser.click_my(AirTrafficControlMicroVisionClassifyPage.atcmvcinfor_add_soncol_cancel_button)

    def atcmvcinfor_soncol_add(self, openbrowser, topcol_name):
        '''封装空管微视顶栏目添加'''
        openbrowser.driver.switch_to.frame(0)  # 进入第二层新增iframe
        self.atcmvcinfor_add_soncol_name_input(openbrowser, topcol_name)  # 输入主栏目名称
        openbrowser.driver.switch_to.parent_frame()
        self.drag_atcmvcinfor_add_soncol_page_text(openbrowser)  # 拖动界面上方框，显示出提交按钮
        openbrowser.driver.switch_to.frame(0)
        self.atcmvcinfor_add_soncol_submit_button_click(openbrowser)  # 点击提交按钮

    def assert_atcmvcinfor_soncol_add_message_textcontent(self, openbrowser):
        '''封装判断添加成功'''
        openbrowser.driver.switch_to.parent_frame()
        res = openbrowser.is_text_in_element(
            AirTrafficControlMicroVisionClassifyPage.assert_atcmvcinfor_add_soncol_message_text, "保存成功")
        return res

    '''栏目删除'''

    def atcmvcinfor_delete_button_click(self, openbrowser,col_name):
        '''封装点击删除按钮'''
        openbrowser.table_button_click(AirTrafficControlMicroVisionClassifyPage.atcmvcinfor_table_all,
                                       AirTrafficControlMicroVisionClassifyPage.atcmvcinfor_table_topcal_name,
                                       AirTrafficControlMicroVisionClassifyPage.atcmvcinfor_delete_button,
                                       col_name)

    def assert_atcmvcinfor_delete_alert_textcontent(self, openbrowser):
        '''封装判断页面文本是否一致,来判断是否弹出删除对话框'''
        res = openbrowser.is_text_in_element(AirTrafficControlMicroVisionClassifyPage.assert_atcmvcinfor_delete_alert_text, "确定删除此栏目吗？")
        return res

    def atcmvcinfor_delete_alert_submit_button_click(self, openbrowser):
        '''封装点击确定'''
        openbrowser.click_my(AirTrafficControlMicroVisionClassifyPage.atcmvcinfor_delete_alert_submit_button)  # 点击确定按钮

    def assert_delete_message_textcontent(self, openbrowser):
        '''封装判断页面文本是否一致,来判断是否删除成功'''
        res = openbrowser.is_text_in_element(AirTrafficControlMicroVisionClassifyPage.assert_delete_message_text, "删除成功")
        return res