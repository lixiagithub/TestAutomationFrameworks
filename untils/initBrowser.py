from selenium import webdriver
from untils.readYaml import baseConfig
from selenium.webdriver.common.action_chains import ActionChains  # 导入鼠标事件
from selenium.webdriver.support import expected_conditions as EC  # 导入EC判断方法
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait  # 导入 显示等待
from log.log import logger
import allure
import random  # 导入随机选取
import time  # 导入强制等待时间
from selenium.webdriver.support.ui import Select  # 导入下拉列表定位


# def browsertype(host,browser):
#     '''
#     根据yaml配置文件，初始化浏览器
#     类型，运行环境，用例的url
#     :return: 浏览器对象
#     '''
#     if baseConfig.browser['env']=='docker':
#         print('开始启动docker模式')
#         # chrome_capabilities = {
#         #     "browserName": "chrome",
#         # }
#         # driver = webdriver.Remote("http://132.138.7.132:5555/wd/hub", desired_capabilities=chrome_capabilities)
#
#         desired_capabilities = {
#              'platform': 'ANY',
#              'browserName': browser,
#              'version': '',
#              'javascriptEnabled': True
#         }
#         driver = webdriver.Remote(host, desired_capabilities=desired_capabilities)
#
#     else:
#         options=webdriver.ChromeOptions()#谷歌浏览器的可选项对象
#         if baseConfig.browser['env']=='headless':
#             options.add_argument('headless')
#         if baseConfig.browser['type']=='chrome':
#             driver=webdriver.Chrome(options=options,executable_path=baseConfig.chrome_driver_path)
#         elif baseConfig.browser['type']=='firefox':
#             driver=webdriver.Firefox(executable_path=baseConfig.firefox_driver_path)
#         elif baseConfig.browser['type']=='ie':
#             driver=webdriver.Ie()
#         else:
#             raise ('没有支持的浏览器类型{}'.format(baseConfig.browser['type']))
#     driver.get(baseConfig.ui['test'])
#     driver.maximize_window()  # 浏览器最大化
#     driver.save_screenshot(baseConfig.picturePath+r'\login.png')
#     return driver
def browsertype():
    '''
    根据yaml配置文件，初始化浏览器
    类型，运行环境，用例的url
    :return: 浏览器对象
    '''
    if baseConfig.browser['env'] == 'docker':
        print('开始启动docker模式')
        chrome_capabilities = {
            "browserName": "chrome",
        }
        driver = webdriver.Remote("http://132.138.7.132:5555/wd/hub", desired_capabilities=chrome_capabilities)
    else:
        options = webdriver.ChromeOptions()  # 谷歌浏览器的可选项对象
        if baseConfig.browser['env'] == 'headless':
            options.add_argument('headless')
        if baseConfig.browser['type'] == 'chrome':
            driver = webdriver.Chrome(options=options, executable_path=baseConfig.chrome_driver_path)
        elif baseConfig.browser['type'] == 'firefox':
            driver = webdriver.Firefox(executable_path=baseConfig.firefox_driver_path)
        elif baseConfig.browser['type'] == 'ie':
            driver = webdriver.Ie()
        else:
            raise ('没有支持的浏览器类型{}'.format(baseConfig.browser['type']))
    driver.get(baseConfig.ui['test'])
    driver.maximize_window()  # 浏览器最大化
    driver.save_screenshot(baseConfig.picturePath + r'\login.png')
    return driver


class BrowserInit():
    '''封装浏览器常用操作：
    等待时间
    log
    错误截图

    '''

    def __init__(self, driver):
        self.driver = driver

    def until_element_visible(self, loc):
        '''等待元素出现'''
        wait_time = 10
        try:
            element = WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(loc))
        except Exception as e:
            logger.info('{0}个元素超过了{1}秒未找到'.format(loc[1], wait_time))
            self.add_fail_picture()
            # raise e
            element = None
        return element

    def until_elements_visible(self, loc):
        '''一个元素在页面上出现的次数'''
        wait_time = 10
        try:
            elements = WebDriverWait(self.driver, wait_time).until(lambda x: x.find_elements(*loc))
            return elements
        except Exception as e:
            logger.info('{0}个元素超过了{1}秒未找到'.format(loc[1], wait_time))
            self.add_fail_picture()
            # raise e
            elements = []
            return elements

    def send_key_my(self, loc, value):
        '''封装输入框操作'''
        ele = self.until_element_visible(loc)
        logger.info('在{0}：这个元素输入了：{1}'.format(loc[1], value))
        ele.send_keys(value)

    def send_key_my_action(self, loc, value):
        '''封装输入框操作'''
        ele = self.until_element_visible(loc)
        actions = ActionChains(self.driver)
        actions.move_to_element(ele).send_keys(value).perform()
        logger.info('在{0}：这个元素输入了：{1}'.format(loc[1], value))
        ele.send_keys(value)

    def click_my(self, loc):
        '''封装点击操作'''
        ele = self.until_element_visible(loc)
        logger.info('点击了{0}：这个元素'.format(loc[1]))
        ele.click()

    def double_click_my(self, loc):
        '''封装双击操作'''
        ele = self.until_element_visible(loc)
        actions = ActionChains(self.driver)
        actions.double_click(ele).perform()
        logger.info('双击这个元素：{0}'.format(loc[1]))

    def find_my(self, loc):
        '''封装找到元素操作'''
        ele = self.until_element_visible(loc)
        if ele is not None:
            logger.info('找到{0}：这个元素'.format(loc[1]))
            return ele
        else:
            logger.info('未找到{0}：这个元素'.format(loc[1]))
            return ele

    def random_click_node_js(self):
        '''封装树形节点随机点击操作，返回点击节点的文本'''
        js = "return document.querySelectorAll('[treenode_a]')"
        node = self.driver.execute_script(js)
        ran_node = random.choice(node)  # 随机获取节点
        ran_node_id = ran_node.get_attribute('id')  # 获取节点id
        self.click_my((By.ID, ran_node_id))
        logger.info('点击id为{}的节点'.format(ran_node_id))
        ran_node_text = ran_node.text
        # print('随机点击的树形节点{}'.format(ran_node),ran_node.text)
        return ran_node_text

    def random_click_node(self, loc_li):
        '''封装树形节点随机点击操作，返回点击节点的文本'''
        li_choice_list = self.until_elements_visible(loc_li)  # 定位所有li
        li_choice = random.choice(li_choice_list)
        # print('随机选择的下拉元素{}'.format(li_choice), li_choice.text)
        ran_node_text = li_choice.text
        logger.info('随机选择树形节点文本:{}'.format(ran_node_text))
        my_loc = li_choice.find_element_by_xpath('a')  # 通过li获取a
        # ran_node_id = li_choice.get_attribute('id')  # 获取节点id
        # self.click_my((By.ID, ran_node_id))
        my_loc.click()
        return ran_node_text

    def select_click_node(self, loc_li,loc_text):
        '''直接选择特定内容文本树形节点'''
        li_choice_list = self.until_elements_visible(loc_li)  # 定位指定内容li
        for li_choice in li_choice_list:
            if li_choice.text == loc_text:
                logger.info('选择树形节点文本:{}'.format(loc_text))
                li_choice.click()

    def get_text(self, loc):
        '''返回页面元素的文本'''
        ele = self.until_element_visible(loc)
        t = ""
        if ele is not None:
            t = ele.text
            return t
        else:
            return t

    def get_vlaue(self, loc):
        '''返回页面元素的文本'''
        t = self.until_element_visible(loc).get_attribute("value")
        return t

    def is_text_in_element(self, loc, text):
        '''判断元素文本是否存在'''
        wait_time = 10
        try:
            WebDriverWait(self.driver, wait_time).until(EC.text_to_be_present_in_element(loc, text))
            return True
        except Exception as e:
            logger.info('{0}个元素超过了{1}秒未找到'.format(loc[1], wait_time))
            self.add_fail_picture()
            return False

    def is_alert_persent(self):
        '''判断页面是否有alert弹出框，有返回alert,没有返回False'''
        wait_time = 10
        try:
            result = WebDriverWait(self.driver, timeout=wait_time).until(EC.alert_is_present())
            logger.info('alert已经进入')
            return result
        except Exception as e:
            logger.info('不存在alert')
            self.add_fail_picture()
            return False

    def is_new_window_is_opened(self, current_handles):
        '''判断页面是否有新窗口，有返回True并且切换窗口,没有返回False'''
        wait_time = 10
        result = WebDriverWait(self.driver, timeout=wait_time).until(EC.new_window_is_opened(current_handles))

        if result:
            logger.info('有新窗口，切换成功')
            self.driver.switch_to_window(self.driver.window_handles[-1])
            return True
        else:
            logger.info('没有新窗口')
            return False

    def get_window_handles(self):
        '''获取窗口所有句柄'''
        return self.driver.window_handles

    def mouse_move(self, loc):
        '''鼠标悬停操作'''
        element = self.until_element_visible(loc)
        ActionChains(self.driver).move_to_element(element).perform()

    def mouse_drag_drop(self, f_loc,s_loc):
        '''鼠标拖动操作'''
        f_element = self.until_element_visible(f_loc)
        s_element = self.until_element_visible(s_loc)
        ActionChains(self.driver).drag_and_drop(f_element,s_element).perform()
        logger.info('拖动成功')

    def random_select_pic(self, locs):
        '''随机选择图片'''
        choice_list = self.until_elements_visible(locs)  # 定位所有图片元素
        index = random.randint(1, len(choice_list))
        # choice_loc = random.choice(choice_list)
        # print('随机选择的下拉元素{}'.format(li_choice), li_choice.text)
        self.mouse_move((By.XPATH,
                         '// *[ @ id = "js-grid-juicy-projects"] / div / div / div[{}] / div / div / div / div[1] / img'.format(
                             index)))
        self.click_my((By.XPATH,
                       '// *[ @ id = "js-grid-juicy-projects"] / div / div / div[{}] / div / div / div / div[2] / div / div / a[2]'.format(
                           index)))
        logger.info('随机选择了一张图片的index:{}'.format(index))
        # // *[ @ id = "js-grid-juicy-projects"] / div / div / div[1] / div / div / div / div[1] / img
        # // *[ @ id = "js-grid-juicy-projects"] / div / div / div[2] / div / div / div / div[1] / img
        # // *[ @ id = "js-grid-juicy-projects"] / div / div / div[3] / div / div / div / div[1] / img
        # // *[ @ id = "js-grid-juicy-projects"] / div / div / div[1] / div / div / div / div[2] / div / div / a[2]
        # // *[ @ id = "js-grid-juicy-projects"] / div / div / div[2] / div / div / div / div[2] / div / div / a[2]
        # // *[ @ id = "js-grid-juicy-projects"] / div / div / div[3] / div / div / div / div[2] / div / div / a[2]

    def is_iframe(self, loc):
        '''判断是否存在ifame'''
        wait_time = 10
        boolean = WebDriverWait(self.driver, timeout=wait_time).until(EC.frame_to_be_available_and_switch_to_it(loc))

        if boolean:
            logger.info('{}这个iframe已经进入'.format(loc[1]))
            return True
        else:
            logger.info('{}这个iframe没有进入'.format(loc[1]))
            return False

    def js_window_bom(self):
        '''通过执行js脚本方式将页面置底,参数左边代表左右移动，右边代表上下'''
        js = "window.scrollTo(0,10000);"
        self.driver.execute_script(js)

    def js_window_top(self):
        '''通过执行js脚本方式将页面置顶,参数左边代表左右移动，右边代表上下'''
        js = "window.scrollTo(0,0);"
        self.driver.execute_script(js)

    def js_element_top(self, loc):
        '''通过js脚本方式将指定元素置顶'''
        try:
            self.target = self.until_element_visible(loc)
            self.driver.execute_script("arguments[0].scrollIntoView();", self.target)
        except Exception as msg:
            print("没有定位到该元素，无法置顶：" + str(msg))

    def execute_js_scroll(self, dom):
        '''js滚动条滚动到指定元素'''
        js = "document.querySelector('{}').scrollIntoView()".format(dom)
        self.driver.execute_script(js)
        logger.info('滚动条指定到这个{}元素'.format(dom))

    def execute_js_queryselect_loc(self, dom):
        '''返回定位的元素'''
        js = "return document.querySelector('{}')".format(dom)
        logger.info('通过js返回{}元素'.format(dom))
        return self.driver.execute_script(js)


    def execute_js_queryselect_loc_text(self, dom):
        '''返回定位的元素'''
        js = "return document.querySelector('{}').innerText".format(dom)
        my_text = self.driver.execute_script(js).strip()
        logger.info('通过js返回{0}元素的文本{1}'.format(dom,my_text))
        return my_text

    def execut_js_loc(self, loc):
        if loc[0] == By.CLASS_NAME:
            js = "return document.getElementsByClassName('{}')".format(loc[1])
            if len(self.driver.execute_script(js)) > 0:
                logger.info('js通过ByClassName定位到{}这个元素'.format(loc[1]))
                return True
            else:
                logger.info('js通过ByClassName定位不到{}这个元素'.format(loc[1]))
                return False
        elif loc[0] == By.ID:
            js = "document.getElementById('{}')".format(loc[1])
            if len(self.driver.execute_script(js)) > 0:
                logger.info('js通过ById定位到{}这个元素'.format(loc[1]))
                return True
            else:
                logger.info('js通过ById定位不到{}这个元素'.format(loc[1]))
                return False

    def execut_js_locs(self, loc):
        if loc[0] == By.CLASS_NAME:
            js = "return document.getElementsByClassName('{}')".format(loc[1])
            if len(self.driver.execute_script(js)) > 0:
                logger.info('js通过ByClassName定位到{}这个元素'.format(loc[1]))
                return self.driver.execute_script(js)
            else:
                logger.info('js通过ByClassName定位不到{}这个元素'.format(loc[1]))
                return False
        elif loc[0] == By.ID:
            js = "document.getElementById('{}')".format(loc[1])
            if len(self.driver.execute_script(js)) > 0:
                logger.info('js通过ById定位到{}这个元素'.format(loc[1]))
                return self.driver.execute_script(js)
            else:
                logger.info('js通过ById定位不到{}这个元素'.format(loc[1]))
                return False

    def execute_js(self, js):
        '''执行js'''
        self.driver.execute_script(js)

    def add_fail_picture(self):
        '''
        截图，添加到allure的报告里面去
        :return:
        '''
        file_name = baseConfig.picturePath + r'\test.png'
        self.driver.save_screenshot(file_name)  # 截图函数
        '''allure添加截图附件'''
        with open(file_name, mode='rb') as file:
            f = file.read()  # 读取文件，将读取的结果作为参数传给allure
        allure.attach(f, 'bug', allure.attachment_type.PNG)

    def element_visible_times(self, loc):
        '''验证结果方法'''
        return len(self.until_elements_visible(loc))

    def random_select_ul(self, loc_li):
        '''随机选择下拉列表内容'''
        li_choice_list = self.until_elements_visible(loc_li)  # 定位所有li
        li_choice = random.choice(li_choice_list)
        # print('随机选择的下拉元素{}'.format(li_choice), li_choice.text)
        logger.info('随机选择下拉文本:{}'.format(li_choice.text))
        li_choice.click()

    def select_ul_click(self, loc_li):
        '''直接选择下拉列表特定内容loc'''
        li_choice = self.until_element_visible(loc_li)  # 定位指定li
        # print('随机选择的下拉元素{}'.format(li_choice), li_choice.text)
        logger.info('直接选择下拉文本:{}'.format(li_choice.text))
        li_choice.click()

    def select_ul_content_click(self, loc_li, loc_text):
        '''直接选择下拉列表特定内容文本'''
        li_choice_list = self.until_elements_visible(loc_li)  # 定位指定内容li
        for li_choice in li_choice_list:
            if li_choice.text == loc_text:
                li_choice.click()

    def random_button_click(self, loc):
        '''随机选择多个元素中的一个，进行点击，比如置顶，取消置顶'''
        locs = self.execut_js_locs(loc)  # 定位所有相同元素
        my_choice = random.choice(locs)
        logger.info('随机选择点击:{}'.format(my_choice.text))
        my_choice.click()

    def get_table_total_number(self, loc):
        '''获取表格记录总数'''
        all_text = self.get_text(loc)
        if all_text != "":
            part_text = all_text.split('总共')  # 分割
            total_number = part_text[1].split('条记录')[0]
            return total_number.strip()  # 去掉左右空格
        else:
            return "0"

    def switch_to_default_iframe(self):
        '''退出iframe'''
        self.driver.switch_to.default_content()

    def switch_to_parent_iframe(self):
        '''返回到父iframe'''
        self.driver.switch_to.parent_frame()

    def table_button_click(self,loc_total,loc_name,loc_button,loc_text):
        '''通过新增之后的名称，点击相应的操作按钮
           loc_total:所有符合提交的定位
           loc_name:获取列表中某个字段的定位          
           loc_text:获取列表中某个字段的定位的文本，新增的时候，信息的名称，用于判断
           loc_button:点击操纵区域某个按钮定位
        '''
        my_loc_total = self.until_elements_visible(loc_total)
        for index in range(1,len(my_loc_total)+1):
            my_text=self.execute_js_queryselect_loc_text('#client_table > tbody > tr:nth-child({0}) > {1}'.format(index, loc_name))
            if my_text.split('├─')[1] == loc_text:
                self.execute_js_queryselect_loc('#client_table > tbody > tr:nth-child({0}) > {1}'.format(index, loc_button)).click()



    '''鼠标移动'''


if __name__ == '__main__':
    browsertype()
