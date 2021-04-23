# coding = utf-8
# Author:李昰 
# Date：2021/4/21 15:06
from WebTestcase.POM.Menu import Menu
from WebTestcase.POM.PartyBuildingDynamicPage import PartyBuildingDynamicPage
import pytest
from log.log import logger
from untils import tool
from untils.op_mysql import execute_web  # 数据库连接
import time


class TestPbdinfor(PartyBuildingDynamicPage, Menu):
    def setup_class(self):  # 每个类执行前执行一次
        self.pbd_name = tool.random_GBK2312(10)
        self.pbd_desc = tool.generate_random_str(20)
        self.pbd_editor = tool.generate_random_str(100)

    @pytest.fixture(scope='module')  # 每个函数可以调用的变量
    def global_data(self):
        '''
        pbdinfor_classify:党建动态类别
        :return: 
        '''
        return {'pbdinfor_classify': ''}

    @pytest.fixture(scope="class")
    def test_into_pbdinforpage(self, login):
        '''进入党建动态管理页面'''
        if login:
            '''用例：登录之后，点击资讯管理，点击党建动态，进入党建动态页面'''
            try:
                # 退出iframe
                login.switch_to_default_iframe()
                # 进入空管资讯管理页面
                self.into_pbdinfor_page(login)
                # 定位iframe,并且进入iframe
                self.into_pbdinfor_iframe(login)
                # 在党建动态页面，查找党建动态验证信息
                if self.assert_page_textcontent(login):
                    logger.info('进入党建动态页面成功')
                    yield login
                    print('所有类的用例执行完毕,执行后置操作')
                    login.switch_to_default_iframe()  # 退出iframe
                    self.click_pbdinfor_tab_close_button(login)  # 点击tab关闭按钮
                    logger.info("关闭党建动态tab")
                    self.click_information_management(login)  # 点击咨询管理，收回下拉菜单
                    logger.info("点击咨询管理，收回下拉菜单")
                else:
                    yield False
                    logger.info('进入党建动态页面失败')
                    assert False, '进入党建动态页面失败'

            except Exception as  e:
                logger.info('进入党建动态页面失败')
                assert False, '进入党建动态页面失败'

    def test_add_pbdinfor(self, test_into_pbdinforpage, global_data):
        if test_into_pbdinforpage:
            global_data['pbdinfor_classify'] = self.random_pbdinfor_classify(test_into_pbdinforpage)  # 随机选择树形节点，党建动态分类
            old_number = self.assert_table_number_text(test_into_pbdinforpage)  # 获取新增前的总数
            logger.info('新增前总数{}'.format(old_number))
            self.click_atcinfor_add_button(test_into_pbdinforpage)  # 点击新增按钮
            if self.assert_page_add_textcontent(test_into_pbdinforpage):  # 判断是否打开新增界面
                logger.info('进入党建动态添加界面成功')
                test_into_pbdinforpage.driver.switch_to.frame(0)  # 进入第二层新增iframe
                self.pbdinfor_add(test_into_pbdinforpage, self.pbd_name, self.pbd_desc, self.pbd_editor)  # 新增党建动态
                logger.info('执行新增操作完毕')
                self.into_pbdinfor_iframe(test_into_pbdinforpage)  # 新增之后切换到党建动态iframe
                new_number = self.assert_table_number_text(test_into_pbdinforpage)  # 添加后获取数据总数
                # 验证是否添加成功
                if eval(new_number) == eval(old_number) + 1:
                    logger.info('{2}信息增加前总数是{0}，信息增加后总数是{1},新增成功'.format(old_number, new_number, global_data['pbdinfor_classify']))
                    assert True, '新增成功'
                else:
                    logger.info('{2}信息增加前总数是{0}，信息增加后总数是{1},新增失败'.format(old_number, new_number, global_data['pbdinfor_classify']))
                    assert False, '新增失败'
            else:
                logger.info('进入党建动态添加界面失败')
                assert False, '进入党建动态添加界面失败'
        else:
            logger.info('进入党建动态页面失败,无法进行添加')
            assert False, '进入党建动态页面失败,无法进行添加'

    # @pytest.mark.skip()
    def test_update_pbdinfor(self, test_into_pbdinforpage):
        '''修改空管资讯'''
        if test_into_pbdinforpage:  # 进入空管资讯界面
            title_text = self.get_table_pbdinfor_title_text(test_into_pbdinforpage)  # 获取列表中标题文本
            self.pbdinfor_update_button_click(test_into_pbdinforpage)  # 点击编辑按钮
            if self.assert_page_update_textcontent(test_into_pbdinforpage):  # 判断是否打开新增界面
                logger.info('进入了党建动态编辑页面')
                test_into_pbdinforpage.driver.switch_to.frame(0)  # 进入第二层修改iframe
                assert self.assert_update_table_pbdinfor_title_text(test_into_pbdinforpage,
                                                                    title_text), '文章名称回显是否正确'
                self.pbdinfor_update_submit_button_click(test_into_pbdinforpage)  # 不修改任何内容，直接提交
                if self.assert_update_message_textcontent(test_into_pbdinforpage):  # 判断是否修改成功
                    self.into_pbdinfor_iframe(test_into_pbdinforpage)  # 修改之后切换到党建动态iframe
                    logger.info('党建动态编辑成功')
                    assert True, '党建动态编辑成功'
                else:
                    logger.info('党建动态编辑失败')
                    assert False, '党建动态编辑失败'
            else:
                logger.info('进入党建动态修改界面失败')
                assert False, '进入党建动态修改界面失败'
        else:
            logger.info('没有进入党建动态界面，不执行党建动态编辑用例')
            assert False, '没有进入党建动态界面，不执行党建动态编辑用例'

    # @pytest.mark.skip()
    def test_query_pbdinfor(self, test_into_pbdinforpage, global_data):
        '''查询'''
        if test_into_pbdinforpage:  # 进入党建动态界面
            self.pbdinfor_query(test_into_pbdinforpage, self.pbd_name)  # 查询党建动态
            logger.info('点击了查询按钮')
            time.sleep(2)
            table_number_text = self.assert_table_number_text(test_into_pbdinforpage)
            query_str = "SELECT * FROM `sp_pbd_article` WHERE `type_id` = "+self.get_pbdinfor_classify(global_data['pbdinfor_classify'])+" AND `pbd_name` LIKE '"+self.pbd_name+"' ORDER BY update_time desc LIMIT 0,10 "
            db_query_res = execute_web(query_str)
            logger.info('table结果数{0}：数据库查询结果数{1}'.format(table_number_text, len(db_query_res)))  # 获取查询数量
            assert int(table_number_text) == len(db_query_res), 'table结果数{0}：数据库查询结果数{1}'.format(table_number_text,
                                                                                                 len(db_query_res))
        else:
            logger.info('没有进入党建动态界面，不执行查询用例')
            assert False, '没有进入党建动态界面，不执行查询用例'
