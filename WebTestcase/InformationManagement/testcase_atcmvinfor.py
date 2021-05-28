# coding = utf-8
# Author:李昰 
# Date：2021/5/19 14:40

from WebTestcase.POM.Menu import Menu
from WebTestcase.POM.AirTrafficControlMicroVisionListPage import AirTrafficControlMicroVisionListPage
from WebTestcase.POM.AirTrafficControlMicroVisionClassifyPage import AirTrafficControlMicroVisionClassifyPage
import pytest
from log.log import logger
# import logging
from untils import tool
from untils.op_mysql import execute_web  # 数据库连接
import time
import random


# from ATF.Method import task_info, attach, step, class_info
# import ATF.Log
# log = logging.getLogger(__name__)

class TestAtcmvinfor(AirTrafficControlMicroVisionListPage, AirTrafficControlMicroVisionClassifyPage, Menu):
    def setup_class(self):  # 每个类执行前执行一次
        self.topcol_name = tool.random_GBK2312(10)
        self.soncol_name = tool.random_GBK2312(10)
        self.atcmv_name = tool.random_GBK2312(10)
        self.atcmv_time = random.randint(1, 300)  # 随机生成1到300之间的整数
        self.atcmv_vedio = tool.random_GBK2312(10)
        self.atcmv_size = random.randint(1, 300)  # 随机生成1到300之间的整数
        self.atcmv_editor = tool.random_GBK2312(50) # 随机生成50字

    @pytest.fixture(scope='module')  # 每个函数可以调用的变量
    def global_data(self):
        '''
        pninfor_organization:空管微视分类
        :return: 
        '''
        return {'atcmvinfor_classify': ''}

    # @task_info(
    #     编号='进入空管微视类型页面',
    #     作者='李昰',
    #     日期='2021-05-21'
    # )
    @pytest.fixture(scope="function")
    def test_into_atcmvclassifyinforpage(self, login):
        '''进入空管空管微视类型页面'''
        if login:
            '''用例：登录之后，点击资讯管理，点击空管微视，点击空管微视类型，进入空管微视类型页面'''
            try:
                # 退出iframe
                login.switch_to_default_iframe()
                # 进入空管微视类型页面
                self.into_atcmvclassifyinfor_page(login)
                # 定位iframe,并且进入iframe
                self.into_atcmvcinfor_iframe(login)
                # 在空管微视列表页面，查找空管微视列表验证信息
                if self.assert_atcmvcinfor_page_textcontent(login):
                    logger.info('进入空管微视类型页面成功')
                    yield login
                    assert True, '进入空管微视类型页面成功'
                    print('所有类的用例执行完毕,执行后置操作')
                    login.switch_to_default_iframe()  # 退出iframe
                    self.click_atcmvcinfor_tab_close_button(login)  # 点击tab关闭按钮
                    logger.info("关闭空管微视类型tab")
                    time.sleep(1)
                    self.click_airtrafficcontrol_mv_management(login)  # 点击菜单空管微视按钮
                    logger.info("点击空管微视，收回下拉菜单")
                    time.sleep(1)
                    self.click_information_management(login)  # 点击咨询管理，收回下拉菜单
                    logger.info("点击咨询管理，收回下拉菜单")
                    time.sleep(1)
                else:
                    yield False
                    logger.info('进入空管微视类型页面失败')
                    assert False, '进入空管微视类型页面失败'
            except Exception as  e:
                logger.info('进入空管微视类型页面失败')
                assert False, '进入空管微视类型页面失败'

    # @task_info(
    #     编号='空管微视类型顶级栏目新增',
    #     作者='李昰',
    #     日期='2021-05-21'
    # )
    #@pytest.mark.skip()
    def test_add_atcmvclassifyinfor_topcol(self, test_into_atcmvclassifyinforpage):
        '''新增空管微视顶级栏目'''
        assert test_into_atcmvclassifyinforpage, '进入空管微视类型页面失败,无法进行主栏目添加'
        self.click_atcmvcinfor_add_topcol_button(test_into_atcmvclassifyinforpage)  # 点击添加顶级栏目按钮
        assert self.assert_atcmvcinfor_add_topcol_page_textcontent(
            test_into_atcmvclassifyinforpage), '进入空管微视主栏目添加界面失败'  # 判断是否打开新增界面
        logger.info('进入空管微视主栏目添加界面成功')
        self.atcmvcinfor_topcol_add(test_into_atcmvclassifyinforpage, self.topcol_name)  # 新增空管微视主栏目
        assert self.assert_atcmvcinfor_topcol_add_message_textcontent(
            test_into_atcmvclassifyinforpage), '主栏目新增失败'  # 验证是否添加成功
        logger.info('主栏目新增成功')

    # @task_info(
    #     编号='空管微视类型顶级栏目修改',
    #     作者='李昰',
    #     日期='2021-05-21'
    # )
    #@pytest.mark.skip()
    def test_update_atcmvclassifyinfor_topcol(self, test_into_atcmvclassifyinforpage):
        '''修改空管微视顶级栏目'''
        assert test_into_atcmvclassifyinforpage, '进入空管微视类型页面失败,无法进行主栏目编辑'
        self.click_atcmvcinfor_update_topcol_button(test_into_atcmvclassifyinforpage, self.topcol_name)  # 点击编辑按钮
        # self.click_atcmvcinfor_update_topcol_button(test_into_atcmvclassifyinforpage,"仝笠窟獗捺日廛烈窳陉" )
        assert self.assert_page_atcmvcinfor_update_textcontent(
            test_into_atcmvclassifyinforpage), '进入空管微视主栏目类型修改界面失败'  # 判断是否打开修改界面
        logger.info('进入空管微视主栏目类型修改界面成功')
        message = self.assert_atcmvcinfor_update_textcontent(test_into_atcmvclassifyinforpage, self.topcol_name)
        # message = self.assert_atcmvcinfor_update_textcontent(test_into_atcmvclassifyinforpage, "仝笠窟獗捺日廛烈窳陉")
        assert message[0], message[1]  # 判断回显是否正确
        logger.info(message[1])
        self.atcmvcinfor_topcol_update(test_into_atcmvclassifyinforpage)  # 点击修改
        assert self.assert_update_message_textcontent(test_into_atcmvclassifyinforpage), '空管微视主栏目类型修改失败'  # 判断是否修改成功
        logger.info('空管微视主栏目类型修改成功')

    #@pytest.mark.skip()
    def test_block_up_atcmvclassifyinfor_topcol(self, test_into_atcmvclassifyinforpage):
        '''停用空管微视顶级栏目'''
        assert test_into_atcmvclassifyinforpage, '进入空管微视类型页面失败,无法进行顶级栏目停用'
        self.atcmvcinfor_block_up_table_topcol_button_click(test_into_atcmvclassifyinforpage,
                                                            self.topcol_name)  # 点击停用按钮
        logger.info('点击停用按钮')
        assert self.assert_atcmvcinfor_block_up_topcol_alert_textcontent(
            test_into_atcmvclassifyinforpage), '弹出置顶对话框失败'  # 判断是否弹出停用对话框
        logger.info('已经弹出置顶对话框')
        self.atcmvcinfor_block_up_topcol_alert_submit_button_click(test_into_atcmvclassifyinforpage)  # 点击确定按钮
        assert self.assert_atcmvcinfor_block_up_topcol_message_textcontent(
            test_into_atcmvclassifyinforpage), '空管微视顶级栏目停用失败'  # 判断是否停用成功
        logger.info('空管微视顶级栏目停用成功')

    #@pytest.mark.skip()
    def test_start_using_atcmvclassifyinfor_topcol(self, test_into_atcmvclassifyinforpage):
        '''启用空管微视顶级栏目'''
        assert test_into_atcmvclassifyinforpage, '进入空管微视类型页面失败,无法进行顶级栏目启用'
        self.atcmvcinfor_start_using_table_topcol_button_click(test_into_atcmvclassifyinforpage,
                                                               self.topcol_name)  # 点击启用按钮
        logger.info('点击启用按钮')
        assert self.assert_atcmvcinfor_start_using_topcol_alert_textcontent(
            test_into_atcmvclassifyinforpage), '弹出启用对话框失败'  # 判断是否弹出启用对话框
        logger.info('已经弹出启用对话框')
        self.atcmvcinfor_start_using_topcol_alert_submit_button_click(test_into_atcmvclassifyinforpage)  # 点击确定按钮
        assert self.assert_atcmvcinfor_start_using_topcol_message_textcontent(
            test_into_atcmvclassifyinforpage), '空管微视顶级栏目启用失败'  # 判断是否启用成功
        logger.info('空管微视顶级栏目启用成功')

    #@pytest.mark.skip()
    def test_add_atcmvclassifyinfor_soncol(self, test_into_atcmvclassifyinforpage):
        '''新增空管微视子栏目'''
        assert test_into_atcmvclassifyinforpage, '进入空管微视类型页面失败,无法进行子栏目添加'
        self.click_atcmvcinfor_add_soncol_button(test_into_atcmvclassifyinforpage, self.topcol_name)  # 点击添加子栏目按钮
        assert self.assert_atcmvcinfor_add_soncol_page_textcontent(
            test_into_atcmvclassifyinforpage), '进入空管微视子栏目添加界面失败'  # 判断是否打开新增界面
        logger.info('进入空管微视子栏目添加界面成功')
        self.atcmvcinfor_soncol_add(test_into_atcmvclassifyinforpage, self.soncol_name)  # 新增空管微视子栏目
        assert self.assert_atcmvcinfor_soncol_add_message_textcontent(
            test_into_atcmvclassifyinforpage), '子栏目新增失败'  # 验证是否添加成功
        logger.info('子栏目新增成功')

    #@pytest.mark.skip()
    def test_update_atcmvclassifyinfor_soncol(self, test_into_atcmvclassifyinforpage):
        '''修改空管微视子栏目'''
        assert test_into_atcmvclassifyinforpage, '进入空管微视类型页面失败,无法进行子栏目编辑'
        self.click_atcmvcinfor_update_topcol_button(test_into_atcmvclassifyinforpage, self.soncol_name)  # 点击编辑按钮
        # self.click_atcmvcinfor_update_topcol_button(test_into_atcmvclassifyinforpage,"仝笠窟獗捺日廛烈窳陉" )
        assert self.assert_page_atcmvcinfor_update_textcontent(
            test_into_atcmvclassifyinforpage), '进入空管微视子栏目类型修改界面失败'  # 判断是否打开修改界面
        logger.info('进入空管微视子栏目类型修改界面成功')
        message = self.assert_atcmvcinfor_update_textcontent(test_into_atcmvclassifyinforpage, self.soncol_name)
        # message = self.assert_atcmvcinfor_update_textcontent(test_into_atcmvclassifyinforpage, "仝笠窟獗捺日廛烈窳陉")
        assert message[0], message[1]  # 判断回显是否正确
        logger.info(message[1])
        self.atcmvcinfor_topcol_update(test_into_atcmvclassifyinforpage)  # 点击修改
        assert self.assert_update_message_textcontent(test_into_atcmvclassifyinforpage), '空管微视子栏目类型修改失败'  # 判断是否修改成功
        logger.info('空管微视子栏目类型修改成功')

    #@pytest.mark.skip()
    def test_block_up_atcmvclassifyinfor_soncol(self, test_into_atcmvclassifyinforpage):
        '''停用空管微视子栏目'''
        assert test_into_atcmvclassifyinforpage, '进入空管微视类型页面失败,无法进行子栏目停用'
        self.atcmvcinfor_block_up_table_topcol_button_click(test_into_atcmvclassifyinforpage,
                                                            self.soncol_name)  # 点击停用按钮
        logger.info('点击停用按钮')
        assert self.assert_atcmvcinfor_block_up_topcol_alert_textcontent(
            test_into_atcmvclassifyinforpage), '弹出置顶对话框失败'  # 判断是否弹出停用对话框
        logger.info('已经弹出置顶对话框')
        self.atcmvcinfor_block_up_topcol_alert_submit_button_click(test_into_atcmvclassifyinforpage)  # 点击确定按钮
        assert self.assert_atcmvcinfor_block_up_topcol_message_textcontent(
            test_into_atcmvclassifyinforpage), '空管微视子栏目停用失败'  # 判断是否停用成功
        logger.info('空管微视子栏目停用成功')

    #@pytest.mark.skip()
    def test_start_using_atcmvclassifyinfor_soncol(self, test_into_atcmvclassifyinforpage):
        '''启用空管微视子栏目'''
        assert test_into_atcmvclassifyinforpage, '进入空管微视类型页面失败,无法进行子栏目启用'
        self.atcmvcinfor_start_using_table_topcol_button_click(test_into_atcmvclassifyinforpage,
                                                               self.soncol_name)  # 点击启用按钮
        logger.info('点击启用按钮')
        assert self.assert_atcmvcinfor_start_using_topcol_alert_textcontent(
            test_into_atcmvclassifyinforpage), '弹出启用对话框失败'  # 判断是否弹出启用对话框
        logger.info('已经弹出启用对话框')
        self.atcmvcinfor_start_using_topcol_alert_submit_button_click(test_into_atcmvclassifyinforpage)  # 点击确定按钮
        assert self.assert_atcmvcinfor_start_using_topcol_message_textcontent(
            test_into_atcmvclassifyinforpage), '空管微视子栏目启用失败'  # 判断是否启用成功
        logger.info('空管微视子栏目启用成功')

    @pytest.fixture(scope="function")
    def test_into_atcmvlistinforpage(self, login):
        '''进入空管微视列表页面'''
        if login:
            '''用例：登录之后，点击资讯管理，点击空管微视，点击空管微视列表，进入空管微视列表页面'''
            try:
                # 退出iframe
                login.switch_to_default_iframe()
                # 进入空管微视列表页面
                self.into_atcmvlistinfor_page(login)
                time.sleep(2)
                # 定位iframe,并且进入iframe
                self.into_atcmvlinfor_iframe(login)
                # 在空管微视列表页面，查找空管微视列表验证信息
                if self.assert_atcmvlinfor_page_textcontent(login):
                    logger.info('进入空管微视列表页面成功')
                    yield login
                    assert True, '进入空管微视列表页面成功'
                    print('所有类的用例执行完毕,执行后置操作')
                    login.switch_to_default_iframe()  # 退出iframe
                    self.click_atcmvlinfor_tab_close_button(login)  # 点击tab关闭按钮
                    logger.info("关闭空管微视列表tab")
                    time.sleep(1)
                    self.click_airtrafficcontrol_mv_management(login)  # 点击tab关闭按钮
                    logger.info("点击空管微视，收回下拉菜单")
                    time.sleep(1)
                    self.click_information_management(login)  # 点击咨询管理，收回下拉菜单
                    logger.info("点击咨询管理，收回下拉菜单")
                    time.sleep(1)
                else:
                    yield False
                    logger.info('进入空管微视列表页面失败')
                    assert False, '进入空管微视列表页面失败'
            except Exception as  e:
                logger.info('进入空管微视列表页面失败')
                assert False, '进入空管微视列表页面失败'

    #@pytest.mark.skip()
    def test_add_atcmvlistinfor(self, test_into_atcmvlistinforpage):
        '''新增空管微视'''
        assert test_into_atcmvlistinforpage, '进入空管微视列表页面失败,无法进行添加'
        self.select_atcmvlinfor_classify(test_into_atcmvlistinforpage, self.soncol_name)  # 选择指定内容树形节点，空管微视分类
        time.sleep(2)
        old_number = self.assert_atcmvlinfor_table_number_text(test_into_atcmvlistinforpage)  # 获取新增前的总数
        self.click_atcmvlinfor_add_button(test_into_atcmvlistinforpage)  # 点击新增按钮
        assert self.assert_atcmvlinfor_page_add_textcontent(test_into_atcmvlistinforpage,
                                                            self.soncol_name), '进入空管微视添加界面失败'  # 判断是否打开新增界面
        logger.info('进入空管微视添加界面成功')
        if self.assert_atcmvlinfor_add_time_textcontent(test_into_atcmvlistinforpage):
            self.atcmvlinfor_add(test_into_atcmvlistinforpage, self.atcmv_name, self.atcmv_time, self.atcmv_vedio,
                                 self.atcmv_size, self.atcmv_editor,'1')  # 新增空管微视
        else:
            self.atcmvlinfor_add(test_into_atcmvlistinforpage, self.atcmv_name, self.atcmv_time, self.atcmv_vedio,
                                 self.atcmv_size, self.atcmv_editor,'0')  # 新增空管微视
        assert self.assert_atcmvlinfor_add_message_textcontent(test_into_atcmvlistinforpage),'空管微视新增失败'
        logger.info('空管微视新增成功')
        self.into_atcmvlinfor_iframe(test_into_atcmvlistinforpage) #切换空管微视到iframe
        new_number = self.assert_atcmvlinfor_table_number_text(test_into_atcmvlistinforpage)  # 添加后获取数据总数
        # 验证是否添加成功
        assert eval(new_number) == eval(old_number) + 1, '空管微视信息增加前总数是{0}，信息增加后总数是{1},新增失败'.format(old_number,
                                                                                                   new_number)
        logger.info('空管微视信息增加前总数是{0}，信息增加后总数是{1},新增成功'.format(old_number, new_number))

    @pytest.fixture(scope="function")
    def test_query_atcmvlistinfor(self, test_into_atcmvlistinforpage):
        '''查询空管微视'''
        assert test_into_atcmvlistinforpage, '没有进入空管微视界面，不执行查询用例'
        # test_into_atcmvlistinforpage.switch_to_default_iframe()  # 退出iframe
        # self.menu_atcmvlistinfor_double_click(test_into_atcmvlistinforpage)  # 点击导航栏，重置
        # self.into_atcmvlinfor_iframe(test_into_atcmvlistinforpage)  # 定位iframe,并且进入iframe
        self.select_atcmvlinfor_classify(test_into_atcmvlistinforpage, self.soncol_name)  # 选择指定内容树形节点，空管微视分类
        self.atcmvlinfor_query(test_into_atcmvlistinforpage, self.atcmv_name)  # 查询空管微视
        logger.info('点击了查询按钮')
        time.sleep(2)
        table_number_text = self.assert_atcmvlinfor_table_number_text(test_into_atcmvlistinforpage)
        query_str = "SELECT * FROM sp_edu_material em, sp_edu_material_category emc WHERE em.material_cat=emc.cat_id and em.material_title like '%"+self.atcmv_name+"%' and emc.cat_name = '"+self.soncol_name+"'"
        db_query_res = execute_web(query_str)
        if int(table_number_text) == len(db_query_res):
            logger.info('查询正确:table结果数{0}：数据库查询结果数{1}'.format(table_number_text, len(db_query_res)))  # 获取查询数量
            yield test_into_atcmvlistinforpage
            assert True, '查询正确：table结果数{0}：数据库查询结果数{1}'.format(table_number_text, len(db_query_res))
        else:
            logger.info('查询失败：table结果数{0}：数据库查询结果数{1}'.format(table_number_text, len(db_query_res)))
            yield False
            assert False, '查询失败：table结果数{0}：数据库查询结果数{1}'.format(table_number_text, len(db_query_res))

    def test_update_atcmvlistinfor(self, test_query_atcmvlistinfor):
        '''修改空管微视'''
        assert test_query_atcmvlistinfor, '没有查询,无法进行修改'
        self.atcmvlinfor_update_button_click(test_query_atcmvlistinfor)  # 点击编辑按钮
        assert self.assert_atcmvlinfor_page_update_textcontent(test_query_atcmvlistinfor,self.soncol_name),'进入空管微视修改界面失败'
        logger.info('进入了空管微视编辑页面')
        message = self.assert_atcmvlinfor_update_textcontent(test_query_atcmvlistinfor, self.atcmv_name, self.atcmv_editor)  # 校验详情信息
        assert message[0],message[1]
        logger.info(message[1])
        self.atcmvlinfor_update_submit_button_click(test_query_atcmvlistinfor)  # 不修改任何内容，直接提交
        assert self.assert_atcmvlinfor_update_message_textcontent(test_query_atcmvlistinfor), '空管微视编辑失败' # 判断是否修改成功
        logger.info('空管微视编辑成功')

    def test_detail_atcmvlistinfor(self, test_query_atcmvlistinfor):
        '''空管微视详情'''
        assert test_query_atcmvlistinfor, '没有查询,无法进行详情'
        self.atcmvlinfor_detail_button_click(test_query_atcmvlistinfor)  # 点击详情按钮
        logger.info('点击了详情按钮')
        assert self.assert_atcmvlinfor_page_detail_textcontent(test_query_atcmvlistinfor,self.soncol_name),'进入空管微视详情界面失败'  # 判断是否打开详情界面
        logger.info('进入了空管微视详情页面')
        message = self.assert_atcmvlinfor_detail_textcontent(test_query_atcmvlistinfor, self.atcmv_name, self.atcmv_editor)  # 校验详情信息
        assert message[0], message[1]
        logger.info(message[1])
        self.atcmvlinfor_detail_return_click(test_query_atcmvlistinfor)  # 点击返回按钮


    def test_top_atcmvlistinfor(self, test_query_atcmvlistinfor):
        '''空管微视置顶'''
        assert test_query_atcmvlistinfor, '没有查询,无法进行置顶'
        self.atcmvlinfor_top_button_click(test_query_atcmvlistinfor)  # 点击一个置顶按钮
        assert self.assert_atcmvlinfor_top_alert_textcontent(test_query_atcmvlistinfor), '没有弹出置顶对话框' # 判断是否弹出置顶对话框
        logger.info('已经弹出置顶对话框')
        self.atcmvlinfor_top_alert_submit_button_click(test_query_atcmvlistinfor)  # 点击确定按钮
        time.sleep(1)
        assert self.assert_atcmvlinfor_top_message_textcontent(test_query_atcmvlistinfor), '空管微视置顶失败'  # 判断是否置顶成功
        logger.info('空管微视置顶成功')

    def test_topcancel_atcmvlistinfor(self, test_query_atcmvlistinfor):
        '''空管微视取消置顶'''
        assert test_query_atcmvlistinfor, '没有查询,无法进行取消置顶'
        self.atcmvlinfor_canceltop_button_click(test_query_atcmvlistinfor)  # 点击一个取消置顶按钮
        assert self.assert_atcmvlinfor_canceltop_alert_textcontent(test_query_atcmvlistinfor), '没有弹出取消置顶对话框'  # 判断是否弹出取消置顶对话框
        logger.info('已经弹出取消置顶对话框')
        self.atcmvlinfor_canceltop_alert_submit_button_click(test_query_atcmvlistinfor)  # 点击确定按钮
        assert self.assert_atcmvlinfor_canceltop_message_textcontent(test_query_atcmvlistinfor), '空管微视取消置顶失败'  # 判断是否取消置顶成功
        logger.info('空管微视取消置顶成功')


    def test_delete_atcmvlistinfor(self, test_query_atcmvlistinfor):
        '''空管微视删除'''
        assert test_query_atcmvlistinfor, '没有查询,无法进行删除'
        self.atcmvlinfor_delete_button_click(test_query_atcmvlistinfor)  # 点击删除按钮
        logger.info('点击了删除按钮')
        assert self.assert_atcmvlinfor_delete_alert_textcontent(test_query_atcmvlistinfor), '没有弹出删除对话框' # 判断是否弹出删除对话框
        logger.info('弹出了删除对话框')
        self.atcmvlinfor_delete_alert_submit_button_click(test_query_atcmvlistinfor)  # 点击确定按钮
        assert self.assert_delete_message_textcontent(test_query_atcmvlistinfor), '空管微视删除失败'  # 判断是否删除成功
        logger.info('空管微视删除成功')


    #@pytest.mark.skip()
    def test_delete_atcmvclassifyinfor_soncol(self, test_into_atcmvclassifyinforpage):
        '''删除空管微视子栏目'''
        assert test_into_atcmvclassifyinforpage,'没有进入空管微视类型界面，不执行删除用例'
        self.atcmvcinfor_block_up_table_topcol_button_click(test_into_atcmvclassifyinforpage,
                                                           self.soncol_name)  # 点击停用按钮
        self.atcmvcinfor_block_up_topcol_alert_submit_button_click(test_into_atcmvclassifyinforpage)  # 点击确定按钮，停用后出现删除按钮
        time.sleep(2)
        self.atcmvcinfor_delete_button_click(test_into_atcmvclassifyinforpage,self.soncol_name)  # 点击删除按钮
        logger.info('点击了删除按钮')
        assert self.assert_atcmvcinfor_delete_alert_textcontent(test_into_atcmvclassifyinforpage),'没有弹出删除对话框'  # 判断是否弹出删除对话框
        logger.info('弹出了删除对话框')
        self.atcmvcinfor_delete_alert_submit_button_click(test_into_atcmvclassifyinforpage)  # 点击确定按钮
        assert self.assert_delete_message_textcontent(test_into_atcmvclassifyinforpage),'子栏目删除失败'  # 判断是否删除成功
        logger.info('子栏目删除成功')

    #@pytest.mark.skip()
    def test_delete_atcmvclassifyinfor_topcol(self, test_into_atcmvclassifyinforpage):
        '''删除空管微视顶级栏目'''
        assert test_into_atcmvclassifyinforpage, '没有进入空管微视类型界面，不执行删除用例'
        self.atcmvcinfor_block_up_table_topcol_button_click(test_into_atcmvclassifyinforpage,
                                                            self.topcol_name)  # 点击停用按钮
        self.atcmvcinfor_block_up_topcol_alert_submit_button_click(test_into_atcmvclassifyinforpage)  # 点击确定按钮，停用后出现删除按钮
        time.sleep(2)
        self.atcmvcinfor_delete_button_click(test_into_atcmvclassifyinforpage, self.topcol_name)  # 点击删除按钮
        logger.info('点击了删除按钮')
        assert self.assert_atcmvcinfor_delete_alert_textcontent(
            test_into_atcmvclassifyinforpage), '没有弹出删除对话框'  # 判断是否弹出删除对话框
        logger.info('弹出了删除对话框')
        self.atcmvcinfor_delete_alert_submit_button_click(test_into_atcmvclassifyinforpage)  # 点击确定按钮
        assert self.assert_delete_message_textcontent(test_into_atcmvclassifyinforpage), '顶级栏目删除失败'  # 判断是否删除成功
        logger.info('顶级栏目删除成功')
