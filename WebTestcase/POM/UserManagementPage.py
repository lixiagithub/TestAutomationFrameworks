# coding = utf-8
# Author:李昰 
# Date：2021/1/13 11:11
from selenium.webdriver.common.by import By
import time
class UserManagementPage():
    user_tab_close_button = (By.XPATH, '/html/body/div[2]/div/div[2]/nav/div/a[2]/i')  # 空管资讯页面关闭
    root_node=(By.XPATH,'// *[ @ id = "treeDemo"]')#党组织列表
    all_node = (By.XPATH,'// *[ @ id = "treeDemo"]/a')#所有节点
    user_iframe=(By.XPATH,'// *[ @ id = "content-main"] / iframe[2]')#用户页面iframe
    assert_page_text = (By.XPATH,'/html/body/div[1]/div/div/div[4]/div/div[1]/div/span[1]')#用户管理列表名
    '''新增'''
    user_add_button =(By.XPATH,'/html/body/div[1]/div/div/div[4]/div/div[2]/div[1]/div[4]')#新增按钮
    assert_page_add_update_text = (By.XPATH,'/html/body/div[1]/div/div/div[3]/div/div/div/span')#用户添加/修改
    administrative_authority_text=(By.XPATH,'//*[@id="myform"]/div/div/div[1]/div/div')#党组织管理权限
    #user_relation_nos=(By.XPATH,'// *[ @ id = "user_relation_nos"]')#选择党员下拉列表隐藏的用于为空校验
    show_party_member_select=(By.XPATH,'//*[@id="myform"]/div/div/div[2]/div/div/span/span[1]')#党委点击显示下拉列表
    #select_party_member_ul = (By.XPATH,'//*[@id="select2-user_relation_nos-results"]')#选择党员下拉列表ul
    select_party_member_li = (By.CLASS_NAME,'select2-results__option')#选择党员下拉列表li
    show_role_select = (By.XPATH, '//*[@id="myform"]/div/div/div[3]/div/div/span/span[1]')  # 选择角色点击显示下拉列表
    #select_role_ul = (By.XPATH, '// *[ @ id = "select2-worker-results"]')  #选择角色下拉列表ul
    select_role_ul_li = (By.CLASS_NAME,'select2-results__option')#选择角色下拉列表li
    remark = (By.XPATH,'//*[@id="maxlength_textarea"]')#备注
    submit_button = (By.XPATH,'//*[@id="btnSave"]')#提交按钮
    cancel_button = (By.XPATH,'//*[@id="myform"]/div/div/div[5]/a')#取消按钮
    assert_table_number = (By.XPATH,'//*[@id="table"]/div[1]/div[2]/div[4]/div[1]/span[1]')#总共多少条数
    div_alert = (By.CLASS_NAME,'layui-layer layui-layer-dialog')#div操作弹出框
    assert_div_alert_text = (By.CLASS_NAME,'layui-layer-content')#新增操作提示框文本
    # assert_div_alert_text = (By.XPATH, '/html/body/div[6]/div[2]')  #新增操作提示框文本
    div_alert_button = (By.CLASS_NAME,'layui-layer-btn0')#操作提示框的确定按钮
    # assert_div_alert_text = (By.XPATH,'/html/body/div[6]/div[2]')#新增操作提示框文本
    # div_alert_button = (By.XPATH,'/html/body/div[6]/div[3]/a')#操作提示框的确定按钮
    navigation_bar_user= (By.XPATH,'/html/body/div[1]/div/div/div[1]/ul/li[2]/a')#导航栏，用户管理
    '''修改'''
    user_update_button = (By.XPATH,'//*[@id="client_table"]/tbody/tr[1]/td[10]/a[1]')#点击第一个编辑按钮
    table_user_administrative_authority_text=(By.XPATH,'//*[@id="client_table"]/tbody/tr[1]/td[7]') #列表中的组织部门
    table_user_party_member_select_text = (By.XPATH,'//*[@id="client_table"]/tbody/tr[1]/td[2]') #列表中的姓名
    table_user_role_select_text = (By.XPATH, '//*[@id="client_table"]/tbody/tr[1]/td[3]')  # 列表中的用户角色
    user_update_administrative_authority_text = (By.CLASS_NAME, 'curSelectedNode')#编辑页面党组织管理权限-回显
    user_update_party_member_select_text=(By.XPATH,'//*[@id="myform"]/div/div/div[2]/div/div/input[1]')#编辑页面选择党员-回显
    user_update_role_select_text = (By.XPATH, '//*[@id="select2-worker-container"]')  # 编辑页面选择角色-回显
    '''查询'''
    user_query_status_select=(By.XPATH,'/html/body/div[1]/div/div/div[4]/div/div[2]/div[1]/div[1]/div/div/span/span[1]/span')#点击显示下拉列表
    user_query_status_ul=(By.XPATH, '//*[@id="select2-status-results"]')#状态ul
    user_query_status_li = (By.XPATH, '//*[@id="select2-status-results"]/li')  # 状态li
    user_query_status_li_text=(By.XPATH, '//*[@id="select2-status-container"]')#获取选择的文本
    user_query_status_li_available = (By.XPATH, '/html/body/span/span/span[2]/ul/li[2]')  # 选择可用
    user_query_status_li_not_available = (By.XPATH, '/html/body/span/span/span[2]/ul/li[3]')  # 选择不可用
    user_query_role_select=(By.XPATH, '/html/body/div[1]/div/div/div[4]/div/div[2]/div[1]/div[2]/div/div/span/span[1]/span')#用户角色
    user_query_role_ul = (By.XPATH, '//*[@id="select2-user_role-results"]')  # 用户角色
    user_query_role_li = (By.XPATH, '//*[@id="select2-user_role-results"]/li')  # 用户角色
    user_query_role_li_text = (By.XPATH, '//*[@id="select2-user_role-container"]')  # 获取选择的文本
    user_query_keyword=(By.XPATH, '//*[@id="user_name"]')#关键词，姓名或党员编号
    user_query_button=(By.XPATH, '/html/body/div[1]/div/div/div[4]/div/div[2]/div[1]/div[5]')#查询按钮
    '''停用'''
    user_block_up=(By.XPATH, '//*[@id="client_table"]/tbody/tr[1]/td[10]/a[2]')#第一个停用按钮
    '''启用'''
    user_start_using = (By.XPATH, '//*[@id="client_table"]/tbody/tr[1]/td[10]/a[2]')  # 第一个启用用按钮


    def click_user_tab_close_button(self, openbrowser):
        '''封装点击tab关闭按钮'''
        openbrowser.click_my(UserManagementPage.user_tab_close_button)

    def click_user_add_button(self,openbrowser):
        '''封装点击新增按钮'''
        openbrowser.click_my(UserManagementPage.user_add_button)

    def into_user_iframe(self,openbrowser):
        '''封装进入iframe'''
        openbrowser.is_iframe(UserManagementPage.user_iframe)

    def assert_page_textcontent(self,openbrowser):
        '''封装判断页面文本是否一致,来判断是否进入用户管理页面'''
        res=openbrowser.is_text_in_element(UserManagementPage.assert_page_text,"用户管理")
        return res

    def assert_page_add_update_textcontent(self,openbrowser):
        '''封装判断添加修改页面文本是否一致'''
        res=openbrowser.is_text_in_element(UserManagementPage.assert_page_add_update_text,"用户添加/修改")
        return res

    def assert_success_textcontent(self,openbrowser):
        '''封装判断添加操作成功文本是否一致'''
        res=openbrowser.is_text_in_element(UserManagementPage.assert_div_alert_text,"操作成功")
        return res

    # def assert_update_success_textcontent(self,openbrowser):
    #     '''封装判断修改操作成功文本是否一致'''
    #     res=openbrowser.is_text_in_element(UserManagementPage.assert_div_alert_text,"操作成功")
    #     return res


    def assert_administrative_authority_text(self,openbrowser,node_text):
        '''封装判断添加页面党组织结构权限是否和树形文本一致'''
        my_administrative_authority_text=openbrowser.get_text(UserManagementPage.administrative_authority_text)
        if my_administrative_authority_text == node_text:
            return True
        else:
            return False

    def assert_update_administrative_authority_text(self,openbrowser,table_text):
        my_update_administrative_authority_text = openbrowser.get_text(UserManagementPage.user_update_administrative_authority_text)
        if my_update_administrative_authority_text == table_text:
            return True
        else:
            return False

    def assert_update_party_member_select_text(self,openbrowser,table_text):
        my_update_party_member_select_text = openbrowser.get_vlaue(UserManagementPage.user_update_party_member_select_text)
        if my_update_party_member_select_text == table_text:
            return True
        else:
            return False

    def assert_update_role_select_text(self, openbrowser, table_text):
        my_update_role_select_text = openbrowser.get_text(UserManagementPage.user_update_role_select_text)
        if my_update_role_select_text == table_text:
            return True
        else:
            return False

    def get_table_user_administrative_authority_text(self,openbrowser):
        my_text=openbrowser.get_text(UserManagementPage.table_user_administrative_authority_text)
        return my_text

    def get_table_user_party_member_select_text(self, openbrowser):
        my_text = openbrowser.get_text(UserManagementPage.table_user_party_member_select_text)
        return my_text

    def get_table_user_role_select_text(self,openbrowser):
        my_text=openbrowser.get_text(UserManagementPage.table_user_role_select_text)
        return my_text

    def assert_alert_persent(self,openbrowser):
        '''封装判断是否存在alert，如果有进入alert'''
        res=openbrowser.is_alert_persent()
        return res

    def assert_alert_text(self,alert_text,node_text):
        '''判断弹出框内容和树形节点内容相同'''
        if alert_text == '您确定要为党组织：{} 新增管理员吗？'.format(node_text):
            return  True
        else:
            return False

    def random_click_node(self,openbrowser):
        '''封装随机点击树形结构中的某个节点'''
        node_text=openbrowser.random_click_node_js()
        return node_text

    def random_select_role(self,openbrowser):
        '''封装党委下拉随即点击'''
        openbrowser.click_my(UserManagementPage.show_role_select)#显示下拉列表
        openbrowser.random_select_ul(UserManagementPage.select_role_ul_li)#随机选择下拉li

    def random_select_party_member(self,openbrowser):
        '''封装党委下拉随即点击'''
        openbrowser.click_my(UserManagementPage.show_party_member_select)#显示下拉列表
        openbrowser.random_select_ul(UserManagementPage.select_party_member_li)#随机选择下拉li

    '''查询'''
    def random_select_query_status(self,openbrowser):
        '''封装查询状态下拉随即点击'''
        openbrowser.click_my(UserManagementPage.user_query_status_select)#显示下拉列表
        openbrowser.random_select_ul(UserManagementPage.user_query_status_li)#随机选择下拉li
        mytext=openbrowser.get_text(UserManagementPage.user_query_status_li_text)#获取文本
        status_text_value = 1
        if mytext == "请选择":
            status_text_value = 2
        elif mytext == "可用":
            status_text_value = 1
        elif mytext == "不可用":
            status_text_value = 0
        return status_text_value

    def random_select_query_role(self,openbrowser):
        '''封装查询角色下拉随即点击'''
        openbrowser.click_my(UserManagementPage.user_query_role_select)#显示下拉列表
        openbrowser.random_select_ul(UserManagementPage.user_query_role_li)#随机选择下拉li
        mytext = openbrowser.get_text(UserManagementPage.user_query_role_li_text)  # 获取文本
        return mytext

    '''封装查询停用'''
    def user_block_up_query(self,openbrowser):
        '''状态下拉选择可用，点击查询，选择停用'''
        openbrowser.click_my(UserManagementPage.user_query_status_select)  # 显示下拉列表
        openbrowser.select_ul_click(UserManagementPage.user_query_status_li_available)# 选择可用
        # ul=openbrowser.driver.find_element_by_xpath('/html/body/span/span/span[2]/ul')# 定位ul可用
        # time.sleep(1)
        # ul.find_element_by_xpath('/html/body/span/span/span[2]/ul/li[2]').click()# 选择可用
        openbrowser.click_my(UserManagementPage.user_query_button)#点击查询按钮

    def user_block_up_click(self,openbrowser):
        openbrowser.click_my(UserManagementPage.user_block_up)  # 点击停用按钮

    '''封装查询启用'''
    def user_start_using_query(self,openbrowser):
        '''状态下拉选择不可用，点击查询'''
        openbrowser.click_my(UserManagementPage.user_query_status_select)  # 显示下拉列表
        openbrowser.click_my(UserManagementPage.user_query_status_li_not_available)# 选择不可用
        # time.sleep(1)
        # ul = openbrowser.driver.find_element_by_xpath('/html/body/span/span/span[2]/ul')  # 定位ul
        # ul.find_element_by_xpath('/html/body/span/span/span[2]/ul/li[3]').click()  # 选择不可用
        openbrowser.click_my(UserManagementPage.user_query_button)  # 点击查询按钮


    def user_start_using_click(self,openbrowser):
        openbrowser.click_my(UserManagementPage.user_start_using)  # 点击启用按钮

    def assert_block_up_textcontent(self,openbrowser):
        '''封装判断停用文本'''
        res=openbrowser.is_text_in_element(UserManagementPage.assert_div_alert_text,"确认停用")
        return res

    def assert_start_using_textcontent(self,openbrowser):
        '''封装判断启用文本'''
        res=openbrowser.is_text_in_element(UserManagementPage.assert_div_alert_text,"确认启用")
        return res

    def user_query_keyword_input(self,openbrowser,input_text):
        '''封装查询输入关键字'''
        openbrowser.send_key_my(UserManagementPage.user_query_keyword,input_text)

    def user_query_button_click(self,openbrowser):
        '''封装查询按钮点击'''
        openbrowser.click_my(UserManagementPage.user_query_button)

    # def user_query(self,openbrowser):
    #     '''封装查询'''
    #     self.random_select_query_state(openbrowser)#随机


    def remark_input(self,openbrowser,input_text):
        '''封装输入备注'''
        openbrowser.send_key_my(UserManagementPage.remark,input_text)

    def submit_button_click(self,openbrowser):
        '''封装提交按钮点击'''
        openbrowser.click_my(UserManagementPage.submit_button)

    def cancel_button_click(self,openbrowser):
        '''封装取消按钮点击'''
        openbrowser.click_my(UserManagementPage.cancel_button)

    def div_alert_button_click(self,openbrowser):
        '''封装操作提示框中的确定按钮点击'''
        openbrowser.click_my(UserManagementPage.div_alert_button)

    def navigation_bar_user_click(self,openbrowser):
        '''封装导航栏中的用户管理'''
        openbrowser.click_my(UserManagementPage.navigation_bar_user)

    def user_update_button_click(self, openbrowser):
        '''封装用户管理编辑按钮'''
        openbrowser.click_my(UserManagementPage.user_update_button)

    def execute_js_div_alert_button_click(self,openbrowser):
        '''封装js点击'''
        openbrowser.execute_js("document.getElementsByClassName('layui-layer-btn0')[0].click()")

    def assert_div_alert(self,openbrowser):
        '''查看div弹框是否存在'''
        openbrowser.element_visible_times(UserManagementPage.div_alert)

    def execut_js_div_alert(self,openbrowser):
        '''获取div'''
        return openbrowser.execut_js_loc(UserManagementPage.div_alert)

    # def assert_new_window_is_opened(self,openbrowser,current_handles):
    #     '''确定是否有新窗口，如果有切换到新窗口'''
    #     res=openbrowser.is_new_window_is_opened(current_handles)
    #     if res:
    #         openbrowser.switch_to_window(openbrowser.window_handles[-1])
    #         return True
    #     else:
    #         return False

    def user_add(self,openbrowser,remark):
        '''封装用户增加'''
        self.random_select_party_member(openbrowser)#选择党员
        self.random_select_role(openbrowser)#选择角色
        self.remark_input(openbrowser,remark)#填写备注
        self.submit_button_click(openbrowser)#点击提交按钮

    def assert_table_number_text(self,openbrowser):
        '''获取用户总数'''
        table_number=openbrowser.get_table_total_number(UserManagementPage.assert_table_number)
        return table_number