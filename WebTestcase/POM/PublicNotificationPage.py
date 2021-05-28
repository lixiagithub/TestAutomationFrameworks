# coding = utf-8
# Author:李昰 
# Date：2021/5/10 14:01
from selenium.webdriver.common.by import By

class PublicNotificationPage():
    pninfor_tab_close_button = (By.XPATH, '/html/body/div[2]/div/div[2]/nav/div/a[2]/i')  # 公示通报页面关闭
    pninfor_iframe = (By.XPATH, '//*[@id="content-main"]/iframe[2]')  # 公示通报页面iframe
    assert_page_text = (By.XPATH, '/html/body/div[1]/div/div/div[3]/div[2]/div/div[1]/div/span')  # 公示通报列表名
    assert_table_number = (By.XPATH, '//*[@id="table"]/div[1]/div[2]/div[4]/div[1]/span[1]')  # 总共多少条数
    '''新增'''
    pninfor_add_button = (By.XPATH, "//*[text()='新增']")  # 新增按钮
    assert_page_add_text = (By.XPATH, ' // *[ @ id = "forms"] / div[1] / div / div / div[1] / div / span')  # 公示通报新增文本title校验
    pninfor_add_title = (By.XPATH, '//*[@id="pa_title"]')  # 公示通报新增标题
    pninfor_add_editor = (By.XPATH, '//*[@id="editor"]')  # 公示通报新增内容
    pninfor_add_choosefile_button = (By.XPATH, '//*[@id="forms"]/div/div[7]/div/div/div/a[1]')  # 公示通报新增缩略图点击选择文件按钮
    pninfor_add_default_diagram_button = (By.XPATH, "//*[text()='在图库选择默认图']")  # 公示通报新增缩略图在图库选择默认图
    show_photo_album_select = (By.XPATH, '//*[@id="forms"]/div/div/div[1]/div/div/div/span')  # 相册下拉
    select_photo_album_ul = (By.XPATH, '//*[@id="select2-gallery-results"]')  # 相册ul
    select_photo_album_li = (By.CLASS_NAME, 'select2-results__option')  # 相册li
    select_photos = (By.CLASS_NAME, 'cbp-item')  # 选择全部photo
    select_photo_buttons = (
        By.CLASS_NAME, 'cbp-l-caption-buttonLeft btn red uppercase btn red uppercase')  # 选择photo的所有选择按钮
    pninfor_add_submit_button = (By.XPATH, "//*[text()='提交']")  # 公示通报新增提交按钮
    pninfor_add_cancel_button = (By.XPATH, "//*[text()='取消']")  # 公示通报新增取消按钮

    '''查询'''
    pninfor_query_name = (By.XPATH, '//*[@id="pa_title"]')  # 公示通报查询名称
    pninfor_query_button = (By.XPATH, "//*[text()='查询']")  # 公示通报查询按钮
    pninfor_query_empty = (By.XPATH, '//*[@id="client_table"]/tbody/tr/td')  # 公示通报查询为空

    '''修改'''
    pninfor_update_button = (By.XPATH, "//*[text()=' 编辑']")  # 点击第一个编辑按钮
    pninfor_update_title = (By.XPATH, '//*[@id="pa_title"]')  # 编辑页面文章标题-回显
    pninfor_update_editor = (By.XPATH, '//*[@id="editor"]')  # 编辑页面内容-回显
    pninfor_update_organization = (By.CLASS_NAME, 'curSelectedNode')  # 编辑页面对应组织-回显
    assert_page_update_text = (By.XPATH, '//*[@id="forms"]/div[1]/div/div/div[1]/div/span')  # 公示通报修改文本title校验
    pninfor_update_submit_button = (By.XPATH, "//*[text()='提交']")  # 公示通报修改提交按钮
    pninfor_update_cancel_button = (By.XPATH, "//*[text()='取消']")  # 公示通报修改取消按钮
    assert_update_message_text = (By.CLASS_NAME, 'layui-layer-content')  # 公示通报修改是否成功文本

    '''详情'''
    pninfor_detail_button = (By.XPATH, "//*[text()=' 详情']")  # 公示通报详情按钮
    assert_page_detail_text = (By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div/div[1]/div[1]/span')  # 公示通报详情页文本title校验
    pninfor_detail_title = (By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div/div[2]/div/div[1]/span[1]')  # 公示通报标题名称
    pninfor_detail_editor = (By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div/div[2]/div/div[2]/div/p')  # 公示通报内容
    pninfor_detail_organization = (By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div/div[2]/div/div[1]/div/span[3]')  # 公示通报组织
    pbdinfor_return_button = (By.XPATH, "//*[text()='返回']")  # 公示通报详情页返回按钮

    '''置顶'''
    pninfor_top_button = (By.XPATH, "//*[text()=' 置顶']")  # 公示通报置顶按钮
    assert_pninfor_top_alert_text = (By.CLASS_NAME, 'layui-layer-content')  # 公示通报置顶提示框文本校验
    pninfor_top_alert_submit_button = (By.CLASS_NAME, 'layui-layer-btn0')  # 公示通报置顶确定按钮
    pninfor_top_alert_cancel_button = (By.CLASS_NAME, 'layui-layer-btn1')  # 公示通报置顶取消按钮
    assert_top_message_text = (By.CLASS_NAME, 'layui-layer-content')  # 公示通报置顶是否成功文本

    '''取消置顶'''
    pninfor_canceltop_button = (By.XPATH, "//*[text()=' 取消置顶']")  # 公示通报取消置顶按钮
    assert_pninfor_canceltop_alert_text = (By.CLASS_NAME, 'layui-layer-content')  # 公示通报取消置顶提示框文本校验
    pninfor_canceltop_alert_submit_button = (By.CLASS_NAME, 'layui-layer-btn0')  # 公示通报取消置顶确定按钮
    pninfor_canceltop_alert_cancel_button = (By.CLASS_NAME, 'layui-layer-btn1')  # 公示通报取消置顶取消按钮
    assert_canceltop_message_text = (By.CLASS_NAME, 'layui-layer-content')  # 公示通报取消置顶是否成功文本

    '''删除'''
    pninfor_delete_button = (By.XPATH, "//*[text()=' 删除']")  # 公示通报删除按钮
    assert_pninfor_delete_alert_text = (By.CLASS_NAME, 'layui-layer-content')  # 公示通报删除提示框文本校验
    pninfor_delete_alert_submit_button = (By.CLASS_NAME, 'layui-layer-btn0')  # 公示通报删除确定按钮
    pninfor_delete_alert_cancel_button = (By.CLASS_NAME, 'layui-layer-btn1')  # 公示通报删除取消按钮
    assert_delete_message_text = (By.CLASS_NAME, 'layui-layer-content')  # 公示通报删除是否成功文本

    def click_pninfor_tab_close_button(self, openbrowser):
        '''封装点击关闭按钮'''
        openbrowser.click_my(PublicNotificationPage.pninfor_tab_close_button)

    def into_pninfor_iframe(self, openbrowser):
        '''封装进入iframe'''
        openbrowser.is_iframe(PublicNotificationPage.pninfor_iframe)

    def assert_page_textcontent(self, openbrowser):
        '''封装判断页面文本是否一致,来判断是否进入用户管理页面'''
        res = openbrowser.is_text_in_element(PublicNotificationPage.assert_page_text, "公示通报列表")
        return res

    def assert_table_number_text(self, openbrowser):
        '''获取公示通报总数'''
        table_number = openbrowser.get_table_total_number(PublicNotificationPage.assert_table_number)
        return table_number

    '''封装新增'''

    def random_click_node(self,openbrowser):
        '''封装随机点击树形结构中的某个节点'''
        node_text=openbrowser.random_click_node_js()
        return node_text

    def click_pninfor_add_button(self, openbrowser):
        '''封装点击新增按钮'''
        openbrowser.click_my(PublicNotificationPage.pninfor_add_button)

    def assert_page_add_textcontent(self, openbrowser):
        '''封装判断添加页面文本是否一致'''
        res = openbrowser.is_text_in_element(PublicNotificationPage.assert_page_add_text, "党务公开新增")
        return res

    def pninfor_add_name_input(self, openbrowser, input_text):
        '''封装输入文章名称'''
        openbrowser.send_key_my(PublicNotificationPage.pninfor_add_title, input_text)

    def pninfor_add_editor_input(self, openbrowser, input_text):
        '''封装输入文章内容'''
        openbrowser.send_key_my(PublicNotificationPage.pninfor_add_editor, input_text)

    def pninfor_add_default_diagram_select(self, openbrowser):
        '''封装选择图库图片'''
        openbrowser.click_my(PublicNotificationPage.pninfor_add_default_diagram_button)  # 点击在图库选择默认图按钮
        openbrowser.driver.switch_to.frame(0)  # 进入第三层图片iframe
        openbrowser.click_my(PublicNotificationPage.show_photo_album_select)  # 显示相册下拉列表
        openbrowser.random_select_ul(PublicNotificationPage.select_photo_album_li)  # 随机选择相册下拉li
        openbrowser.random_select_pic(PublicNotificationPage.select_photos)  # 随机选择一个photo

    def pninfor_add_submit_button_click(self, openbrowser):
        '''封装提交按钮点击'''
        openbrowser.click_my(PublicNotificationPage.pninfor_add_submit_button)

    def pninfor_add_cancel_button_click(self, openbrowser):
        '''封装取消按钮点击'''
        openbrowser.click_my(PublicNotificationPage.pninfor_add_cancel_button)

    def pninfor_add(self, openbrowser, name, editor):
        '''封装公示通报增加'''
        pninfor_classify = self.random_click_node(openbrowser)#随机选择对应组织
        self.pninfor_add_name_input(openbrowser, name)  # 输入文章摘要
        self.pninfor_add_editor_input(openbrowser, editor)  # 输入文章内容
        self.pninfor_add_default_diagram_select(openbrowser)  # 随机选择图片库图片
        openbrowser.driver.switch_to.parent_frame()  # 切换到第二层新增iframe
        self.pninfor_add_submit_button_click(openbrowser)  # 点击提交按钮
        return pninfor_classify

    '''封装查询'''

    def pninfor_query_button_click(self, openbrowser):
        '''封装查询按钮点击'''
        openbrowser.click_my(PublicNotificationPage.pninfor_query_button)

    def pninfor_query_name_input(self, openbrowser, input_text):
        '''封装查询名称'''
        openbrowser.send_key_my(PublicNotificationPage.pninfor_query_name, input_text)

    def pninfor_query(self, openbrowser, name):
        '''封装查询'''
        self.pninfor_query_name_input(openbrowser, name)  # 输入关键字
        self.pninfor_query_button_click(openbrowser)  # 点击查询按钮

    '''封装修改'''

    def pninfor_update_button_click(self, openbrowser):
        '''封装编辑按钮点击'''
        openbrowser.click_my(PublicNotificationPage.pninfor_update_button)

    def get_update_pninfor_title(self, openbrowser):
        '''获取修改页面的标题'''
        my_text = openbrowser.get_vlaue(PublicNotificationPage.pninfor_update_title)
        return my_text

    def get_update_pninfor_editor(self, openbrowser):
        '''获取修改页面的内容'''
        my_text = openbrowser.get_text(PublicNotificationPage.pninfor_update_editor)
        return my_text

    def get_update_pninfor_organization(self, openbrowser):
        '''获取修改页面的对应组织'''
        my_text = openbrowser.get_text(PublicNotificationPage.pninfor_update_organization)
        return my_text

    def assert_update_textcontent(self, openbrowser, pn_name, pn_editor,pn_organization):
        '''封装编辑内容检查'''
        page_pn_name = self.get_update_pninfor_title(openbrowser)
        page_pn_editor = self.get_update_pninfor_editor(openbrowser)
        page_pn_organization = self.get_update_pninfor_organization(openbrowser)
        message = "编辑回显内容："
        flag = True
        if page_pn_name == pn_name:
            message += "页面公示通报标题{0}与新增的数据{1}一致".format(page_pn_name, pn_name)
        else:
            message += "页面公示通报标题{0}与新增的数据{1}不一致".format(page_pn_name, pn_name)
            flag = False
        if page_pn_organization == pn_organization:
            message += ",页面公示通报对应组织{0}与新增的数据{1}一致".format(page_pn_organization, pn_organization)
        else:
            message += ",页面党公示通报对应组织{0}与新增的数据{1}不一致".format(page_pn_organization, pn_organization)
            flag = False

        if page_pn_editor == pn_editor:
            message += ",页面公示通报内容{0}与新增的数据{1}一致".format(page_pn_editor, pn_editor)
        else:
            message += ",页面公示通报内容{0}与新增的数据{1}不一致".format(page_pn_editor, pn_editor)
            flag = False
        return flag, message

    def assert_page_update_textcontent(self, openbrowser):
        '''封装判断修改页面文本是否一致'''
        res = openbrowser.is_text_in_element(PublicNotificationPage.assert_page_update_text, "党务公开编辑")
        return res

    def pninfor_update_submit_button_click(self, openbrowser):
        '''封装修改提交按钮点击'''
        openbrowser.click_my(PublicNotificationPage.pninfor_update_submit_button)

    def assert_update_message_textcontent(self, openbrowser):
        '''封装判断修改成功'''
        res = openbrowser.is_text_in_element(PublicNotificationPage.assert_update_message_text, "修改成功")
        return res

    '''封装详情'''

    def pninfor_detail_button_click(self, openbrowser):
        '''封装详情按钮点击'''
        openbrowser.click_my(PublicNotificationPage.pninfor_detail_button)

    def assert_page_detail_textcontent(self, openbrowser):
        '''封装判断详情页面文本是否一致'''
        res = openbrowser.is_text_in_element(PublicNotificationPage.assert_page_detail_text, "公示通告详情")
        return res

    def get_detail_pninfor_title(self, openbrowser):
        '''封装获取公示通告标题'''
        my_text = openbrowser.get_text(PublicNotificationPage.pninfor_detail_title)
        return my_text

    def get_detail_pninfor_editor(self, openbrowser):
        '''封装获取公示通告内容'''
        my_text = openbrowser.get_text(PublicNotificationPage.pninfor_detail_editor)
        return my_text

    def get_detail_pninfor_organization(self, openbrowser):
        '''封装获取公示通告组织'''
        my_text = openbrowser.get_text(PublicNotificationPage.pninfor_detail_organization).split('组织：')[1].strip()
        return my_text

    def assert_detail_textcontent(self, openbrowser, pn_name, pn_editor,pn_organization):
        '''封装详情内容检查'''
        page_pn_title = self.get_detail_pninfor_title(openbrowser)
        page_pn_organization = self.get_detail_pninfor_organization(openbrowser)
        page_pn_editor = self.get_detail_pninfor_editor(openbrowser)
        message = "详情内容："
        flag = True
        if page_pn_title == pn_name:
            message += "页面公示通报标题{0}与新增的数据{1}一致".format(page_pn_title, pn_name)
        else:
            message += "页面公示通报标题{0}与新增的数据{1}不一致".format(page_pn_title, pn_name)
            flag = False
        if page_pn_organization == pn_organization:
            message += ",页面公示通报组织{0}与新增的数据{1}一致".format(page_pn_organization, pn_organization)
        else:
            message += ",页面公示通报组织{0}与新增的数据{1}不一致".format(page_pn_organization, pn_organization)
            flag = False

        if page_pn_editor == pn_editor:
            message += ",页面公示通报内容{0}与新增的数据{1}一致".format(page_pn_editor, pn_editor)
        else:
            message += ",页面公示通报内容{0}与新增的数据{1}不一致".format(page_pn_editor, pn_editor)
            flag = False
        return flag, message

    def pninfor_detail_return_click(self, openbrowser):
        '''封装详情返回按钮点击'''
        openbrowser.click_my(PublicNotificationPage.pbdinfor_return_button)

    '''封装置顶'''

    def pninfor_top_button_click(self, openbrowser):
        '''封装点击置顶'''
        openbrowser.click_my(PublicNotificationPage.pninfor_top_button)  # 点击置顶按钮

    def assert_pninfor_top_alert_textcontent(self, openbrowser):
        '''封装判断页面文本是否一致,来判断弹出置顶对话框'''
        res = openbrowser.is_text_in_element(PublicNotificationPage.assert_pninfor_top_alert_text, "确定置顶吗？")
        return res

    def pninfor_top_alert_submit_button_click(self, openbrowser):
        '''封装点击确定'''
        openbrowser.click_my(PublicNotificationPage.pninfor_top_alert_submit_button)  # 点击确定按钮

    def assert_top_message_textcontent(self, openbrowser):
        '''封装判断页面文本是否一致,来判断置顶成功'''
        res = openbrowser.is_text_in_element(PublicNotificationPage.assert_top_message_text, "置顶成功")
        return res

    '''封装取消置顶'''

    def pninfor_canceltop_button_click(self, openbrowser):
        '''封装点击取消置顶'''
        openbrowser.click_my(PublicNotificationPage.pninfor_canceltop_button)  # 点击取消置顶按钮

    def assert_pninfor_canceltop_alert_textcontent(self, openbrowser):
        '''封装判断页面文本是否一致,来判断是否弹出取消置顶对话框'''
        res = openbrowser.is_text_in_element(PublicNotificationPage.assert_pninfor_canceltop_alert_text, "确定取消置顶吗？")
        return res

    def pninfor_canceltop_alert_submit_button_click(self, openbrowser):
        '''封装点击确定按钮'''
        openbrowser.click_my(PublicNotificationPage.pninfor_canceltop_alert_submit_button)  # 点击确定按钮

    def assert_canceltop_message_textcontent(self, openbrowser):
        '''封装判断页面文本是否一致,来判断取消置顶成功'''
        res = openbrowser.is_text_in_element(PublicNotificationPage.assert_canceltop_message_text, "取消置顶成功")
        return res

    '''删除'''

    def pninfor_delete_button_click(self, openbrowser):
        '''封装点击删除按钮'''
        openbrowser.click_my(PublicNotificationPage.pninfor_delete_button)  # 点击删除按钮

    def assert_pninfor_delete_alert_textcontent(self, openbrowser):
        '''封装判断页面文本是否一致,来判断是否弹出删除对话框'''
        res = openbrowser.is_text_in_element(PublicNotificationPage.assert_pninfor_delete_alert_text, "确定删除吗？")
        return res

    def pninfor_delete_alert_submit_button_click(self, openbrowser):
        '''封装点击确定'''
        openbrowser.click_my(PublicNotificationPage.pninfor_delete_alert_submit_button)  # 点击确定按钮

    def assert_delete_message_textcontent(self, openbrowser):
        '''封装判断页面文本是否一致,来判断是否删除成功'''
        res = openbrowser.is_text_in_element(PublicNotificationPage.assert_delete_message_text, "删除成功")
        return res