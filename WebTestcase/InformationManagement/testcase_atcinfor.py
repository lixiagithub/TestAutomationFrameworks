# coding = utf-8
# Author:李昰 
# Date：2021/2/22 9:59
from WebTestcase.POM.Menu import Menu
from WebTestcase.POM.AtcInformationPage import AtcInformeationPage
import pytest
from log.log import logger
from untils import tool
from untils.op_mysql import execute_web #数据库连接
import time
class TestAtcinfor(AtcInformeationPage,Menu):
    @pytest.fixture(scope="class")
    def test_into_atcinforpage(self,login):
        '''进入空管资讯管理页面'''
        if login:
            '''用例：登录之后，点击资讯管理，点击空管资讯，进入空管资讯页面'''
            try:
                #退出iframe
                login.switch_to_default_iframe()
                #进入空管资讯管理页面
                self.into_atcinfor_page(login)
                # 定位iframe,并且进入iframe
                self.into_atcinfor_iframe(login)
                # 在空管资讯页面，查找空管资讯验证信息
                if self.assert_page_textcontent(login):
                    logger.info('进入空管资讯页面成功')
                    yield login
                    print('所有类的用例执行完毕,执行后置操作')
                    login.switch_to_default_iframe() #退出iframe
                    self.click_atcinfor_tab_close_button(login) #点击tab关闭按钮
                    logger.info("关闭空管资讯tab")
                    self.click_information_management(login)  # 点击咨询管理，收回下拉菜单
                    logger.info("点击咨询管理，收回下拉菜单")
                else:
                    logger.info('进入空管资讯页面失败')
                    assert False,'进入空管资讯页面失败'

            except Exception as  e:
                logger.info('进入空管资讯页面失败')
                assert False, '进入空管资讯页面失败'

    # @pytest.mark.skip()
    def test_add_atcinfor(self, test_into_atcinforpage):
        '''新增空管资讯'''
        if test_into_atcinforpage:#进入空管资讯界面
            old_number=self.assert_table_number_text(test_into_atcinforpage)#新增之前获取数据总数
            self.click_atcinfor_add_button(test_into_atcinforpage)#点击新增按钮
            if self.assert_page_add_textcontent(test_into_atcinforpage):#判断是否打开新增界面
                logger.info('进入空管资讯添加界面成功')
                test_into_atcinforpage.driver.switch_to.frame(0)  # 进入第二层新增iframe
                self.atcinfor_add(test_into_atcinforpage,'测试空管资讯标题','1','测试文章关键字','测试文章摘要',tool.generate_random_str(100))  # 新增空管资讯
                logger.info('执行新增操作完毕')
                self.into_atcinfor_iframe(test_into_atcinforpage) #新增之后切换到空管资讯iframe
                new_number = self.assert_table_number_text(test_into_atcinforpage)  # 添加后获取数据总数
                # 验证是否添加成功
                if eval(new_number) == eval(old_number) + 1:
                    logger.info('信息增加前总数是{0}，信息增加后总数是{1},新增成功'.format(old_number, new_number))
                    assert True,'新增成功'
                else:
                    logger.info('信息增加前总数是{0}，信息增加后总数是{1},新增失败'.format(old_number, new_number))
                    assert False,'新增失败'
            else:
                logger.info('进入空管资讯添加界面失败')
                assert False, '进入空管资讯添加界面失败'
        else:
            logger.info('没有进入空管资讯界面，不执行空管资讯添加')
            assert False, '没有进入空管资讯界面，不执行空管资讯添加用例'

    # @pytest.mark.skip()
    def test_update_atcinfor(self, test_into_atcinforpage):
        '''修改空管资讯'''
        if test_into_atcinforpage:#进入空管资讯界面
            title_text = self.get_table_atcinfor_title_text(test_into_atcinforpage)  # 获取列表中标题文本
            self.atcinfor_update_button_click(test_into_atcinforpage)  #点击编辑按钮
            if self.assert_page_update_textcontent(test_into_atcinforpage):  # 判断是否打开新增界面
                logger.info('进入了空管资讯编辑页面')
                test_into_atcinforpage.driver.switch_to.frame(0)  # 进入第二层修改iframe
                assert self.assert_update_table_atcinfor_title_text(test_into_atcinforpage,
                                                                        title_text), '文章标题回显是否正确'
                self.atcinfor_update_submit_button_click(test_into_atcinforpage)  #不修改任何内容，直接提交
                if self.assert_update_message_textcontent(test_into_atcinforpage):  #判断是否修改成功
                    self.into_atcinfor_iframe(test_into_atcinforpage)  # 修改之后切换到空管资讯iframe
                    logger.info('空管资讯编辑成功')
                    assert True,'空管资讯编辑成功'
                else:
                    logger.info('空管资讯编辑失败')
                    assert False, '空管资讯编辑失败'
            else:
                logger.info('进入空管资讯修改界面失败')
                assert False, '进入空管资讯修改界面失败'
        else:
            logger.info('没有进入空管资讯界面，不执行空管资讯编辑用例')
            assert False, '没有进入空管资讯界面，不执行空管资讯编辑用例'

    # @pytest.mark.skip()
    def test_query_atcinfor(self,test_into_atcinforpage):
        '''组合查询'''
        if test_into_atcinforpage:  #进入空管资讯界面
            self.atcinfor_query(test_into_atcinforpage, '测试空管资讯标题')  # 查询空管资讯
            logger.info('点击了查询按钮')
            time.sleep(2)
            table_number_text = self.assert_table_number_text(test_into_atcinforpage)
            query_str ="select * from sp_cms_article WHERE article_cat in (SELECT cat_id FROM sp_cms_article_category WHERE cat_id = 10 or cat_pid = 10) AND article_title like '%测试空管资讯标题%' AND add_time BETWEEN '"+tool.get_date_time()+" 00:00:00' AND '"+tool.get_date_time()+" 23:59:59' ORDER BY istop desc,article_order desc,add_time desc limit 0,10"
            db_query_res = execute_web(query_str)
            logger.info('table结果数{0}：数据库查询结果数{1}'.format(table_number_text, len(db_query_res)))  # 获取查询数量
            assert int(table_number_text) == len(db_query_res), 'table结果数{0}：数据库查询结果数{1}'.format(table_number_text,
                                                                                                 len(db_query_res))
        else:
            logger.info('没有进入空管资讯界面，不执行查询用例')
            assert False, '没有进入空管资讯界面，不执行查询用例'

    def test_top_atcinfor(self, test_into_atcinforpage):
        '''置顶'''
        if test_into_atcinforpage:  #进入空管资讯界面
            self.atcinfor_top_button_click(test_into_atcinforpage)  #随机点击一个置顶按钮
            if self.assert_atcinfor_top_alert_textcontent(test_into_atcinforpage):  #判断是否弹出置顶对话框
                logger.info('已经弹出置顶对话框')
                self.atcinfor_top_alert_submit_button_click(test_into_atcinforpage)  #点击确定按钮
                if self.assert_top_message_textcontent(test_into_atcinforpage):  #判断是否置顶成功
                    logger.info('空管资讯置顶成功')
                    assert True,'空管资讯置顶成功'
                else:
                    logger.info('空管资讯置顶失败')
                    assert False, '空管资讯置顶失败'
            else:
                logger.info('没有弹出置顶对话框')
                assert False, '没有弹出置顶对话框'
        else:
            logger.info('没有进入空管资讯界面，不执行置顶用例')
            assert False, '没有进入空管资讯界面，不执行置顶用例'

    def test_topcancel_infor(self, test_into_atcinforpage):
        '''取消置顶'''
        if test_into_atcinforpage:  #进入空管资讯界面
            time.sleep(2)
            self.atcinfor_canceltop_button_click(test_into_atcinforpage)  # 随机点击一个取消置顶按钮
            if self.assert_atcinfor_canceltop_alert_textcontent(test_into_atcinforpage):  # 判断是否弹出取消置顶对话框
                logger.info('已经弹出取消置顶对话框')
                self.atcinfor_canceltop_alert_submit_button_click(test_into_atcinforpage)  # 点击确定按钮
                if self.assert_canceltop_message_textcontent(test_into_atcinforpage):  # 判断是否取消置顶成功
                    logger.info('空管资讯取消置顶成功')
                    assert True, '空管资讯取消置顶成功'
                else:
                    logger.info('空管资讯取消置顶失败')
                    assert False, '空管资讯取消置顶失败'
            else:
                logger.info('没有弹出取消置顶对话框')
                assert False, '没有弹出取消置顶对话框'
        else:
            logger.info('没有进入空管资讯界面，不执行取消置顶用例')
            assert False, '没有进入空管资讯界面，不执行取消置顶用例'

    def test_delete_atcinfor(self, test_into_atcinforpage):
        '''删除空管资讯'''
        if test_into_atcinforpage:  #进入空管资讯界面
            time.sleep(2)
            self.atcinfor_delete_button_click(test_into_atcinforpage)  # 随机点击一个删除按钮
            if self.assert_atcinfor_delete_alert_textcontent(test_into_atcinforpage):  # 判断是否弹出删除对话框
                logger.info('已经弹出删除对话框')
                self.atcinfor_delete_alert_submit_button_click(test_into_atcinforpage)  # 点击确定按钮
                if self.assert_delete_message_textcontent(test_into_atcinforpage):  # 判断是否删除成功
                    logger.info('空管资讯删除成功')
                    assert True, '空管资讯删除成功'
                else:
                    logger.info('空管资讯删除失败')
                    assert False, '空管资讯删除失败'
            else:
                logger.info('没有弹出取消置顶对话框')
                assert False, '没有弹出取消置顶对话框'
        else:
            logger.info('没有进入空管资讯界面，不执行删除用例')
            assert False, '没有进入空管资讯界面，不执行删除用例'