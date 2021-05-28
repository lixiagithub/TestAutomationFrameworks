# coding = utf-8
# Author:李昰 
# Date：2021/5/14 13:27
from selenium.webdriver.common.by import By

class AirTrafficControlPressPage():
    atcpinfor_tab_close_button = (By.XPATH, '/html/body/div[2]/div/div[2]/nav/div/a[2]/i')  # 空管报刊页面关闭
    atcpinfor_iframe = (By.XPATH, '//*[@id="content-main"]/iframe[2]')  # 空管报刊页面iframe
    assert_page_text = (By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div/div[1]/div/span[1]')  # 空管报刊列表名
    assert_table_number = (By.XPATH, '//*[@id="table"]/div[1]/div[2]/div[4]/div[1]/span[1]')  # 总共多少

    '''报刊新增'''
    atcpinfor_add_button = (By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div/div[2]/div[1]/div[2]/a")  # 新增按钮
    assert_page_add_text = (By.XPATH, '/html/body/div[1]/div/div/div[3]/div[1]/div/span[1]')  # 空管报刊新增文本title校验
    atcpinfor_add_name = (By.XPATH, '//*[@id="forms"]/div/div/div[1]/div/div/div/input')  # 空管报刊新增标题
    atcpinfor_add_press= (By.XPATH, '//*[@id="forms"]/div/div/div[2]/div/div/div/input')  # 空管报刊新增出版社
    atcpinfor_add_brief = (By.XPATH, '//*[@id="forms"]/div/div/div[3]/div/div/div/textarea')  # 空管报刊新增报刊简介
    atcpinfor_add_submit_button = (By.XPATH, "//*[text()='保存']")  # 空管报刊新增提交按钮
    atcpinfor_add_cancel_button = (By.XPATH, "//*[text()='取消']")  # 空管报刊新增取消按钮

    '''查询'''
    atcpinfor_query_name = (By.XPATH, '//*[@id="keyword"]')  # 空管报刊查询名称
    atcpinfor_query_button = (By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div/div[2]/div[1]/div[2]/button")  # 空管报刊查询按钮
    atcpinfor_query_empty = (By.XPATH, '//*[@id="client_table"]/tbody/tr/td')  # 空管报刊查询为空

    '''修改'''
    atcpinfor_update_button = (By.XPATH, "//*[text()=' 编辑']")  # 点击第一个编辑按钮
    atcpinfor_update_name = (By.XPATH, '//*[@id="forms"]/div/div/div[1]/div/div/div/input')  # 编辑页面名称-回显
    atcpinfor_update_press = (By.XPATH, '//*[@id="forms"]/div/div/div[2]/div/div/div/input')  # 编辑页面出版社-回显
    atcpinfor_update_brief = (By.XPATH, '//*[@id="forms"]/div/div/div[3]/div/div/div/textarea')  # 编辑页面简介-回显
    assert_page_update_text = (By.XPATH, '/html/body/div[1]/div/div/div[3]/div[1]/div/span[1]')  # 空管报刊修改文本title校验
    atcpinfor_update_submit_button = (By.XPATH, "//*[text()='保存']")  # 空管报刊修改提交按钮
    atcpinfor_update_cancel_button = (By.XPATH, "//*[text()='取消']")  # 空管报刊修改取消按钮
    assert_update_message_text = (By.CLASS_NAME, 'layui-layer-content')  # 空管报刊修改是否成功文本

    '''期数-管理'''
    atcpinfor_manage_number_button = (By.XPATH, "//*[text()=' 管理']")  # 点击管理按钮
    assert_number_page_text = (By.XPATH, '/html/body/div[1]/div/div/div[3]/div[1]/div[1]/span')  # 空管报刊名
    assert_number_table_number = (By.XPATH, '/html/body/div[1]/div/div/div[3]/div[2]/div[2]/div[2]/div[4]/div[1]/span[1]')  # 总共多少期
    atcpinfor_navigation_number_button = (By.XPATH, "//*[text()='报刊往期列表']")  # 导航点击报刊往期列表

    '''期数-新增'''
    atcpinfor_number_add_button = (By.XPATH, "/html/body/div[1]/div/div/div[3]/div[2]/div[1]/div/div/div[2]/a")  # 添加期刊按钮
    assert_page_add_number_text = (By.XPATH, '/html/body/div[1]/div/div/div[3]/div[1]/div/span[1]')  # 空管报刊新增期刊title校验
    atcpinfor_add_number_issue = (By.XPATH, '//*[@id="period_name"]')  # 空管报刊新增期刊数
    atcpinfor_add_number_choosefile_button = (By.XPATH, '//*[@id="forms"]/div/div[7]/div/div/div/a[1]')  # 空管报刊期数新增缩略图点击选择文件按钮
    atcpinfor_add_number_default_diagram_button = (By.XPATH, "//*[text()='在图库选择默认图']")  # 空管报刊期数缩略图在图库选择默认图
    show_photo_album_select = (By.XPATH, '//*[@id="forms"]/div/div/div[1]/div/div/div/span')  # 相册下拉
    select_photo_album_ul = (By.XPATH, '//*[@id="select2-gallery-results"]')  # 相册ul
    select_photo_album_li = (By.CLASS_NAME, 'select2-results__option')  # 相册li
    select_photos = (By.CLASS_NAME, 'cbp-item')  # 选择全部photo
    select_photo_buttons = (By.CLASS_NAME, 'cbp-l-caption-buttonLeft btn red uppercase btn red uppercase')  # 选择photo的所有选择按钮
    atcpinfor_add_number_submit_button = (By.XPATH, '/html/body/div[1]/div/div/div[3]/div[2]/form/div/div/div[4]/button')  # 空管报刊新增提交按钮
    atcpinfor_add_number_cancel_button = (By.XPATH, '//*[@id="forms"]/div/div/div[4]/a')  # 空管报刊新增取消按钮

    '''期数-查询'''
    atcpinfor_number_query_name = (By.XPATH, '//*[@id="keyword"]')  # 空管报刊期数查询
    atcpinfor_number_query_button = (
    By.XPATH, "/html/body/div[1]/div/div/div[3]/div[2]/div[1]/div/div/div[2]/button")  # 空管报刊查询按钮
    atcpinfor_number_query_empty = (By.XPATH, '//*[@id="client_table"]/tbody/tr/td')  # 空管报刊查询为空

    '''期数-修改'''
    atcpinfor_number_update_button = (By.XPATH, "//*[text()=' 编辑']")  # 点击第一个编辑按钮
    atcpinfor_update_number_issue = (By.XPATH, '//*[@id="period_name"]')  # 编辑页面期数-回显
    assert_page_number_update_text = (By.XPATH, '/html/body/div[1]/div/div/div[3]/div[1]/div/span[1]')  # 空管报刊修改文本title校验
    atcpinfor_number_update_submit_button = (By.XPATH, "//*[text()='保存']")  # 空管报刊修改提交按钮
    atcpinfor_number_update_cancel_button = (By.XPATH, "//*[text()='取消']")  # 空管报刊修改取消按钮
    assert_number_update_message_text = (By.CLASS_NAME, 'layui-layer-content')  # 空管报刊修改是否成功文本

    '''期刊详情-管理'''
    atcpinfor_manage_journal_button = (By.XPATH, "//*[text()=' 管理']")  # 点击期刊管理按钮
    assert_journal_page_text = (By.XPATH, '/html/body/div[1]/div/div/div[3]/div[1]/div[1]/span[1]')  # 期刊详情页
    atcpinfor_journal_layout_tab = (By.XPATH, '//*[@id="myTab"]/li[1]')  # 版面
    atcpinfor_journal_contents_tab = (By.XPATH, '//*[@id="myTab"]/li[2]')  # 目录
    atcpinfor_navigation_journal_button = (By.XPATH, "//*[text()='期刊详情']")  # 导航点击报刊往期列表

    '''版面-新增'''
    atcpinfor_journal_layout_add_button = (By.XPATH, "/html/body/div[1]/div/div/div[3]/div[2]/div[1]/div/div/div/a[1]")  # 添加版面按钮
    assert_page_add_journal_layout_text = (By.XPATH, '/html/body/div[1]/div/div/div[3]/div[1]/div/span[1]')  # 空管报刊添加版面title校验
    atcpinfor_add_journal_layout_number = (By.XPATH, '//*[@id="page_num"]')  # 版面编号
    atcpinfor_add_journal_layout_select_file = (By.XPATH,  "//*[text()='点击选择文件']")  # 选择文件按钮
    atcpinfor_add_journal_layout_select_file_iframe = (By.XPATH, '// *[ @ id = "layui-layer-iframe1"]')#选择文件iframe
    atcpinfor_add_journal_layout_select_file2 = (By.XPATH,  "//*[text()='点击选择文件']")  # 在弹出框中选择文件按钮
    assert_add_journal_layout_select_file_iframe_text = (By.XPATH, '//*[@id="layui-layer1"]/div[1]')  # 版面选择文件弹出框文本校验
    atcpinfor_add_journal_layout_submit_button = (By.XPATH, '/html/body/div[1]/div/div/div[3]/div[2]/form/div/div/div[5]/button')  # 版面新增提交按钮
    atcpinfor_add_journal_layout_cancel_button = (By.XPATH, '/html/body/div[1]/div/div/div[3]/div[2]/form/div/div/div[5]/a')  # 版面新增取消按钮
    assert_journal_layout_add_message_text = (By.CLASS_NAME, 'layui-layer-content')  # 版面修改是否成功文本

    '''版面-修改'''
    atcpinfor_journal_layout_update_button = (By.XPATH, '/html/body/div[1]/div/div/div[3]/div[2]/div[2]/div/div[1]/div/div/div/div/div/table/tbody/tr[2]/td[3]/a[1]')  # 点击第一个编辑按钮
    atcpinfor_update_journal_layout_number = (By.XPATH, '//*[@id="page_num"]')  # 编辑页面版面编号-回显
    assert_page_journal_layout_update_text = (By.XPATH, '/html/body/div[1]/div/div/div[3]/div[1]/div/span[1]')  # 版面修改文本title校验
    atcpinfor_journal_layout_update_submit_button = (By.XPATH, "//*[text()='保存']")  # 版面修改提交按钮
    atcpinfor_journal_layout_update_cancel_button = (By.XPATH, "//*[text()='取消']")  # 版面修改取消按钮
    assert_journal_layout_update_message_text = (By.CLASS_NAME, 'layui-layer-content')  # 版面修改是否成功文本

    '''版面-删除'''
    atcpinfor_journal_layout_delete_button = (By.XPATH, '/html/body/div[1]/div/div/div[3]/div[2]/div[2]/div/div[1]/div/div/div/div/div/table/tbody/tr[2]/td[3]/a[2]')  #版面删除按钮
    assert_atcpinfor_journal_layout_delete_alert_text = (By.CLASS_NAME, 'layui-layer-content')  # 版面删除提示框文本校验
    atcpinfor_journal_layout_delete_alert_submit_button = (By.CLASS_NAME, 'layui-layer-btn0')  # 版面删除确定按钮
    atcpinfor_journal_layout_delete_alert_cancel_button = (By.CLASS_NAME, 'layui-layer-btn1')  # 版面删除取消按钮
    assert_atcpinfor_journal_layout_delete_message_text = (By.CLASS_NAME, 'layui-layer-content')  # 版面删除是否成功文本

    '''目录-新增'''
    atcpinfor_journal_contents_add_button = (
    By.XPATH, "/html/body/div[1]/div/div/div[3]/div[2]/div[1]/div/div/div/a[2]")  # 添加版面按钮
    assert_page_add_journal_contents_text = (
    By.XPATH, '/html/body/div[1]/div/div/div[3]/div[1]/div/span[1]')  # 空管报刊添加版面title校验
    atcpinfor_add_journal_contents_layout = (By.XPATH, '//*[@id="forms"]/div/div/div[3]/div/div/div/span/span[1]/span')  # 目录版面下拉
    atcpinfor_add_journal_contents_layout_li = (By.CLASS_NAME, 'select2-results__option')  # 第一个下拉选项
    atcpinfor_add_journal_contents_title = (By.XPATH, '//*[@id="catalog_title"]')  # 目录标题
    atcpinfor_add_journal_contents_author = (By.XPATH, '//*[@id="author"]')  # 目录作者
    atcpinfor_add_journal_contents_editor = (By.XPATH, '//*[@id="editor"]')  # 目录内容
    atcpinfor_add_journal_contents_select_file = (By.XPATH, "//*[text()='点击选择文件']")  # 选择文件按钮
    atcpinfor_add_journal_contents_select_file_iframe = (By.XPATH, '// *[ @ id = "layui-layer-iframe1"]')  # 选择文件iframe
    atcpinfor_add_journal_contents_select_file2 = (By.XPATH, "//*[text()='点击选择文件']")  # 在弹出框中选择文件按钮
    assert_add_journal_contents_select_file_iframe_text = (By.XPATH, '//*[@id="layui-layer1"]/div[1]')  # 目录选择文件弹出框文本校验
    atcpinfor_add_journal_contents_submit_button = (
    By.XPATH, '/html/body/div[1]/div/div/div[3]/div[2]/form/div/div/div[5]/button')  # 目录新增提交按钮
    atcpinfor_add_journal_contents_cancel_button = (
    By.XPATH, '/html/body/div[1]/div/div/div[3]/div[2]/form/div/div/div[5]/a')  # 目录新增取消按钮
    assert_journal_contents_add_message_text = (By.CLASS_NAME, 'layui-layer-content')  # 目录修改是否成功文本

    '''目录-修改'''
    atcpinfor_journal_contents_update_button = (By.XPATH,
                                              '/html/body/div[1]/div/div/div[3]/div[2]/div[2]/div/div[1]/div/div/div/div/div/table/tbody/tr[2]/td[3]/a[1]')  # 点击第一个编辑按钮
    atcpinfor_update_journal_contents_layout = (By.XPATH, '//*[@id="select2-status-container"]')  # 编辑页面目录版面编号-回显
    atcpinfor_update_journal_contents_title = (By.XPATH, '//*[@id="catalog_title"]')  # 编辑页面目录标题-回显
    atcpinfor_update_journal_contents_author = (By.XPATH, '//*[@id="author"]')  # 编辑页面目录作者-回显
    atcpinfor_update_journal_contents_editor = (By.XPATH, '//*[@id="editor"]')  # 编辑页面目录内容-回显
    assert_page_journal_contents_update_text = (By.XPATH, '/html/body/div[1]/div/div/div[3]/div[1]/div/span[1]')  # 目录修改文本title校验
    atcpinfor_journal_contents_update_submit_button = (By.XPATH, "//*[text()='保存']")  # 目录修改提交按钮
    atcpinfor_journal_contents_update_cancel_button = (By.XPATH, "//*[text()='取消']")  # 目录修改取消按钮
    assert_journal_contents_update_message_text = (By.CLASS_NAME, 'layui-layer-content')  # 目录修改是否成功文本

    '''目录-删除'''
    atcpinfor_journal_contents_delete_button = (By.XPATH,
                                              '/html/body/div[1]/div/div/div[3]/div[2]/div[2]/div/div[1]/div/div/div/div/div/table/tbody/tr[2]/td[3]/a[2]')  # 目录删除按钮
    assert_atcpinfor_journal_contents_delete_alert_text = (By.CLASS_NAME, 'layui-layer-content')  # 目录删除提示框文本校验
    atcpinfor_journal_contents_delete_alert_submit_button = (By.CLASS_NAME, 'layui-layer-btn0')  # 目录删除确定按钮
    atcpinfor_journal_contents_delete_alert_cancel_button = (By.CLASS_NAME, 'layui-layer-btn1')  # 目录删除取消按钮
    assert_atcpinfor_journal_contents_delete_message_text = (By.CLASS_NAME, 'layui-layer-content')  # 目录删除是否成功文本

    def click_atcpinfor_tab_close_button(self, openbrowser):
        '''封装点击关闭按钮'''
        openbrowser.click_my(AirTrafficControlPressPage.atcpinfor_tab_close_button)

    def into_atcpinfor_iframe(self, openbrowser):
        '''封装进入iframe'''
        openbrowser.is_iframe(AirTrafficControlPressPage.atcpinfor_iframe)

    def assert_page_textcontent(self, openbrowser):
        '''封装判断页面文本是否一致,来判断是否进入空管报刊页面'''
        res = openbrowser.is_text_in_element(AirTrafficControlPressPage.assert_page_text, "空管报刊")
        return res

    def assert_table_number_text(self, openbrowser):
        '''获取空管报刊总数'''
        table_number = openbrowser.get_table_total_number(AirTrafficControlPressPage.assert_table_number)
        return table_number

    '''封装新增'''

    def click_atcpinfor_add_button(self, openbrowser):
        '''封装点击新增按钮'''
        openbrowser.click_my(AirTrafficControlPressPage.atcpinfor_add_button)

    def assert_page_add_textcontent(self, openbrowser):
        '''封装判断添加页面文本是否一致'''
        res = openbrowser.is_text_in_element(AirTrafficControlPressPage.assert_page_add_text, "报刊编辑")#报刊新增
        return res

    def atcpinfor_add_name_input(self, openbrowser, input_text):
        '''封装输入报刊名称'''
        openbrowser.send_key_my(AirTrafficControlPressPage.atcpinfor_add_name, input_text)

    def atcpinfor_add_press_input(self, openbrowser, input_text):
        '''封装输入报刊出版社'''
        openbrowser.send_key_my(AirTrafficControlPressPage.atcpinfor_add_press, input_text)

    def atcpinfor_add_brief_input(self, openbrowser, input_text):
        '''封装输入报刊简介'''
        openbrowser.send_key_my(AirTrafficControlPressPage.atcpinfor_add_brief, input_text)


    def atcpinfor_add_submit_button_click(self, openbrowser):
        '''封装提交按钮点击'''
        openbrowser.click_my(AirTrafficControlPressPage.atcpinfor_add_submit_button)

    def atcpinfor_add_cancel_button_click(self, openbrowser):
        '''封装取消按钮点击'''
        openbrowser.click_my(AirTrafficControlPressPage.atcpinfor_add_cancel_button)

    def atcpinfor_add(self, openbrowser, name, press,brief):
        '''封装空管报刊增加'''
        self.atcpinfor_add_name_input(openbrowser, name)  # 输入报刊名称
        self.atcpinfor_add_press_input(openbrowser, press)  # 输入报刊出版社
        self.atcpinfor_add_brief_input(openbrowser,brief)  # 输入报刊简介
        self.atcpinfor_add_submit_button_click(openbrowser)  # 点击提交按钮

    '''封装查询'''

    def atcpinfor_query_button_click(self, openbrowser):
        '''封装查询按钮点击'''
        openbrowser.click_my(AirTrafficControlPressPage.atcpinfor_query_button)

    def atcpinfor_query_name_input(self, openbrowser, input_text):
        '''封装查询名称'''
        openbrowser.send_key_my(AirTrafficControlPressPage.atcpinfor_query_name, input_text)

    def atcpinfor_query(self, openbrowser, name):
        '''封装查询'''
        self.atcpinfor_query_name_input(openbrowser, name)  # 输入关键字
        self.atcpinfor_query_button_click(openbrowser)  # 点击查询按钮

    '''封装修改'''

    def atcpinfor_update_button_click(self, openbrowser):
        '''封装编辑按钮点击'''
        openbrowser.click_my(AirTrafficControlPressPage.atcpinfor_update_button)

    def get_update_atcpinfor_name(self, openbrowser):
        '''获取修改页面的标题'''
        my_text = openbrowser.get_vlaue(AirTrafficControlPressPage.atcpinfor_update_name)
        return my_text

    def get_update_atcpinfor_press(self, openbrowser):
        '''获取修改页面的内容'''
        my_text = openbrowser.get_vlaue(AirTrafficControlPressPage.atcpinfor_update_press)
        return my_text

    def get_update_atcpinfor_brief(self, openbrowser):
        '''获取修改页面的对应组织'''
        my_text = openbrowser.get_vlaue(AirTrafficControlPressPage.atcpinfor_update_brief)
        return my_text

    def assert_update_textcontent(self, openbrowser, atcp_name, atcp_press,atcp_brief):
        '''封装编辑内容检查'''
        page_atcp_name = self.get_update_atcpinfor_name(openbrowser)
        page_atcp_press = self.get_update_atcpinfor_press(openbrowser)
        page_atcp_brief = self.get_update_atcpinfor_brief(openbrowser)
        message = "编辑回显内容："
        flag = True
        if page_atcp_name == atcp_name:
            message += "页面空管报刊名称{0}与新增的数据{1}一致".format(page_atcp_name, atcp_name)
        else:
            message += "页面空管报刊名称{0}与新增的数据{1}不一致".format(page_atcp_name, atcp_name)
            flag = False
        if page_atcp_press == atcp_press:
            message += ",页面空管报刊出版社{0}与新增的数据{1}一致".format(page_atcp_press, atcp_press)
        else:
            message += ",页面党空管报刊出版社{0}与新增的数据{1}不一致".format(page_atcp_press, atcp_press)
            flag = False

        if page_atcp_brief == atcp_brief:
            message += ",页面空管报刊简介{0}与新增的数据{1}一致".format(page_atcp_brief, atcp_brief)
        else:
            message += ",页面空管报刊简介{0}与新增的数据{1}不一致".format(page_atcp_brief, atcp_brief)
            flag = False
        return flag, message

    def assert_page_update_textcontent(self, openbrowser):
        '''封装判断修改页面文本是否一致'''
        res = openbrowser.is_text_in_element(AirTrafficControlPressPage.assert_page_update_text, "报刊编辑")
        return res

    def atcpinfor_update_submit_button_click(self, openbrowser):
        '''封装修改提交按钮点击'''
        openbrowser.click_my(AirTrafficControlPressPage.atcpinfor_update_submit_button)

    def assert_update_message_textcontent(self, openbrowser):
        '''封装判断修改成功'''
        res = openbrowser.is_text_in_element(AirTrafficControlPressPage.assert_update_message_text, "编辑成功")
        return res

    '''期数-管理'''

    def atcpinfor_manage_number_button_click(self, openbrowser):
        '''封装管理按钮点击'''
        openbrowser.click_my(AirTrafficControlPressPage.atcpinfor_manage_number_button)

    def assert_number_page_textcontent(self, openbrowser,atcp_name):
        '''封装判断页面文本是否一致,来判断是否进入空管报刊期数页面'''
        res = openbrowser.is_text_in_element(AirTrafficControlPressPage.assert_number_page_text, atcp_name)
        return res

    def assert_number_table_number_text(self, openbrowser):
        '''获取空管报刊期数总数'''
        table_number = openbrowser.get_table_total_number(AirTrafficControlPressPage.assert_number_table_number)
        return table_number

    def atcpinfor_navigation_number_button_click(self, openbrowser):
        '''封装导航点击报刊往期列表'''
        openbrowser.click_my(AirTrafficControlPressPage.atcpinfor_navigation_number_button)

    '''期数-新增'''

    def click_atcpinfor_add_number_button(self, openbrowser):
        '''封装点击新增期刊按钮'''
        openbrowser.click_my(AirTrafficControlPressPage.atcpinfor_number_add_button)

    def assert_page_add_number_textcontent(self, openbrowser):
        '''封装判断添加期刊页面文本是否一致'''
        res = openbrowser.is_text_in_element(AirTrafficControlPressPage.assert_page_add_number_text, "期刊编辑")#期刊新增
        return res

    def atcpinfor_add_number_issue_input(self, openbrowser, input_text):
        '''封装输入报刊名称'''
        openbrowser.send_key_my(AirTrafficControlPressPage.atcpinfor_add_number_issue, input_text)

    def atcpinfor_add_number_default_diagram_select(self, openbrowser):
        '''封装选择图库图片'''
        openbrowser.click_my(AirTrafficControlPressPage.atcpinfor_add_number_default_diagram_button)  # 点击在图库选择默认图按钮
        openbrowser.driver.switch_to.frame(0)  # 进入第三层图片iframe
        openbrowser.click_my(AirTrafficControlPressPage.show_photo_album_select)  # 显示相册下拉列表
        openbrowser.random_select_ul(AirTrafficControlPressPage.select_photo_album_li)  # 随机选择相册下拉li
        openbrowser.random_select_pic(AirTrafficControlPressPage.select_photos)  # 随机选择一个photo

    def atcpinfor_add_number_submit_button_click(self, openbrowser):
        '''封装提交按钮点击'''
        openbrowser.click_my(AirTrafficControlPressPage.atcpinfor_add_number_submit_button)

    def atcpinfor_add_number_cancel_button_click(self, openbrowser):
        '''封装取消按钮点击'''
        openbrowser.click_my(AirTrafficControlPressPage.atcpinfor_add_number_cancel_button)

    def atcpinfor_number_add(self, openbrowser,atcp_number):
        '''封装空管报刊期数增加'''
        self.atcpinfor_add_number_issue_input(openbrowser, atcp_number)  # 输入期数
        self.atcpinfor_add_number_default_diagram_select(openbrowser) #选择图片
        openbrowser.driver.switch_to.parent_frame()  # 切换到第二层新增iframe
        self.atcpinfor_add_number_submit_button_click(openbrowser)  # 点击提交按钮

    '''期数-查询'''

    def atcpinfor_number_query_button_click(self, openbrowser):
        '''封装查询按钮点击'''
        openbrowser.click_my(AirTrafficControlPressPage.atcpinfor_number_query_button)

    def atcpinfor_number_query_name_input(self, openbrowser, input_text):
        '''封装查询名称'''
        openbrowser.send_key_my(AirTrafficControlPressPage.atcpinfor_number_query_name, input_text)

    def atcpinfor_number_query(self, openbrowser, name):
        '''封装查询'''
        self.atcpinfor_number_query_name_input(openbrowser, name)  # 输入关键字
        self.atcpinfor_number_query_button_click(openbrowser)  # 点击查询按钮

    '''期数-修改'''

    def atcpinfor_number_update_button_click(self, openbrowser):
        '''封装期数编辑按钮点击'''
        openbrowser.click_my(AirTrafficControlPressPage.atcpinfor_number_update_button)

    def get_atcpinfor_update_number_issue(self, openbrowser):
        '''获取修改页面的期数'''
        my_text = openbrowser.get_vlaue(AirTrafficControlPressPage.atcpinfor_update_number_issue)
        return my_text

    def assert_number_update_textcontent(self, openbrowser, atcp_number):
        '''封装编辑内容检查'''
        page_atcp_number = self.get_atcpinfor_update_number_issue(openbrowser)
        message = "编辑回显内容："
        flag = True
        if page_atcp_number == atcp_number:
            message += "页面空管报刊期数{0}与新增的数据{1}一致".format(page_atcp_number, atcp_number)
        else:
            message += "页面空管报刊期数{0}与新增的数据{1}不一致".format(page_atcp_number, atcp_number)
            flag = False
        return flag, message

    def assert_number_page_update_textcontent(self, openbrowser):
        '''封装判断修改页面文本是否一致'''
        res = openbrowser.is_text_in_element(AirTrafficControlPressPage.assert_page_number_update_text, "期刊编辑")
        return res

    def atcpinfor_number_update_submit_button_click(self, openbrowser):
        '''封装修改提交按钮点击'''
        openbrowser.click_my(AirTrafficControlPressPage.atcpinfor_number_update_submit_button)

    def assert_number_update_message_textcontent(self, openbrowser):
        '''封装判断修改成功'''
        res = openbrowser.is_text_in_element(AirTrafficControlPressPage.assert_number_update_message_text, "编辑成功")
        return res

    '''期刊详情-管理'''

    def atcpinfor_manage_journal_button_click(self, openbrowser):
        '''封装管理按钮点击'''
        openbrowser.click_my(AirTrafficControlPressPage.atcpinfor_manage_journal_button)

    def assert_journal_page_textcontent(self, openbrowser):
        '''封装判断页面文本是否一致,来判断是否进入空管报刊期数页面'''
        res = openbrowser.is_text_in_element(AirTrafficControlPressPage.assert_number_page_text, "期刊详情")
        return res

    def atcpinfor_journal_layout_tab_click(self, openbrowser):
        '''封装点击版面选项卡'''
        openbrowser.click_my(AirTrafficControlPressPage.atcpinfor_journal_layout_tab)

    def atcpinfor_journal_contents_tab_click(self, openbrowser):
        '''封装点击目录选项卡'''
        openbrowser.click_my(AirTrafficControlPressPage.atcpinfor_journal_contents_tab)

    def atcpinfor_navigation_journal_button_click(self, openbrowser):
        '''封装导航点击期刊详情'''
        openbrowser.click_my(AirTrafficControlPressPage.atcpinfor_navigation_journal_button)

    '''版面-新增'''

    def click_atcpinfor_add_journal_layout_button(self, openbrowser):
        '''封装点击添加版面按钮'''
        openbrowser.click_my(AirTrafficControlPressPage.atcpinfor_journal_layout_add_button)

    def assert_page_add_journal_layout_textcontent(self, openbrowser):
        '''封装判断添加版面文本是否一致'''
        res = openbrowser.is_text_in_element(AirTrafficControlPressPage.assert_page_add_journal_layout_text, "报刊版面编辑")  # 版面新增
        return res

    def atcpinfor_add_journal_layout_number_input(self, openbrowser, input_text):
        '''封装输入报刊名称'''
        openbrowser.send_key_my(AirTrafficControlPressPage.atcpinfor_add_journal_layout_number, input_text)

    # def atcpinfor_add_journal_layout_diagram_select(self, openbrowser):
    #     '''封装选择图库图片'''
    #     openbrowser.click_my(AirTrafficControlPressPage.atcpinfor_add_journal_layout_select_file)  # 点击选择文件
    #     openbrowser.driver.switch_to.frame(0)  # 进入第三层图片iframe
    #     openbrowser.click_my(AirTrafficControlPressPage.atcpinfor_add_journal_layout_select_file2)  # 在弹出框中点击选择文件
    #     openbrowser.click_my(AirTrafficControlPressPage.show_photo_album_select)  # 显示相册下拉列表
    #     openbrowser.random_select_ul(AirTrafficControlPressPage.select_photo_album_li)  # 随机选择相册下拉li
    #     openbrowser.random_select_pic(AirTrafficControlPressPage.select_photos)  # 随机选择一个photo

    def atcpinfor_add_journal_layout_submit_button_click(self, openbrowser):
        '''封装提交按钮点击'''
        openbrowser.click_my(AirTrafficControlPressPage.atcpinfor_add_journal_layout_submit_button)

    def atcpinfor_add_journal_layout_cancel_button_click(self, openbrowser):
        '''封装取消按钮点击'''
        openbrowser.click_my(AirTrafficControlPressPage.atcpinfor_add_journal_layout_cancel_button)

    def atcpinfor_journal_layout_add(self, openbrowser, atcp_layout):
        '''封装版面增加'''
        self.atcpinfor_add_journal_layout_number_input(openbrowser, atcp_layout)  # 输入版面编号
        # self.atcpinfor_add_journal_layout_diagram_select(openbrowser)  # 选择图片
        # openbrowser.driver.switch_to.parent_frame()  # 切换到第二层新增iframe
        self.atcpinfor_add_journal_layout_submit_button_click(openbrowser)  # 点击提交按钮

    def assert_journal_layout_add_message_textcontent(self, openbrowser):
        '''封装判断修改成功'''
        res = openbrowser.is_text_in_element(AirTrafficControlPressPage.assert_journal_layout_add_message_text, "添加成功")
        return res

    '''版面-修改'''

    def atcpinfor_journal_layout_update_button_click(self, openbrowser):
        '''封装版面编辑按钮点击'''
        openbrowser.click_my(AirTrafficControlPressPage.atcpinfor_journal_layout_update_button)

    def get_atcpinfor_update_journal_layout_number(self, openbrowser):
        '''获取修改页面的版面编号'''
        my_text = openbrowser.get_vlaue(AirTrafficControlPressPage.atcpinfor_update_journal_layout_number)
        return my_text

    def assert_journal_layout_update_textcontent(self, openbrowser, atcp_layout):
        '''封装编辑内容检查'''
        page_atcp_layout = self.get_atcpinfor_update_journal_layout_number(openbrowser)
        message = "编辑回显内容："
        flag = True
        if page_atcp_layout == atcp_layout:
            message += "版面编号{0}与新增的数据{1}一致".format(page_atcp_layout, atcp_layout)
        else:
            message += "版面编号{0}与新增的数据{1}不一致".format(page_atcp_layout, atcp_layout)
            flag = False
        return flag, message

    def assert_journal_layout_page_update_textcontent(self, openbrowser):
        '''封装判断修改页面文本是否一致'''
        res = openbrowser.is_text_in_element(AirTrafficControlPressPage.assert_page_journal_layout_update_text, "报刊版面编辑")
        return res

    def atcpinfor_journal_layout_update_submit_button_click(self, openbrowser):
        '''封装修改保存按钮点击'''
        openbrowser.click_my(AirTrafficControlPressPage.atcpinfor_journal_layout_update_submit_button)

    def assert_journal_layout_update_message_textcontent(self, openbrowser):
        '''封装判断修改成功'''
        res = openbrowser.is_text_in_element(AirTrafficControlPressPage.assert_journal_layout_update_message_text, "编辑成功")
        return res

    '''版面-删除'''

    def atcpinfor_journal_layout_delete_button_click(self, openbrowser):
        '''封装点击删除按钮'''
        openbrowser.click_my(AirTrafficControlPressPage.atcpinfor_journal_layout_delete_button)  # 点击删除按钮

    def assert_atcpinfor_journal_layout_delete_alert_textcontent(self, openbrowser):
        '''封装判断页面文本是否一致,来判断是否弹出删除对话框'''
        res = openbrowser.is_text_in_element(AirTrafficControlPressPage.assert_atcpinfor_journal_layout_delete_alert_text, "确定删除吗？")
        return res

    def atcpinfor_journal_layout_delete_alert_submit_button_click(self, openbrowser):
        '''封装点击确定'''
        openbrowser.click_my(AirTrafficControlPressPage.atcpinfor_journal_layout_delete_alert_submit_button)  # 点击确定按钮

    def assert_atcpinfor_journal_layout_delete_message_textcontent(self, openbrowser):
        '''封装判断页面文本是否一致,来判断是否删除成功'''
        res = openbrowser.is_text_in_element(AirTrafficControlPressPage.assert_atcpinfor_journal_layout_delete_message_text, "删除成功")
        return res

    '''目录-新增'''

    def click_atcpinfor_add_journal_contents_button(self, openbrowser):
        '''封装点击添加目录按钮'''
        openbrowser.click_my(AirTrafficControlPressPage.atcpinfor_journal_contents_add_button)

    def assert_page_add_journal_contents_textcontent(self, openbrowser):
        '''封装判断添加目录文本是否一致'''
        res = openbrowser.is_text_in_element(AirTrafficControlPressPage.assert_page_add_journal_contents_text,
                                             "报刊版面编辑")  # 目录新增
        return res

    def atcpinfor_add_journal_contents_layout_select(self, openbrowser,atcp_layout):
        '''封装下拉选择版面'''
        openbrowser.click_my(AirTrafficControlPressPage.atcpinfor_add_journal_contents_layout)#点击下拉
        openbrowser.select_ul_content_click(AirTrafficControlPressPage.atcpinfor_add_journal_contents_layout_li,atcp_layout)#选择固定内容的下拉项

    def atcpinfor_add_journal_contents_title_input(self, openbrowser, input_text):
        '''封装输入目录标题'''
        openbrowser.send_key_my(AirTrafficControlPressPage.atcpinfor_add_journal_contents_title, input_text)

    def atcpinfor_add_journal_contents_author_input(self, openbrowser, input_text):
        '''封装输入目录作者'''
        openbrowser.send_key_my(AirTrafficControlPressPage.atcpinfor_add_journal_contents_author, input_text)

    def atcpinfor_add_journal_contents_editor_input(self, openbrowser, input_text):
        '''封装输入目录内容'''
        openbrowser.send_key_my(AirTrafficControlPressPage.atcpinfor_add_journal_contents_editor, input_text)

    # def atcpinfor_add_journal_contents_diagram_select(self, openbrowser):
    #     '''封装选择图库图片'''
    #     openbrowser.click_my(AirTrafficControlPressPage.atcpinfor_add_journal_contents_select_file)  # 点击选择文件
    #     openbrowser.driver.switch_to.frame(0)  # 进入第三层图片iframe
    #     openbrowser.click_my(AirTrafficControlPressPage.atcpinfor_add_journal_contents_select_file2)  # 在弹出框中点击选择文件
    #     openbrowser.click_my(AirTrafficControlPressPage.show_photo_album_select)  # 显示相册下拉列表
    #     openbrowser.random_select_ul(AirTrafficControlPressPage.select_photo_album_li)  # 随机选择相册下拉li
    #     openbrowser.random_select_pic(AirTrafficControlPressPage.select_photos)  # 随机选择一个photo

    def atcpinfor_add_journal_contents_submit_button_click(self, openbrowser):
        '''封装提交按钮点击'''
        openbrowser.click_my(AirTrafficControlPressPage.atcpinfor_add_journal_contents_submit_button)

    def atcpinfor_add_journal_contents_cancel_button_click(self, openbrowser):
        '''封装取消按钮点击'''
        openbrowser.click_my(AirTrafficControlPressPage.atcpinfor_add_journal_contents_cancel_button)

    def atcpinfor_journal_contents_add(self, openbrowser, atcp_layout,atcp_title,atcp_author,atcp_editor):
        '''封装目录增加'''
        self.atcpinfor_add_journal_contents_layout_select(openbrowser,atcp_layout)  # 选择版面编号
        self.atcpinfor_add_journal_contents_title_input(openbrowser,atcp_title) #目录名
        self.atcpinfor_add_journal_contents_author_input(openbrowser, atcp_author)  # 作者
        self.atcpinfor_add_journal_contents_editor_input(openbrowser, atcp_editor)  # 内容
        self.atcpinfor_add_journal_contents_submit_button_click(openbrowser)  # 点击提交按钮

    def assert_journal_contents_add_message_textcontent(self, openbrowser):
        '''封装判断添加成功'''
        res = openbrowser.is_text_in_element(AirTrafficControlPressPage.assert_journal_contents_add_message_text, "添加成功")
        return res

    '''目录-修改'''

    def atcpinfor_journal_contents_update_button_click(self, openbrowser):
        '''封装目录编辑按钮点击'''
        openbrowser.click_my(AirTrafficControlPressPage.atcpinfor_journal_contents_update_button)

    def get_atcpinfor_update_journal_contents_layout(self, openbrowser):
        '''获取修改页面的目录版面'''
        my_text = openbrowser.get_text(AirTrafficControlPressPage.atcpinfor_update_journal_contents_layout)
        return my_text

    def get_atcpinfor_update_journal_contents_title(self, openbrowser):
        '''获取修改页面的目录标题'''
        my_text = openbrowser.get_vlaue(AirTrafficControlPressPage.atcpinfor_update_journal_contents_title)
        return my_text

    def get_atcpinfor_update_journal_contents_author(self, openbrowser):
        '''获取修改页面的目录作者'''
        my_text = openbrowser.get_vlaue(AirTrafficControlPressPage.atcpinfor_update_journal_contents_author)
        return my_text

    def get_atcpinfor_update_journal_contents_editor(self, openbrowser):
        '''获取修改页面的目录内容'''
        my_text = openbrowser.get_text(AirTrafficControlPressPage.atcpinfor_update_journal_contents_editor)
        return my_text

    def assert_journal_contents_update_textcontent(self, openbrowser, atcp_layout,atcp_title,atcp_author,atcp_editor):
        '''封装编辑内容检查'''
        page_atcp_layout = self.get_atcpinfor_update_journal_contents_layout(openbrowser)
        page_atcp_title = self.get_atcpinfor_update_journal_contents_title(openbrowser)
        page_atcp_author = self.get_atcpinfor_update_journal_contents_author(openbrowser)
        page_atcp_editor = self.get_atcpinfor_update_journal_contents_editor(openbrowser)

        message = "编辑回显内容："
        flag = True
        if page_atcp_layout == atcp_layout:
            message += "目录版面编号{0}与新增的数据{1}一致".format(page_atcp_layout, atcp_layout)
        else:
            message += "目录版面编号{0}与新增的数据{1}不一致".format(page_atcp_layout, atcp_layout)
            flag = False
        if page_atcp_title == atcp_title:
            message += "目录标题{0}与新增的数据{1}一致".format(page_atcp_title, atcp_title)
        else:
            message += "目录标题{0}与新增的数据{1}不一致".format(page_atcp_title, atcp_title)
            flag = False
        if page_atcp_author == atcp_author:
            message += "目录作者{0}与新增的数据{1}一致".format(page_atcp_author, atcp_author)
        else:
            message += "目录作者{0}与新增的数据{1}不一致".format(page_atcp_author, atcp_author)
            flag = False
        if page_atcp_editor == atcp_editor:
            message += "目录内容{0}与新增的数据{1}一致".format(page_atcp_editor, atcp_editor)
        else:
            message += "目录内容{0}与新增的数据{1}不一致".format(page_atcp_editor, atcp_editor)
            flag = False
        return flag, message

    def assert_journal_contents_page_update_textcontent(self, openbrowser):
        '''封装判断修改页面文本是否一致'''
        res = openbrowser.is_text_in_element(AirTrafficControlPressPage.assert_page_journal_contents_update_text,
                                             "报刊版面编辑")#目录编辑
        return res

    def atcpinfor_journal_contents_update_submit_button_click(self, openbrowser):
        '''封装修改保存按钮点击'''
        openbrowser.click_my(AirTrafficControlPressPage.atcpinfor_journal_contents_update_submit_button)

    def assert_journal_contents_update_message_textcontent(self, openbrowser):
        '''封装判断修改成功'''
        res = openbrowser.is_text_in_element(AirTrafficControlPressPage.assert_journal_contents_update_message_text,
                                             "编辑成功")
        return res

    '''目录-删除'''

    def atcpinfor_journal_contents_delete_button_click(self, openbrowser):
        '''封装点击删除按钮'''
        openbrowser.click_my(AirTrafficControlPressPage.atcpinfor_journal_contents_delete_button)  # 点击删除按钮

    def assert_atcpinfor_journal_contents_delete_alert_textcontent(self, openbrowser):
        '''封装判断页面文本是否一致,来判断是否弹出删除对话框'''
        res = openbrowser.is_text_in_element(
            AirTrafficControlPressPage.assert_atcpinfor_journal_contents_delete_alert_text, "确定删除吗？")
        return res

    def atcpinfor_journal_contents_delete_alert_submit_button_click(self, openbrowser):
        '''封装点击确定'''
        openbrowser.click_my(AirTrafficControlPressPage.atcpinfor_journal_contents_delete_alert_submit_button)  # 点击确定按钮

    def assert_atcpinfor_journal_contents_delete_message_textcontent(self, openbrowser):
        '''封装判断页面文本是否一致,来判断是否删除成功'''
        res = openbrowser.is_text_in_element(
            AirTrafficControlPressPage.assert_atcpinfor_journal_contents_delete_message_text, "删除成功")
        return res