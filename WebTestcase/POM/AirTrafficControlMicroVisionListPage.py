# coding = utf-8
# Author:李昰 
# Date：2021/5/19 13:49

from selenium.webdriver.common.by import By

class AirTrafficControlMicroVisionListPage():
    atcmvlinfor_tab_close_button = (By.XPATH, '/html/body/div[2]/div/div[2]/nav/div/a[2]/i')  # 空管微视页面关闭
    atcmvlinfor_iframe = (By.XPATH, '//*[@id="content-main"]/iframe[2]')  # 空管微视页面iframe
    assert_atcmvlinfor_page_text = (By.XPATH, '/html/body/div[1]/div/div/div[3]/div[1]/div/div[1]/div/span')  # 空管微视列表
    atcmvlinfor_classify = (By.XPATH, '//*[@id="treeDemo"]/li/ul/li')  # 左侧树形空管微视分类
    assert_atcmvlinfor_table_number = (By.XPATH, '//*[@id="download_zip"]/div[1]/div[2]/div[4]/div[1]/span[1]')  # 总共多少条数

    '''新增'''
    atcmvlinfor_add_button = (By.XPATH, '//*[@id="addedu"]')  # 新增按钮
    assert_page_add_text = (By.CLASS_NAME, 'layui-layer-title')  # 空管微视新增文本title校验
    atcmvlinfor_add_title = (By.XPATH, '//*[@id="material_title"]')  # 空管微视新增名称
    atcmvlinfor_add_time = (By.XPATH, '//*[@id="t1"]')  # 空管微视新增视频时长
    assert_atcmvlinfor_add_time = (By.XPATH, '//*[@id="forms"]/div/div[4]/label')  # 判断是否存在视频时长
    atcmvlinfor_add_vedio = (By.XPATH, '//*[@id="material_vedio"]')  # 空管微视新增视频地址
    atcmvlinfor_add_size = (By.XPATH, '//*[@id="video_size"]')  # 空管微视新增视频大小
    atcmvlinfor_add_editor = (By.XPATH, '//*[@id="editor"]')  # 空管微视新增内容
    atcmvlinfor_add_choosefile_button = (By.XPATH, '//*[@id="forms"]/div/div[7]/div/div/div/a[1]')  # 空管微视新增缩略图点击选择文件按钮
    atcmvlinfor_add_default_diagram_button = (
        By.XPATH, "//*[text()='在图库选择默认图']")  # 空管微视新增缩略图在图库选择默认图
    atcmvlinfor_add_default_diagram_iframe = (By.XPATH, '/html/body/div[6]')  # 空管微视新增缩略图iframe
    show_photo_album_select = (By.XPATH, '//*[@id="forms"]/div/div/div[1]/div/div/div/span')  # 相册下拉
    select_photo_album_ul = (By.XPATH, '//*[@id="select2-gallery-results"]')  # 相册ul
    select_photo_album_li = (By.CLASS_NAME, 'select2-results__option')  # 相册li
    select_photos = (By.CLASS_NAME, 'cbp-item')  # 选择全部photo
    select_photo_buttons = (
        By.CLASS_NAME, 'cbp-l-caption-buttonLeft btn red uppercase btn red uppercase')  # 选择photo的所有选择按钮
    atcmvlinfor_add_submit_button = (By.XPATH, "//*[text()='提交']")  # 空管微视新增下发按钮
    atcmvlinfor_add_cancel_button = (By.XPATH, "//*[text()='取消']")  # 空管微视新增取消按钮
    assert_atcmvlinfor_add_message_text = (By.CLASS_NAME, 'layui-layer-content')  # 空管微视新增是否成功文本

    '''查询'''
    atcmvlinfor_query_title = (By.XPATH, '//*[@id="material_title"]')  # 空管微视查询名称
    atcmvlinfor_query_button = (By.XPATH, "/html/body/div[1]/div/div/div[3]/div[2]/div/div[2]/div[1]/div/div/div[2]/button[2]")  # 空管微视查询按钮
    atcmvlinfor_query_empty = (By.XPATH, '//*[@id="client_table"]/tbody/tr/td')  # 空管微视查询为空

    '''修改'''
    atcmvlinfor_update_button = (By.XPATH, '//*[@id="client_table"]/tbody/tr/td[9]/a[2]')  # 点击第一个编辑按钮
    atcmvlinfor_update_title = (By.XPATH, '//*[@id="material_title"]')  # 编辑页面名称-回显
    atcmvlinfor_update_editor = (By.XPATH, '//*[@id="editor"]')  # 编辑页面出版社-回显
    assert_atcmvlinfor_page_update_text = (By.CLASS_NAME, 'layui-layer-title')  # 空管微视修改文本title校验
    atcmvlinfor_update_submit_button = (By.XPATH, "//*[text()='提交']")  # 空管微视修改提交按钮
    atcmvlinfor_update_cancel_button = (By.XPATH, "//*[text()='取消']")  # 空管微视修改取消按钮
    assert_atcmvlinfor_update_message_text = (By.CLASS_NAME, 'layui-layer-content')  # 空管微视修改是否成功文本

    '''详情'''
    atcmvlinfor_detail_button = (By.XPATH, '//*[@id="client_table"]/tbody/tr/td[9]/a[1]')  # 空管微视详情按钮
    assert_atcmvlinfor_page_detail_text = (By.CLASS_NAME, 'layui-layer-title')  # 空管微视详情页文本title校验
    atcmvlinfor_detail_title = (By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div[1]/span')  # 空管微视标题名称
    atcmvlinfor_detail_editor = (By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[2]/div/div/div[2]/p')  # 空管微视内容
    atcmvlinfor_return_button = (By.XPATH, "//*[text()='返回']")  # 空管微视详情页返回按钮

    '''置顶'''
    atcmvlinfor_top_button = (By.XPATH, '//*[@id="client_table"]/tbody/tr/td[9]/a[4]')  # 空管微视置顶按钮
    assert_atcmvlinfor_top_alert_text = (By.CLASS_NAME, 'layui-layer-content')  # 空管微视置顶提示框文本校验
    atcmvlinfor_top_alert_submit_button = (By.CLASS_NAME, 'layui-layer-btn0')  # 空管微视置顶确定按钮
    atcmvlinfor_top_alert_cancel_button = (By.CLASS_NAME, 'layui-layer-btn1')  # 空管微视置顶取消按钮
    assert_atcmvlinfor_top_message_text = (By.CLASS_NAME, 'layui-layer-content')  # 空管微视置顶是否成功文本

    '''取消置顶'''
    atcmvlinfor_canceltop_button = (By.XPATH, '//*[@id="client_table"]/tbody/tr/td[9]/a[4]')  # 空管微视取消置顶按钮
    assert_atcmvlinfor_canceltop_alert_text = (By.CLASS_NAME, 'layui-layer-content')  # 空管微视取消置顶提示框文本校验
    atcmvlinfor_canceltop_alert_submit_button = (By.CLASS_NAME, 'layui-layer-btn0')  # 空管微视取消置顶确定按钮
    atcmvlinfor_canceltop_alert_cancel_button = (By.CLASS_NAME, 'layui-layer-btn1')  # 空管微视取消置顶取消按钮
    assert_atcmvlinfor_canceltop_message_text = (By.CLASS_NAME, 'layui-layer-content')  # 空管微视取消置顶是否成功文本

    '''删除'''
    atcmvlinfor_delete_button = (By.XPATH, '//*[@id="client_table"]/tbody/tr/td[9]/a[3]')  # 空管微视删除按钮
    assert_atcmvlinfor_delete_alert_text = (By.CLASS_NAME, 'layui-layer-content')  # 空管微视删除提示框文本校验
    atcmvlinfor_delete_alert_submit_button = (By.CLASS_NAME, 'layui-layer-btn0')  # 空管微视删除确定按钮
    atcmvlinfor_delete_alert_cancel_button = (By.CLASS_NAME, 'layui-layer-btn1')  # 空管微视删除取消按钮
    assert_atcmvlinfor_delete_message_text = (By.CLASS_NAME, 'layui-layer-content')  # 空管微视删除是否成功文本

    def click_atcmvlinfor_tab_close_button(self, openbrowser):
        '''封装点击关闭按钮'''
        openbrowser.click_my(AirTrafficControlMicroVisionListPage.atcmvlinfor_tab_close_button)

    def into_atcmvlinfor_iframe(self, openbrowser):
        '''封装进入iframe'''
        openbrowser.is_iframe(AirTrafficControlMicroVisionListPage.atcmvlinfor_iframe)

    def assert_atcmvlinfor_page_textcontent(self, openbrowser):
        '''封装判断页面文本是否一致,来判断是否进入空管微视页面'''
        res = openbrowser.is_text_in_element(AirTrafficControlMicroVisionListPage.assert_atcmvlinfor_page_text, "空管微视列表")
        return res

    def select_atcmvlinfor_classify(self, openbrowser,soncol_name):
        '''封装随机选择左侧树形空管微视分类'''
        res = openbrowser.select_click_node(AirTrafficControlMicroVisionListPage.atcmvlinfor_classify,soncol_name)
        return res

    def assert_atcmvlinfor_table_number_text(self, openbrowser):
        '''获取空管微视总数'''
        table_number = openbrowser.get_table_total_number(AirTrafficControlMicroVisionListPage.assert_atcmvlinfor_table_number)
        return table_number

    '''封装新增'''

    def click_atcmvlinfor_add_button(self, openbrowser):
        '''封装点击新增按钮'''
        openbrowser.click_my(AirTrafficControlMicroVisionListPage.atcmvlinfor_add_button)

    def assert_atcmvlinfor_page_add_textcontent(self, openbrowser,col_name):
        '''封装判断添加页面文本是否一致'''
        res = openbrowser.is_text_in_element(AirTrafficControlMicroVisionListPage.assert_page_add_text, "{}新增".format(col_name))
        return res

    def assert_atcmvlinfor_add_time_textcontent(self, openbrowser):
        '''封装判断页面文本是否一致,来判断是否存在'''
        res = openbrowser.is_text_in_element(AirTrafficControlMicroVisionListPage.assert_atcmvlinfor_add_time,
                                             "视频时长：")
        return res

    def atcmvlinfor_add_title_input(self, openbrowser, input_text):
        '''封装输入名称'''
        openbrowser.send_key_my(AirTrafficControlMicroVisionListPage.atcmvlinfor_add_title, input_text)

    def atcmvlinfor_add_time_input(self, openbrowser, input_text):
        '''封装输入视频时长'''
        openbrowser.send_key_my(AirTrafficControlMicroVisionListPage.atcmvlinfor_add_time, input_text)

    def atcmvlinfor_add_vedio_input(self, openbrowser, input_text):
        '''封装输入视频地址'''
        openbrowser.send_key_my(AirTrafficControlMicroVisionListPage.atcmvlinfor_add_vedio, input_text)

    def atcmvlinfor_add_size_input(self, openbrowser, input_text):
        '''封装输入视频大小'''
        openbrowser.send_key_my(AirTrafficControlMicroVisionListPage.atcmvlinfor_add_size, input_text)

    def atcmvlinfor_add_editor_input(self, openbrowser, input_text):
        '''封装输入内容'''
        openbrowser.send_key_my(AirTrafficControlMicroVisionListPage.atcmvlinfor_add_editor, input_text)

    def atcmvlinfor_add_default_diagram_select(self, openbrowser):
        '''封装选择图库图片'''
        openbrowser.click_my(AirTrafficControlMicroVisionListPage.atcmvlinfor_add_default_diagram_button)  # 点击在图库选择默认图按钮
        openbrowser.driver.switch_to.frame(0)  # 进入第三层图片iframe
        openbrowser.click_my(AirTrafficControlMicroVisionListPage.show_photo_album_select)  # 显示相册下拉列表
        openbrowser.random_select_ul(AirTrafficControlMicroVisionListPage.select_photo_album_li)  # 随机选择相册下拉li
        openbrowser.random_select_pic(AirTrafficControlMicroVisionListPage.select_photos)  # 随机选择一个photo

    def atcmvlinfor_add_submit_button_click(self, openbrowser):
        '''封装提交按钮点击'''
        openbrowser.click_my(AirTrafficControlMicroVisionListPage.atcmvlinfor_add_submit_button)

    def atcmvlinfor_add_cancel_button_click(self, openbrowser):
        '''封装取消按钮点击'''
        openbrowser.click_my(AirTrafficControlMicroVisionListPage.atcmvlinfor_add_cancel_button)

    def atcmvlinfor_add(self, openbrowser, name, time, vedio,size,editor,isvedio):
        '''封装空管微视视频增加'''
        openbrowser.driver.switch_to.frame(0)  # 进入第二层新增iframe
        self.atcmvlinfor_add_title_input(openbrowser, name)  # 输入视频名称
        if isvedio=='1':
            self.atcmvlinfor_add_time_input(openbrowser, time)  # 输入视频时长
            self.atcmvlinfor_add_vedio_input(openbrowser, vedio)  # 输入视频地址
            self.atcmvlinfor_add_size_input(openbrowser, size)  # 输入视频大小
        else:
            self.atcmvlinfor_add_editor_input(openbrowser, editor)
        self.atcmvlinfor_add_default_diagram_select(openbrowser)  # 随机选择图片库图片
        openbrowser.driver.switch_to.parent_frame()  # 切换到第二层新增iframe
        self.atcmvlinfor_add_submit_button_click(openbrowser)  # 点击提交按钮

    def assert_atcmvlinfor_add_message_textcontent(self, openbrowser):
        '''封装判断新增成功'''
        res = openbrowser.is_text_in_element(AirTrafficControlMicroVisionListPage.assert_atcmvlinfor_add_message_text, "保存成功")
        return res

    '''封装查询'''

    def atcmvlinfor_query_button_click(self, openbrowser):
        '''封装查询按钮点击'''
        openbrowser.click_my(AirTrafficControlMicroVisionListPage.atcmvlinfor_query_button)

    def atcmvlinfor_query_title_input(self, openbrowser, input_text):
        '''封装查询名称'''
        openbrowser.send_key_my(AirTrafficControlMicroVisionListPage.atcmvlinfor_query_title, input_text)

    def atcmvlinfor_query(self, openbrowser, title):
        '''封装查询'''
        self.atcmvlinfor_query_title_input(openbrowser, title)  # 输入关键字
        self.atcmvlinfor_query_button_click(openbrowser)  # 点击查询按钮

    '''封装修改'''

    def atcmvlinfor_update_button_click(self, openbrowser):
        '''封装编辑按钮点击'''
        openbrowser.click_my(AirTrafficControlMicroVisionListPage.atcmvlinfor_update_button)

    def get_atcmvlinfor_update_title(self, openbrowser):
        '''获取修改页面的标题'''
        my_text = openbrowser.get_vlaue(AirTrafficControlMicroVisionListPage.atcmvlinfor_update_title)
        return my_text

    def get_atcmvlinfor_update_editor(self, openbrowser):
        '''获取修改页面的内容'''
        my_text = openbrowser.get_text(AirTrafficControlMicroVisionListPage.atcmvlinfor_update_editor)
        return my_text


    def assert_atcmvlinfor_update_textcontent(self, openbrowser, atcmv_name, atcmv_editor):
        '''封装编辑内容检查'''
        openbrowser.driver.switch_to.frame(0)  # 进入第二层修改iframe
        page_atcmv_name = self.get_atcmvlinfor_update_title(openbrowser)
        page_atcmv_editor = self.get_atcmvlinfor_update_editor(openbrowser)
        message = "编辑回显内容："
        flag = True
        if page_atcmv_name == atcmv_name:
            message += "页面空管微视名称{0}与新增的数据{1}一致".format(page_atcmv_name, atcmv_name)
        else:
            message += "页面空管微视名称{0}与新增的数据{1}不一致".format(page_atcmv_name, atcmv_name)
            flag = False
        if page_atcmv_editor == atcmv_editor:
            message += ",页面空管微视内容{0}与新增的数据{1}一致".format(page_atcmv_editor, atcmv_editor)
        else:
            message += ",页面空管微视内容{0}与新增的数据{1}不一致".format(page_atcmv_editor, atcmv_editor)
            flag = False
        return flag, message

    def assert_atcmvlinfor_page_update_textcontent(self, openbrowser,col_name):
        '''封装判断修改页面文本是否一致'''
        res = openbrowser.is_text_in_element(AirTrafficControlMicroVisionListPage.assert_atcmvlinfor_page_update_text, "{}编辑".format(col_name))
        return res

    def atcmvlinfor_update_submit_button_click(self, openbrowser):
        '''封装修改提交按钮点击'''
        openbrowser.click_my(AirTrafficControlMicroVisionListPage.atcmvlinfor_update_submit_button)

    def assert_atcmvlinfor_update_message_textcontent(self, openbrowser):
        '''封装判断修改成功'''
        res = openbrowser.is_text_in_element(AirTrafficControlMicroVisionListPage.assert_atcmvlinfor_update_message_text, "保存成功")
        return res

    '''封装详情'''

    def atcmvlinfor_detail_button_click(self, openbrowser):
        '''封装详情按钮点击'''
        openbrowser.click_my(AirTrafficControlMicroVisionListPage.atcmvlinfor_detail_button)

    def assert_atcmvlinfor_page_detail_textcontent(self, openbrowser,col_name):
        '''封装判断详情页面文本是否一致'''
        res = openbrowser.is_text_in_element(AirTrafficControlMicroVisionListPage.assert_atcmvlinfor_page_detail_text, "{}详情".format(col_name))
        return res

    def get_detail_atcmvlinfor_title(self, openbrowser):
        '''封装获取公示通告标题'''
        my_text = openbrowser.get_text(AirTrafficControlMicroVisionListPage.atcmvlinfor_detail_title)
        return my_text

    def get_detail_atcmvlinfor_editor(self, openbrowser):
        '''封装获取公示通告内容'''
        my_text = openbrowser.get_text(AirTrafficControlMicroVisionListPage.atcmvlinfor_detail_editor)
        return my_text

    def assert_atcmvlinfor_detail_textcontent(self, openbrowser , atcmv_name, atcmv_editor):
        '''封装详情内容检查'''
        openbrowser.driver.switch_to.frame(0)  # 进入第二层修改iframe
        page_atcmv_name = self.get_detail_atcmvlinfor_title(openbrowser)
        page_atcmv_editor = self.get_detail_atcmvlinfor_editor(openbrowser)
        message = "详情内容："
        flag = True
        if page_atcmv_name == atcmv_name:
            message += "页面空管微视名称{0}与新增的数据{1}一致".format(page_atcmv_name, atcmv_name)
        else:
            message += "页面空管微视名称{0}与新增的数据{1}不一致".format(page_atcmv_name, atcmv_name)
            flag = False
        if page_atcmv_editor == atcmv_editor:
            message += ",页面空管微视内容{0}与新增的数据{1}一致".format(page_atcmv_editor, atcmv_editor)
        else:
            message += ",页面空管微视内容{0}与新增的数据{1}不一致".format(page_atcmv_editor, atcmv_editor)
            flag = False
        return flag, message

    def atcmvlinfor_detail_return_click(self, openbrowser):
        '''封装详情返回按钮点击'''
        openbrowser.click_my(AirTrafficControlMicroVisionListPage.atcmvlinfor_return_button)

    '''封装置顶'''

    def atcmvlinfor_top_button_click(self, openbrowser):
        '''封装点击置顶'''
        openbrowser.click_my(AirTrafficControlMicroVisionListPage.atcmvlinfor_top_button)  # 点击置顶按钮

    def assert_atcmvlinfor_top_alert_textcontent(self, openbrowser):
        '''封装判断页面文本是否一致,来判断弹出置顶对话框'''
        res = openbrowser.is_text_in_element(AirTrafficControlMicroVisionListPage.assert_atcmvlinfor_top_alert_text, "确定置顶吗？")
        return res

    def atcmvlinfor_top_alert_submit_button_click(self, openbrowser):
        '''封装点击确定'''
        openbrowser.click_my(AirTrafficControlMicroVisionListPage.atcmvlinfor_top_alert_submit_button)  # 点击确定按钮

    def assert_atcmvlinfor_top_message_textcontent(self, openbrowser):
        '''封装判断页面文本是否一致,来判断置顶成功'''
        res = openbrowser.is_text_in_element(AirTrafficControlMicroVisionListPage.assert_atcmvlinfor_top_message_text, "置顶成功")
        return res

    '''封装取消置顶'''

    def atcmvlinfor_canceltop_button_click(self, openbrowser):
        '''封装点击取消置顶'''
        openbrowser.click_my(AirTrafficControlMicroVisionListPage.atcmvlinfor_canceltop_button)  # 点击取消置顶按钮

    def assert_atcmvlinfor_canceltop_alert_textcontent(self, openbrowser):
        '''封装判断页面文本是否一致,来判断是否弹出取消置顶对话框'''
        res = openbrowser.is_text_in_element(AirTrafficControlMicroVisionListPage.assert_atcmvlinfor_canceltop_alert_text, "确定取消置顶吗？")
        return res

    def atcmvlinfor_canceltop_alert_submit_button_click(self, openbrowser):
        '''封装点击确定按钮'''
        openbrowser.click_my(AirTrafficControlMicroVisionListPage.atcmvlinfor_canceltop_alert_submit_button)  # 点击确定按钮

    def assert_atcmvlinfor_canceltop_message_textcontent(self, openbrowser):
        '''封装判断页面文本是否一致,来判断取消置顶成功'''
        res = openbrowser.is_text_in_element(AirTrafficControlMicroVisionListPage.assert_atcmvlinfor_canceltop_message_text, "取消置顶成功")
        return res

    '''删除'''

    def atcmvlinfor_delete_button_click(self, openbrowser):
        '''封装点击删除按钮'''
        openbrowser.click_my(AirTrafficControlMicroVisionListPage.atcmvlinfor_delete_button)  # 点击删除按钮

    def assert_atcmvlinfor_delete_alert_textcontent(self, openbrowser):
        '''封装判断页面文本是否一致,来判断是否弹出删除对话框'''
        res = openbrowser.is_text_in_element(AirTrafficControlMicroVisionListPage.assert_atcmvlinfor_delete_alert_text, "确定删除吗？")
        return res

    def atcmvlinfor_delete_alert_submit_button_click(self, openbrowser):
        '''封装点击确定'''
        openbrowser.click_my(AirTrafficControlMicroVisionListPage.atcmvlinfor_delete_alert_submit_button)  # 点击确定按钮

    def assert_atcmvlinfor_delete_message_textcontent(self, openbrowser):
        '''封装判断页面文本是否一致,来判断是否删除成功'''
        res = openbrowser.is_text_in_element(AirTrafficControlMicroVisionListPage.assert_atcmvlinfor_delete_message_text, "删除成功")
        return res

