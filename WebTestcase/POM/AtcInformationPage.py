# coding = utf-8
# Author:李昰 
# Date：2021/2/22 9:30
from selenium.webdriver.common.by import By


class AtcInformeationPage():
    atcinfor_tab_close_button = (By.XPATH, '/html/body/div[2]/div/div[2]/nav/div/a[2]/i')  # 空管资讯页面关闭
    atcinfor_iframe = (By.XPATH, '//*[@id="content-main"]/iframe[2]')  # 空管资讯页面iframe
    assert_page_text = (By.XPATH, '//*[@id="rdiva"]/div/span[1]')  # 空管资讯列表名
    atcinfor_add_iframe = (By.XPATH, '/html/body/div[6]/div[2]/iframe')  # 空管资讯新增页面
    '''新增'''
    atcinfor_add_button = (By.XPATH, '//*[@id="add"]')  # 新增按钮
    assert_page_add_text = (By.CLASS_NAME, 'layui-layer-title')  # 空管资讯新增文本title校验
    atcinfor_add_title = (By.XPATH, '//*[@id="article_title"]')  # 空管资讯新增文章标题
    atcinfor_add_time = (By.XPATH, '//*[@id="release_time"]')  # 空管资讯新增计划发布时间
    atcinfor_add_time_now_button = (By.XPATH, '//*[@id="layui-laydate1"]/div[2]/div/span[2]')  # 空管资讯新增计划发布时间选择现在
    atcinfor_add_order = (By.XPATH, '//*[@id="forms"]/div/div[3]/div/div/div/input')  # 空管资讯新增排序
    atcinfor_add_keyword = (By.XPATH, '//*[@id="forms"]/div/div[4]/div/div/div/input')  # 空管资讯新增文章关键字
    atcinfor_add_description = (By.XPATH, '//*[@id="maxlength_textarea"]')  # 空管资讯新增文章摘要
    atcinfor_add_editor = (By.XPATH, '//*[@id="editor"]')  # 空管资讯新增文章内容
    atcinfor_add_choosefile_button = (By.XPATH, '//*[@id="forms"]/div/div[7]/div/div/div/a[1]')  # 空管资讯新增缩略图点击选择文件按钮
    atcinfor_add_default_diagram_button = (
    By.XPATH, '//*[@id="forms"]/div/div[7]/div/div/div/a[2]')  # 空管资讯新增缩略图在图库选择默认图
    atcinfor_add_default_diagram_iframe = (By.XPATH, '/html/body/div[6]')  # 空管资讯新增缩略图iframe
    show_photo_album_select = (By.XPATH, '//*[@id="forms"]/div/div/div[1]/div/div/div/span')  # 相册下拉
    select_photo_album_ul = (By.XPATH, '//*[@id="select2-gallery-results"]')  # 相册ul
    select_photo_album_li = (By.CLASS_NAME, 'select2-results__option')  # 相册li
    select_photos = (By.CLASS_NAME, 'cbp-item')  # 选择全部photo
    select_photo_buttons = (
    By.CLASS_NAME, 'cbp-l-caption-buttonLeft btn red uppercase btn red uppercase')  # 选择photo的所有选择按钮
    atcinfor_add_submit_button = (By.XPATH, '//*[@id="forms"]/div/div[8]/button[2]')  # 空管资讯新增提交按钮
    atcinfor_add_cancel_button = (By.XPATH, '//*[@id="forms"]/div/div[8]/button[1]')  # 空管资讯新增取消按钮
    assert_table_number = (By.XPATH, '//*[@id="table"]/div[1]/div[2]/div[4]/div[1]/span[1]')  # 总共多少条数

    '''修改'''
    atcinfor_update_button = (By.XPATH, '//*[@id="client_table"]/tbody/tr[1]/td[8]/a[1]')  # 点击第一个编辑按钮
    table_atcinfor_title_text = (By.XPATH, '//*[@id="client_table"]/tbody/tr[1]/td[2]/a')  # 列表中的文章名称
    atcinfor_update_title_text = (By.XPATH, '//*[@id="article_title"]')  # 编辑页面文章标题-回显
    assert_page_update_text = (By.CLASS_NAME, 'layui-layer-title')  # 空管资讯修改文本title校验
    atcinfor_update_submit_button = (By.XPATH, '//*[@id="forms"]/div/div[8]/button[2]')  # 空管资讯新增提交按钮
    atcinfor_update_cancel_button = (By.XPATH, '//*[@id="forms"]/div/div[8]/button[1]')  # 空管资讯新增取消按钮
    assert_update_message_text = (By.CLASS_NAME, 'layui-layer-content')  # 空管资讯修改是否成功文本

    '''查询'''
    atcinfor_query_startdate = (By.XPATH, '//*[@id="start_time"]')  # 空管资讯查询开始日期
    atcinfor_query_enddate = (By.XPATH, '//*[@id="end_time"]')  # 空管资讯查询结束日期
    atcinfor_query_startdate_now = (By.XPATH, '//*[@id="layui-laydate1"]/div[2]/div/span[2]')  # 空管资讯查询开始日期选择现在
    atcinfor_query_keyword = (By.XPATH, '//*[@id="keyword"]')  # 空管资讯查询关键字
    atcinfor_query_enddate_now = (By.XPATH, '//*[@id="layui-laydate2"]/div[2]/div/span[2]')  # 空管资讯查询结束日期选择现在
    atcinfor_query_button = (By.XPATH, '//*[@id="rdivb"]/div[1]/div[3]/button')  # 空管资讯查询按钮
    atcinfor_query_empty = (By.XPATH, '//*[@id="client_table"]/tbody/tr/td')  # 空管资讯查询为空

    '''置顶'''
    atcinfor_top_button = (By.CLASS_NAME, 'btn green btn-xs btn-outline')  # 空管资讯置顶按钮
    assert_atcinfor_top_alert_text = (By.CLASS_NAME, 'layui-layer-content')  # 空管资讯置顶提示框文本校验
    atcinfor_top_alert_submit_button = (By.CLASS_NAME, 'layui-layer-btn0')  # 空管资讯置顶确定按钮
    atcinfor_top_alert_cancel_button = (By.CLASS_NAME, 'layui-layer-btn1')  # 空管资讯置顶取消按钮
    assert_top_message_text = (By.CLASS_NAME, 'layui-layer-content')  # 空管资讯置顶是否成功文本

    '''取消置顶'''
    atcinfor_canceltop_button = (By.CLASS_NAME, 'btn blue btn-xs btn-outline')  # 空管资讯置顶按钮
    assert_atcinfor_canceltop_alert_text = (By.CLASS_NAME, 'layui-layer-content')  # 空管资讯置顶提示框文本校验
    atcinfor_canceltop_alert_submit_button = (By.CLASS_NAME, 'layui-layer-btn0')  # 空管资讯置顶确定按钮
    atcinfor_canceltop_alert_cancel_button = (By.CLASS_NAME, 'layui-layer-btn1')  # 空管资讯置顶取消按钮
    assert_canceltop_message_text = (By.CLASS_NAME, 'layui-layer-content')  # 空管资讯置顶是否成功文本

    '''删除'''
    atcinfor_delete_button = (By.CLASS_NAME, 'btn red btn-xs btn-outline')  # 空管资讯删除按钮
    assert_atcinfor_delete_alert_text = (By.CLASS_NAME, 'layui-layer-content')  # 空管资讯删除提示框文本校验
    atcinfor_delete_alert_submit_button = (By.CLASS_NAME, 'layui-layer-btn0')  # 空管资讯删除确定按钮
    atcinfor_delete_alert_cancel_button = (By.CLASS_NAME, 'layui-layer-btn1')  # 空管资讯删除取消按钮
    assert_delete_message_text = (By.CLASS_NAME, 'layui-layer-content')  # 空管资讯删除是否成功文本

    def click_atcinfor_tab_close_button(self, openbrowser):
        '''封装点击新增按钮'''
        openbrowser.click_my(AtcInformeationPage.atcinfor_tab_close_button)

    def into_atcinfor_iframe(self, openbrowser):
        '''封装进入iframe'''
        openbrowser.is_iframe(AtcInformeationPage.atcinfor_iframe)

    def into_atcinfor_add_iframe(self, openbrowser):
        '''封装进入iframe'''
        openbrowser.is_iframe(AtcInformeationPage.atcinfor_add_iframe)

    def assert_page_textcontent(self, openbrowser):
        '''封装判断页面文本是否一致,来判断是否进入用户管理页面'''
        res = openbrowser.is_text_in_element(AtcInformeationPage.assert_page_text, "空管资讯")
        return res

    '''封装新增'''

    def click_atcinfor_add_button(self, openbrowser):
        '''封装点击新增按钮'''
        openbrowser.click_my(AtcInformeationPage.atcinfor_add_button)

    def assert_page_add_textcontent(self, openbrowser):
        '''封装判断添加页面文本是否一致'''
        res = openbrowser.is_text_in_element(AtcInformeationPage.assert_page_add_text, "空管资讯新增")
        return res

    def atcinfor_add_title_input(self, openbrowser, input_text):
        '''封装输入文章标题'''
        openbrowser.send_key_my(AtcInformeationPage.atcinfor_add_title, input_text)

    def atcinfor_add_time_select(self, openbrowser):
        '''封装选择时间--date日期框'''
        openbrowser.click_my(AtcInformeationPage.atcinfor_add_time)  # 点击日期框，出现日期选择框
        openbrowser.click_my(AtcInformeationPage.atcinfor_add_time_now_button)  # 点击现在按钮

    def atcinfor_add_order_input(self, openbrowser, input_text):
        '''封装输入排序'''
        openbrowser.send_key_my(AtcInformeationPage.atcinfor_add_order, input_text)

    def atcinfor_add_keyword_input(self, openbrowser, input_text):
        '''封装输入关键字'''
        openbrowser.send_key_my(AtcInformeationPage.atcinfor_add_keyword, input_text)

    def atcinfor_add_description_input(self, openbrowser, input_text):
        '''封装输入文章摘要'''
        openbrowser.send_key_my(AtcInformeationPage.atcinfor_add_description, input_text)

    def atcinfor_add_editor_input(self, openbrowser, input_text):
        '''封装输入文章内容'''
        openbrowser.send_key_my(AtcInformeationPage.atcinfor_add_editor, input_text)

    def atcinfor_add_default_diagram_select(self, openbrowser):
        '''封装选择图库图片'''
        openbrowser.click_my(AtcInformeationPage.atcinfor_add_default_diagram_button)  # 点击在图库选择默认图按钮
        openbrowser.driver.switch_to.frame(0)  # 进入第三层图片iframe
        openbrowser.click_my(AtcInformeationPage.show_photo_album_select)  # 显示相册下拉列表
        openbrowser.random_select_ul(AtcInformeationPage.select_photo_album_li)  # 随机选择相册下拉li
        openbrowser.random_select_pic(AtcInformeationPage.select_photos)  # 随机选择一个photo

    def atcinfor_add_submit_button_click(self, openbrowser):
        '''封装提交按钮点击'''
        openbrowser.click_my(AtcInformeationPage.atcinfor_add_submit_button)

    def atcinfor_add_cancel_button_click(self, openbrowser):
        '''封装取消按钮点击'''
        openbrowser.click_my(AtcInformeationPage.atcinfor_add_cancel_button)

    def atcinfor_add(self, openbrowser, title, order, keyword, description, editor):
        '''封装空管资讯增加'''
        self.atcinfor_add_title_input(openbrowser, title)  # 输入文章标题
        self.atcinfor_add_time_select(openbrowser)  # 选择现在日期
        self.atcinfor_add_order_input(openbrowser, order)  # 输入排序
        self.atcinfor_add_keyword_input(openbrowser, keyword)  # 输入排序
        self.atcinfor_add_description_input(openbrowser, description)  # 输入文章摘要
        self.atcinfor_add_editor_input(openbrowser, editor)  # 输入文章内容
        self.atcinfor_add_default_diagram_select(openbrowser)  # 随机选择图片库图片
        openbrowser.driver.switch_to.parent_frame()  # 切换到第二层新增iframe
        self.atcinfor_add_submit_button_click(openbrowser)  # 点击提交按钮

    def assert_table_number_text(self, openbrowser):
        '''获取空管资讯总数'''
        table_number = openbrowser.get_table_total_number(AtcInformeationPage.assert_table_number)
        return table_number

    '''封装修改'''

    def atcinfor_update_button_click(self, openbrowser):
        '''封装编辑按钮点击'''
        openbrowser.click_my(AtcInformeationPage.atcinfor_update_button)

    def get_table_atcinfor_title_text(self, openbrowser):
        '''获取列表中的文章标题内容'''
        my_text = openbrowser.get_text(AtcInformeationPage.table_atcinfor_title_text)
        return my_text

    def assert_update_table_atcinfor_title_text(self, openbrowser, table_text):
        my_update_atcinfor_title_text = openbrowser.get_vlaue(AtcInformeationPage.atcinfor_update_title_text)
        if my_update_atcinfor_title_text == table_text:
            return True
        else:
            return False

    def assert_page_update_textcontent(self, openbrowser):
        '''封装判断修改页面文本是否一致'''
        res = openbrowser.is_text_in_element(AtcInformeationPage.assert_page_update_text, "空管资讯编辑")
        return res

    def atcinfor_update_submit_button_click(self, openbrowser):
        '''封装修改提交按钮点击'''
        openbrowser.click_my(AtcInformeationPage.atcinfor_update_submit_button)

    def assert_update_message_textcontent(self, openbrowser):
        '''封装判断修改成功'''
        res = openbrowser.is_text_in_element(AtcInformeationPage.assert_update_message_text, "保存成功")
        return res

    '''封装查询'''

    def atcinfor_query_button_click(self, openbrowser):
        '''封装查询按钮点击'''
        openbrowser.click_my(AtcInformeationPage.atcinfor_query_button)

    def atcinfor_query_keyword_input(self, openbrowser, input_text):
        '''封装查询关键字'''
        openbrowser.send_key_my(AtcInformeationPage.atcinfor_query_keyword, input_text)

    def atcinfor_query_startdate_select(self, openbrowser):
        '''封装选择开始时间--date日期框'''
        openbrowser.click_my(AtcInformeationPage.atcinfor_query_startdate)  # 点击日期框，出现日期选择框
        openbrowser.click_my(AtcInformeationPage.atcinfor_query_startdate_now)  # 点击现在按钮

    def atcinfor_query_enddate_select(self, openbrowser):
        '''封装选择结束时间--date日期框'''
        openbrowser.click_my(AtcInformeationPage.atcinfor_query_enddate)  # 点击日期框，出现日期选择框
        openbrowser.click_my(AtcInformeationPage.atcinfor_query_enddate_now)  # 点击现在按钮

    def atcinfor_query(self, openbrowser, keyword):
        '''封装查询'''

        self.atcinfor_query_startdate_select(openbrowser)  # 选择开始日期
        self.atcinfor_query_enddate_select(openbrowser)  # 选择结束日期
        self.atcinfor_query_keyword_input(openbrowser, keyword)  # 输入关键字
        self.atcinfor_query_button_click(openbrowser)  # 点击查询按钮

    '''封装置顶'''

    def atcinfor_top_button_click(self, openbrowser):
        '''封装随机点击置顶'''
        openbrowser.random_button_click(AtcInformeationPage.atcinfor_top_button)  # 随机点击置顶按钮

    def assert_atcinfor_top_alert_textcontent(self, openbrowser):
        '''封装判断页面文本是否一致,来判断是否进入用户管理页面'''
        res = openbrowser.is_text_in_element(AtcInformeationPage.assert_atcinfor_top_alert_text, "确定置顶吗？")
        return res

    def atcinfor_top_alert_submit_button_click(self, openbrowser):
        '''封装随机点击置顶'''
        openbrowser.click_my(AtcInformeationPage.atcinfor_top_alert_submit_button)  # 点击确定按钮

    def assert_top_message_textcontent(self, openbrowser):
        '''封装判断页面文本是否一致,来判断是否进入用户管理页面'''
        res = openbrowser.is_text_in_element(AtcInformeationPage.assert_top_message_text, "置顶成功")
        return res


    '''封装取消置顶'''

    def atcinfor_canceltop_button_click(self, openbrowser):
        '''封装随机点击置顶'''
        openbrowser.random_button_click(AtcInformeationPage.atcinfor_canceltop_button)  # 随机点击置顶按钮

    def assert_atcinfor_canceltop_alert_textcontent(self, openbrowser):
        '''封装判断页面文本是否一致,来判断是否进入用户管理页面'''
        res = openbrowser.is_text_in_element(AtcInformeationPage.assert_atcinfor_canceltop_alert_text, "确定取消置顶吗？")
        return res

    def atcinfor_canceltop_alert_submit_button_click(self, openbrowser):
        '''封装随机点击置顶'''
        openbrowser.click_my(AtcInformeationPage.atcinfor_canceltop_alert_submit_button)  # 点击确定按钮

    def assert_canceltop_message_textcontent(self, openbrowser):
        '''封装判断页面文本是否一致,来判断是否进入用户管理页面'''
        res = openbrowser.is_text_in_element(AtcInformeationPage.assert_canceltop_message_text, "取消置顶成功")
        return res

    '''封装删除'''

    def atcinfor_delete_button_click(self, openbrowser):
        '''封装随机点击删除'''
        openbrowser.random_button_click(AtcInformeationPage.atcinfor_delete_button)  # 随机点击删除按钮

    def assert_atcinfor_delete_alert_textcontent(self, openbrowser):
        '''封装判断页面文本是否一致,来判断是否弹出删除对话框'''
        res = openbrowser.is_text_in_element(AtcInformeationPage.assert_atcinfor_delete_alert_text, "确定删除吗？")
        return res

    def atcinfor_delete_alert_submit_button_click(self, openbrowser):
        '''封装点击确定按钮'''
        openbrowser.click_my(AtcInformeationPage.atcinfor_delete_alert_submit_button)  # 点击确定按钮

    def assert_delete_message_textcontent(self, openbrowser):
        '''封装判断页面文本是否一致,来判断是否删除成功'''
        res = openbrowser.is_text_in_element(AtcInformeationPage.assert_delete_message_text, "删除成功")
        return res