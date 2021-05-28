# coding = utf-8
# Author:李昰 
# Date：2021/1/13 10:47
from selenium.webdriver.common.by import By
import time
class Menu():
    menu_scrollBar = (By.XPATH, '// *[ @ id = "wrapper"] / nav / div[3] / div[2]')  # 菜单div滚动条

    menu_system_management_dom = '#side-menu > li:nth-child(12)'  # 系统管理document定位
    menu_system_management = (By.XPATH, '//*[@id="side-menu"]/li[12]/a')  # 主菜单系统管理
    menu_user_management_dom = '#side-menu > li.active > ul > li:nth-child(5) > a'  # 用户管理document定位
    menu_user_management = (By.XPATH, '//*[@id="side-menu"]/li[12]/ul/li[5]/a')  # 用户管理

    menu_information_management_dom = '#side-menu > li:nth-child(3)'  # 资讯管理document定位
    menu_information_management = (By.XPATH, '/html/body/div[2]/nav/div[3]/div[1]/ul/li[3]/a')  # 主菜单资讯管理
    menu_atcinfor_management_dom = '#side-menu > li.active > ul > li:nth-child(1) > a'  # 空管资讯管理document定位
    menu_atcinfor_management = (By.XPATH, '/html/body/div[2]/nav/div[3]/div[1]/ul/li[3]/ul/li[1]/a')  # 空管资讯管理
    menu_party_building_dynamic_dom = '#side-menu > li.active > ul > li:nth-child(2) > a'  # 党建动态管理document定位
    menu_party_building_dynamic = (By.XPATH, '/html/body/div[2]/nav/div[3]/div[1]/ul/li[3]/ul/li[2]/a')  # 党建动态管理
    menu_public_notification_dom = '#side-menu > li.active > ul > li:nth-child(3) > a'  # 公示通报管理document定位
    menu_public_notification = (By.XPATH, '/html/body/div[2]/nav/div[3]/div[1]/ul/li[3]/ul/li[3]/a')  # 公示通报管理
    menu_airtrafficcontrol_press_dom = '#side-menu > li.active > ul > li:nth-child(4) > a'  # 空管报刊管理document定位
    menu_airtrafficcontrol_press = (By.XPATH, '/html/body/div[2]/nav/div[3]/div[1]/ul/li[3]/ul/li[4]/a')  # 空管报刊管理
    menu_airtrafficcontrol_mv_dom = '#side-menu > li.active > ul > li:nth-child(6) > a'  # 空管微视管理document定位
    menu_airtrafficcontrol_mv = (By.XPATH, '/html/body/div[2]/nav/div[3]/div[1]/ul/li[3]/ul/li[6]/a')  # 空管微视管理document定位
    menu_airtrafficcontrol_mvlist_dom = '#side-menu > li.active > ul > li.active > ul > li:nth-child(1) > a'  # 空管微视列表dom
    menu_airtrafficcontrol_mvlist = (By.XPATH, '/html/body/div[2]/nav/div[3]/div[1]/ul/li[3]/ul/li[6]/ul/li[1]/a')  # 空管微视列表
    menu_airtrafficcontrol_mvclassify_dom = '#side-menu > li.active > ul > li.active > ul > li:nth-child(2) > a'  # 空管微视类型
    menu_airtrafficcontrol_mvclassify = (By.XPATH, '/html/body/div[2]/nav/div[3]/div[1]/ul/li[3]/ul/li[6]/ul/li[2]/a')  # 空管微视类型

    '''封装点击用户管理子菜单，进入用户管理页面'''
    def into_user_page(self, openbrowser):
        openbrowser.execute_js_scroll(Menu.menu_system_management_dom)  # 滚动条滑动到系统管理菜单处
        openbrowser.click_my(Menu.menu_system_management)  # 点击主菜单系统管理
        openbrowser.execute_js_scroll(Menu.menu_user_management_dom)  # 滚动条滑动到用户管理子菜单处
        openbrowser.click_my(Menu.menu_user_management)  # 点击用户管理子菜单

    def click_information_management(self,openbrowser):
        '''封装点击主菜单资讯管理'''
        openbrowser.execute_js_scroll(Menu.menu_information_management_dom)  # 滚动条滑动主菜单资讯管理处
        openbrowser.click_my(Menu.menu_information_management)  # 点击主菜单资讯管理

    '''封装点击空管资讯子菜单，进入空管资讯页面'''
    def into_atcinfor_page(self, openbrowser):
        openbrowser.execute_js_scroll(Menu.menu_information_management_dom)  # 滚动条滑动主菜单资讯管理处
        openbrowser.click_my(Menu.menu_information_management)  # 点击主菜单资讯管理
        openbrowser.execute_js_scroll(Menu.menu_atcinfor_management_dom)  # 滚动条滑动到用户管理子菜单处
        openbrowser.click_my(Menu.menu_atcinfor_management)  # 点击空管资讯子菜单

    '''封装点击党建动态子菜单，进入党建动态页面'''
    def into_pbdinfor_page(self, openbrowser):
        openbrowser.execute_js_scroll(Menu.menu_information_management_dom)  # 滚动条滑动主菜单资讯管理处
        openbrowser.click_my(Menu.menu_information_management)  # 点击主菜单资讯管理
        openbrowser.execute_js_scroll(Menu.menu_party_building_dynamic_dom)  # 滚动条滑动到党建动态管理子菜单处
        openbrowser.click_my(Menu.menu_party_building_dynamic)  # 点击党建动态子菜单

    '''封装点击公示通报子菜单，进入公示通报页面'''
    def into_pninfor_page(self, openbrowser):
        openbrowser.execute_js_scroll(Menu.menu_information_management_dom)  # 滚动条滑动主菜单资讯管理处
        openbrowser.click_my(Menu.menu_information_management)  # 点击主菜单资讯管理
        openbrowser.execute_js_scroll(Menu.menu_public_notification_dom)  # 滚动条滑动到公示通报管理子菜单处
        openbrowser.click_my(Menu.menu_public_notification)  # 点击公示通报子菜单

    def menu_public_notification_double_click(self,openbrowser):
        '''封装双击公示通报'''
        openbrowser.double_click_my(Menu.menu_public_notification) # 双击公示通报子菜单

    '''封装点击空管报刊子菜单，进入空管报刊页面'''
    def into_atcpinfor_page(self, openbrowser):
        openbrowser.execute_js_scroll(Menu.menu_information_management_dom)  # 滚动条滑动主菜单资讯管理处
        openbrowser.click_my(Menu.menu_information_management)  # 点击主菜单资讯管理
        openbrowser.execute_js_scroll(Menu.menu_airtrafficcontrol_press_dom)  # 滚动条滑动到空管报刊管理子菜单处
        openbrowser.click_my(Menu.menu_airtrafficcontrol_press)  # 点击空管报刊子菜单

    def menu_atcpinfor_double_click(self,openbrowser):
        '''封装双击空管报刊'''
        openbrowser.double_click_my(Menu.menu_airtrafficcontrol_press) # 双击空管报刊子菜单

    def click_airtrafficcontrol_mv_management(self,openbrowser):
        '''封装点击子菜单空管微视'''
        openbrowser.execute_js_scroll(Menu.menu_airtrafficcontrol_mv_dom)  # 滚动条滑动子菜单空管微视处
        openbrowser.click_my(Menu.menu_airtrafficcontrol_mv)  # 点击子菜单空管微视

    '''封装点击空管微视列表子菜单，进入空管微视列表页面'''
    def into_atcmvlistinfor_page(self, openbrowser):
        openbrowser.js_element_top(Menu.menu_information_management)  # 滚动条滑动主菜单资讯管理处
        openbrowser.click_my(Menu.menu_information_management)  # 点击主菜单资讯管理
        openbrowser.js_element_top(Menu.menu_airtrafficcontrol_mv)  # 滚动条滑动到空管微视子菜单处
        openbrowser.click_my(Menu.menu_airtrafficcontrol_mv)  # 点击空管微视子菜单
        openbrowser.js_element_top(Menu.menu_airtrafficcontrol_mvlist)  # 滚动条滑动到空管微视列表处
        openbrowser.click_my(Menu.menu_airtrafficcontrol_mvlist)  # 点击空管微视列表子菜单


    def menu_atcmvlistinfor_double_click(self,openbrowser):
        '''封装双击空管微视列表'''
        openbrowser.double_click_my(Menu.menu_airtrafficcontrol_mvlist) # 双击空管微视列表子菜单

    '''封装点击空管微视类型子菜单，进入空管微视类型页面'''
    def into_atcmvclassifyinfor_page(self, openbrowser):
        openbrowser.js_element_top(Menu.menu_information_management)  # 滚动条滑动主菜单资讯管理处
        openbrowser.click_my(Menu.menu_information_management)  # 点击主菜单资讯管理
        openbrowser.js_element_top(Menu.menu_airtrafficcontrol_mv)  # 滚动条滑动到空管微视子菜单处
        openbrowser.click_my(Menu.menu_airtrafficcontrol_mv)  # 点击空管微视子菜单
        openbrowser.js_element_top(Menu.menu_airtrafficcontrol_mvclassify)  # 滚动条滑动到空管微视类型处
        openbrowser.click_my(Menu.menu_airtrafficcontrol_mvclassify)  # 点击空管微视类型子菜单


    def menu_atcmvclassifyinfor_double_click(self,openbrowser):
        '''封装双击空管微视类型'''
        openbrowser.double_click_my(Menu.menu_airtrafficcontrol_mvclassify) # 双击空管微视类型子菜单