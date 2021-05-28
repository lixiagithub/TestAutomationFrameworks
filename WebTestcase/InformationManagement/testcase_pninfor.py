# coding = utf-8
# Author:李昰 
# Date：2021/5/10 14:31

from WebTestcase.POM.Menu import Menu
from WebTestcase.POM.PublicNotificationPage import PublicNotificationPage
import pytest
from log.log import logger
from untils import tool
from untils.op_mysql import execute_web  # 数据库连接
import time

class TestPninfor(PublicNotificationPage, Menu):
    def setup_class(self):  # 每个类执行前执行一次
        self.pn_name = tool.random_GBK2312(10)
        self.pn_editor = tool.generate_random_str(100)

    @pytest.fixture(scope='module')  # 每个函数可以调用的变量
    def global_data(self):
        '''
        pninfor_organization:公示通报对应组织
        :return: 
        '''
        return {'pninfor_organization': ''}

    @pytest.fixture(scope="class")
    def test_into_pninforpage(self, login):
        '''进入公示通报管理页面'''
        if login:
            '''用例：登录之后，点击资讯管理，点击公示通报，进入公示通报页面'''
            try:
                # 退出iframe
                login.switch_to_default_iframe()
                # 进入公示通报管理页面
                self.into_pninfor_page(login)
                # 定位iframe,并且进入iframe
                self.into_pninfor_iframe(login)
                # 在公示通报页面，查找公示通报验证信息
                if self.assert_page_textcontent(login):
                    logger.info('进入公示通报页面成功')
                    yield login
                    assert True, '进入公示通报页面成功'
                    print('所有类的用例执行完毕,执行后置操作')
                    login.switch_to_default_iframe()  # 退出iframe
                    self.click_pninfor_tab_close_button(login)  # 点击tab关闭按钮
                    logger.info("关闭公示通报tab")
                    self.click_information_management(login)  # 点击咨询管理，收回下拉菜单
                    logger.info("点击咨询管理，收回下拉菜单")
                else:
                    yield False
                    logger.info('进入公示通报页面失败')
                    assert False, '进入公示通报页面失败'

            except Exception as  e:
                logger.info('进入公示通报页面失败')
                assert False, '进入公示通报页面失败'

    def test_add_pninfor(self, test_into_pninforpage,global_data):
        '''新增'''
        if test_into_pninforpage:
            old_number = self.assert_table_number_text(test_into_pninforpage)  # 获取新增前的总数
            logger.info('新增前总数{}'.format(old_number))
            self.click_pninfor_add_button(test_into_pninforpage)  # 点击新增按钮
            if self.assert_page_add_textcontent(test_into_pninforpage):  # 判断是否打开新增界面
                logger.info('进入公示通报添加界面成功')
                # test_into_pninforpage.driver.switch_to.frame(0)  # 进入第二层新增iframe
                global_data['pninfor_organization'] = self.pninfor_add(test_into_pninforpage, self.pn_name,self.pn_editor)  # 新增公示通报
                logger.info('执行新增操作成功,对应组织:{}'.format(global_data['pninfor_organization']))
                # self.into_pninfor_iframe(test_into_pninforpage)  # 新增之后切换到公示通报iframe
                new_number = self.assert_table_number_text(test_into_pninforpage)  # 添加后获取数据总数
                # 验证是否添加成功
                if eval(new_number) == eval(old_number) + 1:
                    logger.info('公示通报信息增加前总数是{0}，信息增加后总数是{1},新增成功'.format(old_number, new_number))
                    assert True, '新增成功'
                else:
                    test_into_pninforpage.switch_to_default_iframe()  # 退出iframe
                    self.menu_public_notification_double_click(test_into_pninforpage)  # 点击导航栏，重置
                    logger.info('公示通报信息增加前总数是{0}，信息增加后总数是{1},新增失败'.format(old_number, new_number))
                    assert False, '新增失败'
            else:
                test_into_pninforpage.switch_to_default_iframe()# 退出iframe
                self.menu_public_notification_double_click(test_into_pninforpage)  # 点击导航栏，重置
                logger.info('进入公示通报添加界面失败')
                assert False, '进入公示通报添加界面失败'
        else:
            logger.info('进入公示通报页面失败,无法进行添加')
            assert False, '进入公示通报页面失败,无法进行添加'

    #@pytest.mark.dependency(name="test_query_pninfor")
    @pytest.fixture(scope="function")
    def test_query_pninfor(self, test_into_pninforpage):
        '''查询'''
        if test_into_pninforpage:  # 进入公示通报界面
            test_into_pninforpage.switch_to_default_iframe()  # 退出iframe
            self.menu_public_notification_double_click(test_into_pninforpage)  # 点击导航栏，重置
            self.into_pninfor_iframe(test_into_pninforpage)# 定位iframe,并且进入iframe
            self.pninfor_query(test_into_pninforpage, self.pn_name)  # 查询公示通报
            logger.info('点击了查询按钮')
            time.sleep(2)
            table_number_text = self.assert_table_number_text(test_into_pninforpage)
            query_str = "SELECT * FROM `sp_pa_article` WHERE `pa_title` LIKE '" + self.pn_name + "' ORDER BY update_time desc LIMIT 0,10 "
            db_query_res = execute_web(query_str)
            if int(table_number_text) == len(db_query_res):
                logger.info('table结果数{0}：数据库查询结果数{1}'.format(table_number_text, len(db_query_res)))  # 获取查询数量
                logger.info('公示通报查询成功')
                yield test_into_pninforpage
                assert True,'公示通报查询正确：table结果数{0}：数据库查询结果数{1}'.format(table_number_text,len(db_query_res))
            else:
                logger.info('公示通报查询失败')
                yield False
                assert False, '公示通报查询失败：table结果数{0}：数据库查询结果数{1}'.format(table_number_text,len(db_query_res))
        else:
            logger.info('没有进入公示通报界面，不执行查询用例')
            assert False, '没有进入公示通报界面，不执行查询用例'

    #@pytest.mark.dependency(depends=["test_query_pninfor"])
    def test_update_pninfor(self, test_query_pninfor,global_data):
        '''修改'''
        if test_query_pninfor:  # 已经查询
            self.pninfor_update_button_click(test_query_pninfor)  # 点击编辑按钮
            if self.assert_page_update_textcontent(test_query_pninfor):  # 判断是否打开修改界面
                logger.info('进入了公示通报编辑页面')
                message = self.assert_update_textcontent(test_query_pninfor, self.pn_name, self.pn_editor,
                                                         global_data['pninfor_organization'])  # 校验详情信息
                if message[0]:
                    logger.info(message[1])
                    self.pninfor_update_submit_button_click(test_query_pninfor)  # 不修改任何内容，直接提交
                    if self.assert_update_message_textcontent(test_query_pninfor):  # 判断是否修改成功
                        logger.info('公示通报编辑成功')
                        assert True, '公示通报编辑成功'
                    else:
                        logger.info('公示通报编辑失败')
                        assert False, '公示通报编辑失败'
                else:
                    logger.info(message[1])
                    assert False, message[1]
            else:
                logger.info('进入公示通报修改界面失败')
                assert False, '进入公示通报修改界面失败'
        else:
            logger.info('没有执行查询，不执行公示通报编辑用例')
            assert False, '没有执行查询，不执行公示通报编辑用例'

    def test_detail_pninfor(self, test_query_pninfor, global_data):
        '''详情'''
        if test_query_pninfor:  # 已经查询
            self.pninfor_detail_button_click(test_query_pninfor)  # 点击详情按钮
            logger.info('点击了详情按钮')
            if self.assert_page_detail_textcontent(test_query_pninfor):  # 判断是否打开详情界面
                logger.info('进入了公示通报详情页面')
                message = self.assert_detail_textcontent(test_query_pninfor, self.pn_name, self.pn_editor,global_data['pninfor_organization'])#校验详情信息
                if message[0]:
                    self.pninfor_detail_return_click(test_query_pninfor)  # 点击返回按钮
                    logger.info(message[1])
                    assert True, message[1]
                else:
                    logger.info(message[1])
                    assert False, message[1]
            else:
                logger.info('进入公示通报详情界面失败')
                assert False, '进入公示通报详情界面失败'
        else:
            logger.info('没有执行查询，不执行查看详情用例')
            assert False, '没有执行查询，不执行查看详情用例'
            
    def test_top_pninfor(self, test_query_pninfor):
        '''置顶'''
        if test_query_pninfor:  #进入查询
            self.pninfor_top_button_click(test_query_pninfor)  #点击一个置顶按钮
            if self.assert_pninfor_top_alert_textcontent(test_query_pninfor):  #判断是否弹出置顶对话框
                logger.info('已经弹出置顶对话框')
                self.pninfor_top_alert_submit_button_click(test_query_pninfor)  #点击确定按钮
                if self.assert_top_message_textcontent(test_query_pninfor):  #判断是否置顶成功
                    logger.info('公示通报置顶成功')
                    assert True,'公示通报置顶成功'
                else:
                    logger.info('公示通报置顶失败')
                    assert False, '公示通报置顶失败'
            else:
                logger.info('没有弹出置顶对话框')
                assert False, '没有弹出置顶对话框'
        else:
            logger.info('没有进入公示通报界面，不执行置顶用例')
            assert False, '没有进入公示通报界面，不执行置顶用例'

    def test_topcancel_infor(self, test_query_pninfor):
        '''取消置顶'''
        if test_query_pninfor:  #进入公示通报界面
            time.sleep(2)
            self.pninfor_canceltop_button_click(test_query_pninfor)  # 点击一个取消置顶按钮
            if self.assert_pninfor_canceltop_alert_textcontent(test_query_pninfor):  # 判断是否弹出取消置顶对话框
                logger.info('已经弹出取消置顶对话框')
                self.pninfor_canceltop_alert_submit_button_click(test_query_pninfor)  # 点击确定按钮
                if self.assert_canceltop_message_textcontent(test_query_pninfor):  # 判断是否取消置顶成功
                    logger.info('公示通报取消置顶成功')
                    assert True, '公示通报取消置顶成功'
                else:
                    logger.info('公示通报取消置顶失败')
                    assert False, '公示通报取消置顶失败'
            else:
                logger.info('没有弹出取消置顶对话框')
                assert False, '没有弹出取消置顶对话框'
        else:
            logger.info('没有进入公示通报界面，不执行取消置顶用例')
            assert False, '没有进入公示通报界面，不执行取消置顶用例'

    def test_delete_pbdinfor(self, test_query_pninfor):
        '''删除'''
        if test_query_pninfor:  # 已经查询
            self.pninfor_delete_button_click(test_query_pninfor)  # 点击删除按钮
            logger.info('点击了删除按钮')
            if self.assert_pninfor_delete_alert_textcontent(test_query_pninfor):  # 判断是否弹出删除对话框
                logger.info('弹出了删除对话框')
                self.pninfor_delete_alert_submit_button_click(test_query_pninfor)  # 点击确定按钮
                if self.assert_delete_message_textcontent(test_query_pninfor):  # 判断是否删除成功
                    logger.info('公示通报删除成功')
                    assert True, '公示通报删除成功'
                else:
                    logger.info('公示通报删除失败')
                    assert False, '公示通报删除失败'
            else:
                logger.info('没有弹出删除对话框')
                assert False, '没有弹出删除对话框'
        else:
            logger.info('没有进入公示通报界面，不执行删除用例')
            assert False, '没有进入公示通报界面，不执行删除用例'