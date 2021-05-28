# coding = utf-8
# Author:李昰 
# Date：2021/5/14 13:33

from WebTestcase.POM.Menu import Menu
from WebTestcase.POM.AirTrafficControlPressPage import AirTrafficControlPressPage
import pytest
from log.log import logger
from untils import tool
from untils.op_mysql import execute_web  # 数据库连接
import time
import random

class TestAtcpinfor(AirTrafficControlPressPage, Menu):
    def setup_class(self):  # 每个类执行前执行一次
        self.atcp_name = tool.random_GBK2312(10)
        self.atcp_press = tool.random_GBK2312(10)
        self.atcp_brief = tool.generate_random_str(50)
        self.atcp_number = "第{}期".format(random.randint(1,300))#随机生成1到300之间的整数
        self.atcp_layout = "第{}版".format(random.randint(1,10))  # 随机生成1到300之间的整数
        self.atcp_title = tool.random_GBK2312(10)
        self.atcp_author = tool.create_name()
        self.atcp_editor = tool.random_GBK2312(50)

    @pytest.fixture(scope='module')  # 每个函数可以调用的变量
    def global_data(self):
        '''
        pninfor_organization:空管报刊对应组织
        :return: 
        '''
        return {'pninfor_organization': ''}

    @pytest.fixture(scope="class")
    def test_into_atcpinforpage(self, login):
        '''进入空管报刊管理页面'''
        if login:
            '''用例：登录之后，点击资讯管理，点击空管报刊，进入空管报刊页面'''
            try:
                # 退出iframe
                login.switch_to_default_iframe()
                # 进入空管报刊管理页面
                self.into_atcpinfor_page(login)
                # 定位iframe,并且进入iframe
                self.into_atcpinfor_iframe(login)
                # 在空管报刊页面，查找空管报刊验证信息
                if self.assert_page_textcontent(login):
                    logger.info('进入空管报刊页面成功')
                    yield login
                    assert True, '进入空管报刊页面成功'
                    print('所有类的用例执行完毕,执行后置操作')
                    login.switch_to_default_iframe()  # 退出iframe
                    self.click_atcpinfor_tab_close_button(login)  # 点击tab关闭按钮
                    logger.info("关闭空管报刊tab")
                    self.click_information_management(login)  # 点击咨询管理，收回下拉菜单
                    logger.info("点击咨询管理，收回下拉菜单")
                else:
                    yield False
                    logger.info('进入空管报刊页面失败')
                    assert False, '进入空管报刊页面失败'

            except Exception as  e:
                logger.info('进入空管报刊页面失败')
                assert False, '进入空管报刊页面失败'
                
    def test_add_atcpinfor(self, test_into_atcpinforpage):
        '''新增报刊'''
        if test_into_atcpinforpage:
            old_number = self.assert_table_number_text(test_into_atcpinforpage)  # 获取新增前的总数
            logger.info('新增前总数{}'.format(old_number))
            self.click_atcpinfor_add_button(test_into_atcpinforpage)  # 点击新增按钮
            if self.assert_page_add_textcontent(test_into_atcpinforpage):  # 判断是否打开新增界面
                logger.info('进入空管报刊添加界面成功')
                self.atcpinfor_add(test_into_atcpinforpage, self.atcp_name,self.atcp_press,self.atcp_brief)  # 新增空管报刊
                logger.info('执行新增操作成功')
                new_number = self.assert_table_number_text(test_into_atcpinforpage)  # 添加后获取数据总数
                # 验证是否添加成功
                if eval(new_number) == eval(old_number) + 1:
                    logger.info('空管报刊信息增加前总数是{0}，信息增加后总数是{1},新增成功'.format(old_number, new_number))
                    assert True, '新增成功'
                else:
                    test_into_atcpinforpage.switch_to_default_iframe()  # 退出iframe
                    self.menu_atcpinfor_double_click(test_into_atcpinforpage)  # 点击导航栏，重置
                    logger.info('空管报刊信息增加前总数是{0}，信息增加后总数是{1},新增失败'.format(old_number, new_number))
                    assert False, '新增失败'
            else:
                test_into_atcpinforpage.switch_to_default_iframe()# 退出iframe
                self.menu_atcpinfor_double_click(test_into_atcpinforpage)  # 点击导航栏，重置
                logger.info('进入空管报刊添加界面失败')
                assert False, '进入空管报刊添加界面失败'
        else:
            logger.info('进入空管报刊页面失败,无法进行添加')
            assert False, '进入空管报刊页面失败,无法进行添加'

    @pytest.fixture(scope="function")
    def test_query_atcpinfor(self, test_into_atcpinforpage):
        '''查询报刊'''
        if test_into_atcpinforpage:  # 进入空管报刊界面
            test_into_atcpinforpage.switch_to_default_iframe()  # 退出iframe
            self.menu_atcpinfor_double_click(test_into_atcpinforpage)  # 点击导航栏，重置
            self.into_atcpinfor_iframe(test_into_atcpinforpage)  # 定位iframe,并且进入iframe
            self.atcpinfor_query(test_into_atcpinforpage, self.atcp_name)  # 查询空管报刊
            logger.info('点击了查询按钮')
            time.sleep(2)
            table_number_text = self.assert_table_number_text(test_into_atcpinforpage)
            query_str = "SELECT * FROM `sp_news_journal` WHERE `journal_name` LIKE '" + self.atcp_name + "' ORDER BY update_time desc LIMIT 0,10 "
            db_query_res = execute_web(query_str)
            if int(table_number_text) == len(db_query_res):
                logger.info('table结果数{0}：数据库查询结果数{1}'.format(table_number_text, len(db_query_res)))  # 获取查询数量
                logger.info('空管报刊查询成功')
                yield test_into_atcpinforpage
                assert True,'查询正确：table结果数{0}：数据库查询结果数{1}'.format(table_number_text,len(db_query_res))
            else:
                logger.info('空管报刊查询失败')
                yield False
                assert False, '查询失败：table结果数{0}：数据库查询结果数{1}'.format(table_number_text,len(db_query_res))
        else:
            logger.info('没有进入空管报刊界面，不执行查询用例')
            assert False, '没有进入空管报刊界面，不执行查询用例'

    def test_update_atcpinfor(self, test_query_atcpinfor):
        '''修改报刊'''
        if test_query_atcpinfor:  # 已经查询
            self.atcpinfor_update_button_click(test_query_atcpinfor)  # 点击编辑按钮
            if self.assert_page_update_textcontent(test_query_atcpinfor):  # 判断是否打开修改界面
                logger.info('进入了空管报刊编辑页面')
                message = self.assert_update_textcontent(test_query_atcpinfor, self.atcp_name, self.atcp_press,
                                                         self.atcp_brief)  # 校验详情信息
                if message[0]:
                    logger.info(message[1])
                    self.atcpinfor_update_submit_button_click(test_query_atcpinfor)  # 不修改任何内容，直接提交
                    if self.assert_update_message_textcontent(test_query_atcpinfor):  # 判断是否修改成功
                        logger.info('空管报刊编辑成功')
                        assert True, '空管报刊编辑成功'
                    else:
                        logger.info('空管报刊编辑失败')
                        assert False, '空管报刊编辑失败'
                else:
                    logger.info(message[1])
                    assert False, message[1]
            else:
                logger.info('进入空管报刊修改界面失败')
                assert False, '进入空管报刊修改界面失败'
        else:
            logger.info('没有执行查询，不执行空管报刊编辑用例')
            assert False, '没有执行查询，不执行空管报刊编辑用例'

    @pytest.fixture(scope="function")
    def test_into_atcpinfor_number_page(self, test_query_atcpinfor):
        '''进入空管报刊期数管理页面'''
        if test_query_atcpinfor:
            self.atcpinfor_manage_number_button_click(test_query_atcpinfor)#点击管理
            if self.assert_number_page_textcontent(test_query_atcpinfor,self.atcp_name):
                logger.info('进入空管报刊期数页面成功')
                yield test_query_atcpinfor
                assert True, '进入空管报刊期数页面成功'
            else:
                yield False
                logger.info('进入空管报刊期数页面失败')
                assert False, '进入空管报刊期数页面失败'
        else:
            logger.info('没有执行查询，不执行点击管理用例')
            assert False, '没有执行查询，不执行点击管理用例'

    def test_add_atcpinfor_number(self, test_into_atcpinfor_number_page):
        '''新增期数'''
        if test_into_atcpinfor_number_page:
            old_number = self.assert_number_table_number_text(test_into_atcpinfor_number_page)  # 获取新增前的总数
            logger.info('新增期数前总数{}'.format(old_number))
            self.click_atcpinfor_add_number_button(test_into_atcpinfor_number_page)  # 点击新增按钮
            if self.assert_page_add_number_textcontent(test_into_atcpinfor_number_page):  # 判断是否打开新增界面
                logger.info('进入空管报刊期数添加界面成功')
                self.atcpinfor_number_add(test_into_atcpinfor_number_page, self.atcp_number)  # 新增空管报刊
                logger.info('执行新增操作成功')
                new_number = self.assert_number_table_number_text(test_into_atcpinfor_number_page)  # 添加后获取数据总数
                # 验证是否添加成功
                if eval(new_number) == eval(old_number) + 1:
                    logger.info('空管报刊期数信息增加前总数是{0}，信息增加后总数是{1},新增成功'.format(old_number, new_number))
                    assert True, '新增成功'
                else:
                    self.atcpinfor_navigation_number_button_click(test_into_atcpinfor_number_page)#点击导航重置
                    logger.info('空管报刊期数信息增加前总数是{0}，信息增加后总数是{1},新增失败'.format(old_number, new_number))
                    assert False, '新增失败'
            else:
                self.atcpinfor_navigation_number_button_click(test_into_atcpinfor_number_page)#点击导航重置
                logger.info('进入空管报刊期数添加界面失败')
                assert False, '进入空管报刊期数添加界面失败'
        else:
            logger.info('进入空管报刊期数页面失败,无法进行添加期数')
            assert False, '进入空管报刊期数页面失败,无法进行添加期数'

    @pytest.fixture(scope="function")
    def test_query_atcpinfor_number(self, test_into_atcpinfor_number_page):
        '''查询期数'''
        if test_into_atcpinfor_number_page:  # 进入空管报刊界面
            self.atcpinfor_navigation_number_button_click(test_into_atcpinfor_number_page)  # 点击导航重置
            self.atcpinfor_number_query(test_into_atcpinfor_number_page, self.atcp_number)  # 查询空管报刊期数
            logger.info('点击了查询按钮')
            time.sleep(2)
            table_number_text = self.assert_number_table_number_text(test_into_atcpinfor_number_page)
            query_str = "select * from sp_news_period p ,sp_news_journal j where p.journal_id=j.journal_id and j.journal_name LIKE '" + self.atcp_name + "' and p.period_name like '" + self.atcp_number + "' ORDER BY p.update_time desc LIMIT 0,10"
            db_query_res = execute_web(query_str)
            if int(table_number_text) == len(db_query_res):
                logger.info('table结果数{0}：数据库查询结果数{1}'.format(table_number_text, len(db_query_res)))  # 获取查询数量
                logger.info('空管报刊期数查询成功')
                yield test_into_atcpinfor_number_page
                assert True, '查询正确：table结果数{0}：数据库查询结果数{1}'.format(table_number_text, len(db_query_res))
            else:
                logger.info('空管报刊期数查询失败')
                yield False
                assert False, '查询失败：table结果数{0}：数据库查询结果数{1}'.format(table_number_text, len(db_query_res))
        else:
            logger.info('没有进入空管报刊期数界面，不执行期数查询用例')
            assert False, '没有进入空管报刊期数界面，不执行期数查询用例'

    def test_update_atcpinfor_number(self, test_query_atcpinfor_number):
        '''修改期数'''
        if test_query_atcpinfor_number:  # 已经查询
            self.atcpinfor_number_update_button_click(test_query_atcpinfor_number)  # 点击编辑按钮
            if self.assert_number_page_update_textcontent(test_query_atcpinfor_number):  # 判断是否打开期数修改界面
                logger.info('进入了空管报刊期数编辑页面')
                message = self.assert_number_update_textcontent(test_query_atcpinfor_number, self.atcp_number)  # 校验详情信息
                if message[0]:
                    logger.info(message[1])
                    self.atcpinfor_number_update_submit_button_click(test_query_atcpinfor_number)  # 不修改任何内容，直接提交
                    if self.assert_number_update_message_textcontent(test_query_atcpinfor_number):  # 判断是否修改成功
                        logger.info('空管报刊期数编辑成功')
                        assert True, '空管报刊期数编辑成功'
                    else:
                        logger.info('空管报刊期数编辑失败')
                        assert False, '空管报刊期数编辑失败'
                else:
                    logger.info(message[1])
                    assert False, message[1]
            else:
                logger.info('进入空管报刊期数修改界面失败')
                assert False, '进入空管报刊期数修改界面失败'
        else:
            logger.info('没有执行期数查询，不执行空管报刊期数编辑用例')
            assert False, '没有执行期数查询，不执行空管报刊期数编辑用例'

    @pytest.fixture(scope="function")
    def test_into_atcpinfor_journal_page(self, test_query_atcpinfor_number):
        '''进入空管报刊期数期刊详情管理页面'''
        if test_query_atcpinfor_number:
            self.atcpinfor_manage_journal_button_click(test_query_atcpinfor_number)  # 点击管理
            if self.assert_journal_page_textcontent(test_query_atcpinfor_number):
                logger.info('进入空管报刊期数-期刊详情页面成功')
                yield test_query_atcpinfor_number
                assert True, '进入空管报刊期数-期刊详情页面成功'
            else:
                yield False
                logger.info('进入空管报刊期数-期刊详情页面失败')
                assert False, '进入空管报刊期数-期刊详情页面失败'
        else:
            logger.info('没有执行期数查询，不执行点击管理用例')
            assert False, '没有执行期数查询，不执行点击管理用例'

    def test_add_atcpinfor_journal_layout(self, test_into_atcpinfor_journal_page):
        '''新增版面'''
        if test_into_atcpinfor_journal_page:
            self.click_atcpinfor_add_journal_layout_button(test_into_atcpinfor_journal_page)  # 点击添加版面按钮
            if self.assert_page_add_journal_layout_textcontent(test_into_atcpinfor_journal_page):  # 判断是否打开新增界面
                logger.info('进入版面添加界面成功')
                self.atcpinfor_journal_layout_add(test_into_atcpinfor_journal_page, self.atcp_layout)  # 新增版面
                # 验证是否添加成功
                if self.assert_journal_layout_add_message_textcontent(test_into_atcpinfor_journal_page):
                    logger.info('版面信息新增成功')
                    assert True, '版面信息新增成功'
                else:
                    self.atcpinfor_navigation_journal_button_click(test_into_atcpinfor_journal_page)  # 点击导航重置
                    logger.info('版面信息新增失败')
                    assert False, '版面信息新增失败'
            else:
                self.atcpinfor_navigation_journal_button_click(test_into_atcpinfor_journal_page)  # 点击导航重置
                logger.info('进入空管报刊期数添加界面失败')
                assert False, '进入空管报刊期数添加界面失败'
        else:
            logger.info('进入期刊详情页面失败,无法进行添加期数')
            assert False, '进入期刊详情页面失败,无法进行添加期数'

    def test_update_atcpinfor_journal_layout(self, test_into_atcpinfor_journal_page):
        '''修改版面'''
        if test_into_atcpinfor_journal_page:  # 进入界面
            self.atcpinfor_journal_layout_update_button_click(test_into_atcpinfor_journal_page)  # 点击编辑按钮
            if self.assert_journal_layout_page_update_textcontent(test_into_atcpinfor_journal_page):  # 判断是否打开期数修改界面
                logger.info('进入了版面编辑页面')
                message = self.assert_journal_layout_update_textcontent(test_into_atcpinfor_journal_page, self.atcp_layout)  # 校验详情信息
                if message[0]:
                    logger.info(message[1])
                    self.atcpinfor_journal_layout_update_submit_button_click(test_into_atcpinfor_journal_page)  # 不修改任何内容，直接提交
                    if self.assert_journal_layout_update_message_textcontent(test_into_atcpinfor_journal_page):  # 判断是否修改成功
                        logger.info('版面编辑成功')
                        assert True, '版面编辑成功'
                    else:
                        logger.info('版面编辑失败')
                        assert False, '版面编辑失败'
                else:
                    logger.info(message[1])
                    assert False, message[1]
            else:
                logger.info('进入版面修改界面失败')
                assert False, '进入版面修改界面失败'
        else:
            logger.info('没有进入期刊详情界面，不执行版面编辑用例')
            assert False, '没有进入期刊详情界面，不执行版面编辑用例'

    @pytest.mark.dependency(depends=["test_delete_atcpinfor_journal_contents"])
    def test_delete_atcpinfor_journal_layout(self, test_into_atcpinfor_journal_page):
        '''删除版面'''
        if test_into_atcpinfor_journal_page:  # 进入界面
            self.atcpinfor_navigation_journal_button_click(test_into_atcpinfor_journal_page) #重置，进入期刊详情页
            self.atcpinfor_journal_layout_delete_button_click(test_into_atcpinfor_journal_page)  # 点击删除按钮
            logger.info('点击了删除按钮')
            if self.assert_atcpinfor_journal_layout_delete_alert_textcontent(test_into_atcpinfor_journal_page):  # 判断是否弹出删除对话框
                logger.info('弹出了删除对话框')
                self.atcpinfor_journal_layout_delete_alert_submit_button_click(test_into_atcpinfor_journal_page)  # 点击确定按钮
                if self.assert_atcpinfor_journal_layout_delete_message_textcontent(test_into_atcpinfor_journal_page):  # 判断是否删除成功
                    logger.info('版面删除成功')
                    assert True, '版面删除成功'
                else:
                    logger.info('版面删除失败')
                    assert False, '版面删除失败'
            else:
                logger.info('没有弹出删除对话框')
                assert False, '没有弹出删除对话框'
        else:
            logger.info('没有进入期刊详情界面，不执行删除版面用例')
            assert False, '没有进入期刊详情界面，不执行删除版面用例'

    def test_add_atcpinfor_journal_contents(self, test_into_atcpinfor_journal_page):
        '''新增目录'''
        if test_into_atcpinfor_journal_page:
            self.click_atcpinfor_add_journal_contents_button(test_into_atcpinfor_journal_page)  # 点击添加目录按钮
            if self.assert_page_add_journal_contents_textcontent(test_into_atcpinfor_journal_page):  # 判断是否打开新增界面
                logger.info('进入目录添加界面成功')
                self.atcpinfor_journal_contents_add(test_into_atcpinfor_journal_page, self.atcp_layout,self.atcp_title,self.atcp_author,self.atcp_editor)  # 新增版面
                # 验证是否添加成功
                if self.assert_journal_contents_add_message_textcontent(test_into_atcpinfor_journal_page):
                    logger.info('目录信息新增成功')
                    assert True, '目录信息新增成功'
                else:
                    self.atcpinfor_navigation_journal_button_click(test_into_atcpinfor_journal_page)  # 点击导航重置
                    self.atcpinfor_journal_contents_tab_click(test_into_atcpinfor_journal_page) #点击目录选项卡
                    logger.info('目录信息新增失败')
                    assert False, '目录信息新增失败'
            else:
                self.atcpinfor_navigation_journal_button_click(test_into_atcpinfor_journal_page)  # 点击导航重置
                self.atcpinfor_journal_contents_tab_click(test_into_atcpinfor_journal_page)  # 点击目录选项卡
                logger.info('进入空管报刊期数添加界面失败')
                assert False, '进入空管报刊期数添加界面失败'
        else:
            logger.info('进入期刊详情页面失败,无法进行目录添加')
            assert False, '进入期刊详情页面失败,无法进行目录添加'

    def test_update_atcpinfor_journal_contents(self, test_into_atcpinfor_journal_page):
        '''修改目录'''
        if test_into_atcpinfor_journal_page:  # 进入界面
            self.atcpinfor_journal_contents_update_button_click(test_into_atcpinfor_journal_page)  # 点击编辑按钮
            if self.assert_journal_contents_page_update_textcontent(test_into_atcpinfor_journal_page):  # 判断是否打开期数修改界面
                logger.info('进入了目录编辑页面')
                message = self.assert_journal_contents_update_textcontent(test_into_atcpinfor_journal_page,self.atcp_layout,self.atcp_title,self.atcp_author,self.atcp_editor)  # 校验详情信息
                if message[0]:
                    logger.info(message[1])
                    self.atcpinfor_journal_contents_update_submit_button_click(test_into_atcpinfor_journal_page)  # 不修改任何内容，直接提交
                    if self.assert_journal_contents_update_message_textcontent(test_into_atcpinfor_journal_page):  # 判断是否修改成功
                        logger.info('目录编辑成功')
                        assert True, '目录编辑成功'
                    else:
                        self.atcpinfor_navigation_journal_button_click(test_into_atcpinfor_journal_page)  # 点击导航重置
                        self.atcpinfor_journal_contents_tab_click(test_into_atcpinfor_journal_page)  # 点击目录选项卡
                        logger.info('目录编辑失败')
                        assert False, '目录编辑失败'
                else:
                    self.atcpinfor_navigation_journal_button_click(test_into_atcpinfor_journal_page)  # 点击导航重置
                    self.atcpinfor_journal_contents_tab_click(test_into_atcpinfor_journal_page)  # 点击目录选项卡
                    logger.info(message[1])
                    assert False, message[1]
            else:
                self.atcpinfor_navigation_journal_button_click(test_into_atcpinfor_journal_page)  # 点击导航重置
                self.atcpinfor_journal_contents_tab_click(test_into_atcpinfor_journal_page)  # 点击目录选项卡
                logger.info('进入目录修改界面失败')
                assert False, '进入目录修改界面失败'
        else:
            logger.info('没有进入期刊详情界面，不执行目录编辑用例')
            assert False, '没有进入期刊详情界面，不执行目录编辑用例'

    @pytest.mark.dependency(name="test_delete_atcpinfor_journal_contents")
    def test_delete_atcpinfor_journal_contents(self, test_into_atcpinfor_journal_page):
        '''删除目录'''
        if test_into_atcpinfor_journal_page:  # 进入界面
            self.atcpinfor_journal_contents_delete_button_click(test_into_atcpinfor_journal_page)  # 点击删除按钮
            logger.info('点击了删除按钮')
            if self.assert_atcpinfor_journal_contents_delete_alert_textcontent(test_into_atcpinfor_journal_page):  # 判断是否弹出删除对话框
                logger.info('弹出了删除对话框')
                self.atcpinfor_journal_contents_delete_alert_submit_button_click(test_into_atcpinfor_journal_page)  # 点击确定按钮
                if self.assert_atcpinfor_journal_contents_delete_message_textcontent(test_into_atcpinfor_journal_page):  # 判断是否删除成功
                    logger.info('目录删除成功')
                    assert True, '目录删除成功'
                else:
                    self.atcpinfor_navigation_journal_button_click(test_into_atcpinfor_journal_page)  # 点击导航重置
                    self.atcpinfor_journal_contents_tab_click(test_into_atcpinfor_journal_page)  # 点击目录选项卡
                    logger.info('目录删除失败')
                    assert False, '目录删除失败'
            else:
                self.atcpinfor_navigation_journal_button_click(test_into_atcpinfor_journal_page)  # 点击导航重置
                self.atcpinfor_journal_contents_tab_click(test_into_atcpinfor_journal_page)  # 点击目录选项卡
                logger.info('没有弹出删除对话框')
                assert False, '没有弹出删除对话框'
        else:
            logger.info('没有进入期刊详情界面，不执行目录删除用例')
            assert False, '没有进入期刊详情界面，不执行目录删除用例'