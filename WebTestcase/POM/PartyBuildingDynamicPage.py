# coding = utf-8
# Author:李昰 
# Date：2021/4/21 14:55
from selenium.webdriver.common.by import By
import random  # 导入随机选取
from log.log import logger


class PartyBuildingDynamicPage():
    pbdinfor_tab_close_button = (By.XPATH, '/html/body/div[2]/div/div[2]/nav/div/a[2]/i')  # 党建动态页面关闭
    pbdinfor_iframe = (By.XPATH, '//*[@id="content-main"]/iframe[2]')  # 党建动态页面iframe
    assert_page_text = (By.XPATH, '/html/body/div[1]/div/div/div[3]/div[2]/div/div[1]/div/span')  # 党建动态列表名
    pbdinfor_classify = (By.XPATH, '//*[@id="treeDemo"]/li')  # 左侧树形党建动态分类
    assert_table_number = (By.XPATH, '//*[@id="table"]/div[1]/div[2]/div[4]/div[1]/span[1]')  # 总共多少条数

    '''新增'''
    pbdinfor_add_button = (By.XPATH, "//*[text()='新增']")  # 新增按钮
    assert_page_add_text = (By.CLASS_NAME, 'layui-layer-title')  # 党建动态新增文本title校验
    pbdinfor_add_pbd_name = (By.XPATH, '//*[@id="pbd_name"]')  # 党建动态新增名称
    pbdinfor_add_pbd_desc = (By.XPATH, '//*[@id="pbd_desc"]')  # 党建动态新增摘要
    pbdinfor_add_pbd_editor = (By.XPATH, '//*[@id="editor"]')  # 党建动态新增内容
    pbdinfor_add_choosefile_button = (By.XPATH, '//*[@id="forms"]/div/div[7]/div/div/div/a[1]')  # 党建动态新增缩略图点击选择文件按钮
    pbdinfor_add_default_diagram_button = (
        By.XPATH, "//*[text()='在图库选择默认图']")  # 党建动态新增缩略图在图库选择默认图
    pbdinfor_add_default_diagram_iframe = (By.XPATH, '/html/body/div[6]')  # 党建动态新增缩略图iframe
    show_photo_album_select = (By.XPATH, '//*[@id="forms"]/div/div/div[1]/div/div/div/span')  # 相册下拉
    select_photo_album_ul = (By.XPATH, '//*[@id="select2-gallery-results"]')  # 相册ul
    select_photo_album_li = (By.CLASS_NAME, 'select2-results__option')  # 相册li
    select_photos = (By.CLASS_NAME, 'cbp-item')  # 选择全部photo
    select_photo_buttons = (
        By.CLASS_NAME, 'cbp-l-caption-buttonLeft btn red uppercase btn red uppercase')  # 选择photo的所有选择按钮
    pbdinfor_add_submit_button = (By.XPATH, "//*[text()='下发']")  # 党建动态新增下发按钮
    pbdinfor_add_cancel_button = (By.XPATH, "//*[text()='取消']")  # 党建动态新增取消按钮

    '''修改'''
    pbdinfor_update_button = (By.XPATH, "//*[text()=' 编辑']")  # 点击第一个编辑按钮
    table_pbdinfor_title_text = (By.XPATH, '//*[@id="client_table"]/tbody/tr/td[3]')  # 列表中的文章名称
    pbdinfor_update_title_text = (By.XPATH, '//*[@id="pbd_name"]')  # 编辑页面文章名称-回显
    assert_page_update_text = (By.CLASS_NAME, 'layui-layer-title')  # 党建动态修改文本title校验
    pbdinfor_update_submit_button = (By.XPATH, "//*[text()='修改']")  # 党建动态修改提交按钮
    pbdinfor_update_cancel_button = (By.XPATH, "//*[text()='取消']")  # 党建动态修改取消按钮
    assert_update_message_text = (By.CLASS_NAME, 'layui-layer-content')  # 党建动态修改是否成功文本

    '''查询'''
    pbdinfor_query_name = (By.XPATH, '//*[@id="pbd_name"]')  # 党建动态查询名称
    pbdinfor_query_button = (By.XPATH, "//*[text()='查询']")  # 党建动态查询按钮
    pbdinfor_query_empty = (By.XPATH, '//*[@id="client_table"]/tbody/tr/td')  # 党建动态查询为空

    '''详情'''
    pbdinfor_detail_button = (By.XPATH, "//*[text()=' 详情']")  # 党建动态详情按钮
    assert_page_detail_text = (By.CLASS_NAME, 'layui-layer-title')  # 党建动态详情页文本title校验
    pbdinfor_detail_pbd_name = (By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[1]/div/div[1]/span[1]')  # 党建动态标题名称
    pbdinfor_detail_pbd_desc = (By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[1]/div/span')  # 党建动态摘要
    pbdinfor_detail_pbd_editor = (By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[1]/div/div[2]/div/p')  # 党建动态内容
    pbdinfor_like_button = (By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[3]/div[2]/a/span')  # 党建动态点赞按钮
    assert_page_like_text = (By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[1]/div[1]/span')  # 党建动态点赞详情页文本title校验
    pbdinfor_like_back_button = (By.XPATH, "//*[text()='返回']")  # 党建动态点赞详情页返回按钮
    pbdinfor_like_close_button = (By.XPATH, '//*[@id="layui-layer3"]/span[1]/a')  # 党建动态详情页关闭按钮

    '''删除'''
    pbdinfor_delete_button = (By.XPATH, "//*[text()=' 删除']")  # 党建动态删除按钮
    assert_pbdinfor_delete_alert_text = (By.CLASS_NAME, 'layui-layer-content')  # 党建动态删除提示框文本校验
    pbdinfor_delete_alert_submit_button = (By.CLASS_NAME, 'layui-layer-btn0')  # 党建动态删除确定按钮
    pbdinfor_delete_alert_cancel_button = (By.CLASS_NAME, 'layui-layer-btn1')  # 党建动态删除取消按钮
    assert_delete_message_text = (By.CLASS_NAME, 'layui-layer-content')  # 党建动态删除是否成功文本

    def click_pbdinfor_tab_close_button(self, openbrowser):
        '''封装点击关闭按钮'''
        openbrowser.click_my(PartyBuildingDynamicPage.pbdinfor_tab_close_button)

    def into_pbdinfor_iframe(self, openbrowser):
        '''封装进入iframe'''
        openbrowser.is_iframe(PartyBuildingDynamicPage.pbdinfor_iframe)

    def assert_page_textcontent(self, openbrowser):
        '''封装判断页面文本是否一致,来判断是否进入党建动态页面'''
        res = openbrowser.is_text_in_element(PartyBuildingDynamicPage.assert_page_text, "党建动态列表")
        return res

    def random_pbdinfor_classify(self, openbrowser):
        '''封装随机选择左侧树形党建动态分类'''
        res = openbrowser.random_click_node(PartyBuildingDynamicPage.pbdinfor_classify)
        return res

    def assert_table_number_text(self, openbrowser):
        '''获取党建动态总数'''
        table_number = openbrowser.get_table_total_number(PartyBuildingDynamicPage.assert_table_number)
        return table_number

    '''封装新增'''

    def click_pbdinfor_add_button(self, openbrowser):
        '''封装点击新增按钮'''
        openbrowser.click_my(PartyBuildingDynamicPage.pbdinfor_add_button)

    def assert_page_add_textcontent(self, openbrowser):
        '''封装判断添加页面文本是否一致'''
        res = openbrowser.is_text_in_element(PartyBuildingDynamicPage.assert_page_add_text, "党建动态新增")
        return res

    def pbdinfor_add_name_input(self, openbrowser, input_text):
        '''封装输入文章名称'''
        openbrowser.send_key_my(PartyBuildingDynamicPage.pbdinfor_add_pbd_name, input_text)

    def pbdinfor_add_description_input(self, openbrowser, input_text):
        '''封装输入文章摘要'''
        openbrowser.send_key_my(PartyBuildingDynamicPage.pbdinfor_add_pbd_desc, input_text)

    def pbdinfor_add_editor_input(self, openbrowser, input_text):
        '''封装输入文章内容'''
        openbrowser.send_key_my(PartyBuildingDynamicPage.pbdinfor_add_pbd_editor, input_text)

    def pbdinfor_add_default_diagram_select(self, openbrowser):
        '''封装选择图库图片'''
        openbrowser.click_my(PartyBuildingDynamicPage.pbdinfor_add_default_diagram_button)  # 点击在图库选择默认图按钮
        openbrowser.driver.switch_to.frame(0)  # 进入第三层图片iframe
        openbrowser.click_my(PartyBuildingDynamicPage.show_photo_album_select)  # 显示相册下拉列表
        openbrowser.random_select_ul(PartyBuildingDynamicPage.select_photo_album_li)  # 随机选择相册下拉li
        openbrowser.random_select_pic(PartyBuildingDynamicPage.select_photos)  # 随机选择一个photo

    def pbdinfor_add_submit_button_click(self, openbrowser):
        '''封装提交按钮点击'''
        openbrowser.click_my(PartyBuildingDynamicPage.pbdinfor_add_submit_button)

    def pbdinfor_add_cancel_button_click(self, openbrowser):
        '''封装取消按钮点击'''
        openbrowser.click_my(PartyBuildingDynamicPage.pbdinfor_add_cancel_button)

    def pbdinfor_add(self, openbrowser, name, description, editor):
        '''封装党建动态增加'''
        self.pbdinfor_add_name_input(openbrowser, name)  # 输入文章摘要
        self.pbdinfor_add_description_input(openbrowser, description)  # 输入文章摘要
        self.pbdinfor_add_editor_input(openbrowser, editor)  # 输入文章内容
        self.pbdinfor_add_default_diagram_select(openbrowser)  # 随机选择图片库图片
        openbrowser.driver.switch_to.parent_frame()  # 切换到第二层新增iframe
        self.pbdinfor_add_submit_button_click(openbrowser)  # 点击提交按钮

    '''封装修改'''

    def pbdinfor_update_button_click(self, openbrowser):
        '''封装编辑按钮点击'''
        openbrowser.click_my(PartyBuildingDynamicPage.pbdinfor_update_button)

    def get_table_pbdinfor_title_text(self, openbrowser):
        '''获取列表中的文章标题内容'''
        my_text = openbrowser.get_text(PartyBuildingDynamicPage.table_pbdinfor_title_text)
        return my_text

    def assert_update_table_pbdinfor_title_text(self, openbrowser, table_text):
        my_update_atcinfor_title_text = openbrowser.get_vlaue(PartyBuildingDynamicPage.pbdinfor_update_title_text)
        if my_update_atcinfor_title_text == table_text:
            return True
        else:
            return False

    def assert_page_update_textcontent(self, openbrowser):
        '''封装判断修改页面文本是否一致'''
        res = openbrowser.is_text_in_element(PartyBuildingDynamicPage.assert_page_update_text, "党建动态编辑")
        return res

    def pbdinfor_update_submit_button_click(self, openbrowser):
        '''封装修改提交按钮点击'''
        openbrowser.click_my(PartyBuildingDynamicPage.pbdinfor_update_submit_button)

    def assert_update_message_textcontent(self, openbrowser):
        '''封装判断修改成功'''
        res = openbrowser.is_text_in_element(PartyBuildingDynamicPage.assert_update_message_text, "修改成功")
        return res

    '''封装查询'''

    def pbdinfor_query_button_click(self, openbrowser):
        '''封装查询按钮点击'''
        openbrowser.click_my(PartyBuildingDynamicPage.pbdinfor_query_button)

    def pbdinfor_query_name_input(self, openbrowser, input_text):
        '''封装查询名称'''
        openbrowser.send_key_my(PartyBuildingDynamicPage.pbdinfor_query_name, input_text)

    def pbdinfor_query(self, openbrowser, name):
        '''封装查询'''
        self.pbdinfor_query_name_input(openbrowser, name)  # 输入关键字
        self.pbdinfor_query_button_click(openbrowser)  # 点击查询按钮

    def get_pbdinfor_classify(self, pbdinfor_classify):
        my_pbdinfor_classify = ""
        if pbdinfor_classify == "系统动态":
            my_pbdinfor_classify = "1"
        if pbdinfor_classify == "地区动态":
            my_pbdinfor_classify = "2"
        if pbdinfor_classify == "分局（站）动态":
            my_pbdinfor_classify = "3"
        if pbdinfor_classify == "支部动态":
            my_pbdinfor_classify = "4"
        return my_pbdinfor_classify

    '''封装详情'''

    def pbdinfor_detail_button_click(self, openbrowser):
        '''封装详情按钮点击'''
        openbrowser.click_my(PartyBuildingDynamicPage.pbdinfor_detail_button)

    def assert_page_detail_textcontent(self, openbrowser):
        '''封装判断详情页面文本是否一致'''
        res = openbrowser.is_text_in_element(PartyBuildingDynamicPage.assert_page_detail_text, "党建动态详情")
        return res

    def get_detail_pbd_name(self, openbrowser):
        '''封装获取党建动态标题'''
        my_text = openbrowser.get_text(PartyBuildingDynamicPage.pbdinfor_detail_pbd_name)
        return my_text

    def get_detail_pbd_desc(self, openbrowser):
        '''封装获取党建动态摘要'''
        my_text = openbrowser.get_text(PartyBuildingDynamicPage.pbdinfor_detail_pbd_desc)
        return my_text

    def get_detail_pbd_editor(self, openbrowser):
        '''封装获取党建动态内容'''
        my_text = openbrowser.get_text(PartyBuildingDynamicPage.pbdinfor_detail_pbd_editor)
        return my_text

    def assert_detail_textcontent(self, openbrowser, pbd_name, pbd_desc, pbd_editor):
        '''封装详情内容检查'''
        page_pbd_name = self.get_detail_pbd_name(openbrowser)
        page_pbd_desc = self.get_detail_pbd_desc(openbrowser).split('摘要:')[1].strip()
        page_pbd_editor = self.get_detail_pbd_editor(openbrowser)
        message = "详情内容："
        flag = True
        if page_pbd_name == pbd_name:
            message += "页面党建动态名称{0}与新增的数据{1}一致".format(page_pbd_name, pbd_name)
        else:
            message += "页面党建动态名称{0}与新增的数据{1}不一致".format(page_pbd_name, pbd_name)
            flag = False
        if page_pbd_desc == pbd_desc:
            message += ",页面党建动态摘要{0}与新增的数据{1}一致".format(page_pbd_desc, pbd_desc)
        else:
            message += ",页面党建动态摘要{0}与新增的数据{1}不一致".format(page_pbd_desc, pbd_desc)
            flag = False

        if page_pbd_editor == pbd_editor:
            message += ",页面党建动态内容{0}与新增的数据{1}相同，文本显示正确".format(page_pbd_editor, pbd_editor)
        else:
            message += ",页面党建动态内容{0}与新增的数据{1}不相同，文本显示错误".format(page_pbd_editor, pbd_editor)
            flag = False
        return flag, message

    def pbdinfor_like_button_click(self, openbrowser):
        '''封装点赞连接点击'''
        openbrowser.click_my(PartyBuildingDynamicPage.pbdinfor_like_button)

    def assert_page_like_textcontent(self, openbrowser):
        '''封装判断详情点赞页面文本是否一致'''
        res = openbrowser.is_text_in_element(PartyBuildingDynamicPage.assert_page_like_text, "党建动态点赞详情")
        return res

    def pbdinfor_like_back_button_click(self, openbrowser):
        '''封装返回点击'''
        openbrowser.click_my(PartyBuildingDynamicPage.pbdinfor_like_back_button)

    def pbdinfor_like_close_button_click(self, openbrowser):
        '''封装关闭点击'''
        openbrowser.click_my(PartyBuildingDynamicPage.pbdinfor_like_close_button)

    '''删除'''

    def pbdinfor_delete_button_click(self, openbrowser):
        '''封装点击删除按钮'''
        openbrowser.click_my(PartyBuildingDynamicPage.pbdinfor_delete_button)  # 点击删除按钮

    def assert_pbdinfor_delete_alert_textcontent(self, openbrowser):
        '''封装判断页面文本是否一致,来判断是否弹出删除对话框'''
        res = openbrowser.is_text_in_element(PartyBuildingDynamicPage.assert_pbdinfor_delete_alert_text, "您确定删除吗?")
        return res

    def pbdinfor_delete_alert_submit_button_click(self, openbrowser):
        '''封装点击确定'''
        openbrowser.click_my(PartyBuildingDynamicPage.pbdinfor_delete_alert_submit_button)  # 点击确定按钮

    def assert_delete_message_textcontent(self, openbrowser):
        '''封装判断页面文本是否一致,来判断是否删除成功'''
        res = openbrowser.is_text_in_element(PartyBuildingDynamicPage.assert_delete_message_text, "删除成功")
        return res
