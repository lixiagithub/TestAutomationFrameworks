# coding = utf-8
# Author:李昰 
# Date：2021/1/13 10:47
from selenium.webdriver.common.by import By
import time
class Menu():
    menu_scrollBar = (By.XPATH, '// *[ @ id = "wrapper"] / nav / div[3] / div[2]')  # 菜单div滚动条

    menu_system_management_dom = '#side-menu > li:nth-child(12)'  # 系统管理document定位
    menu_system_management = (By.XPATH, '//*[@id="side-menu"]/li[12]')  # 主菜单系统管理
    menu_user_management_dom = '#side-menu > li.active > ul > li:nth-child(5) > a'  # 用户管理document定位
    menu_user_management = (By.XPATH, '//*[@id="side-menu"]/li[12]/ul/li[5]')  # 用户管理

    menu_information_management_dom = '#side-menu > li:nth-child(3)'  # 资讯管理document定位
    menu_information_management = (By.XPATH, '//*[@id="side-menu"]/li[3]')  # 主菜单资讯管理
    menu_atcinfor_management_dom = '#side-menu > li.active > ul > li:nth-child(1) > a'  # 空管资讯管理document定位
    menu_atcinfor_management = (By.XPATH, '//*[@id="side-menu"]/li[3]/ul/li[1]')  # 空管资讯管理

    '''封装点击用户管理子菜单，进入用户管理页面'''
    def into_user_page(self, openbrowser):
        openbrowser.execute_js_scroll(Menu.menu_system_management_dom)  # 滚动条滑动到系统管理菜单处
        openbrowser.click_my(Menu.menu_system_management)  # 点击主菜单系统管理
        openbrowser.execute_js_scroll(Menu.menu_user_management_dom)  # 滚动条滑动到用户管理子菜单处
        openbrowser.click_my(Menu.menu_user_management)  # 点击用户管理子菜单

    '''封装点击空管资讯子菜单，进入空管资讯页面'''
    def into_atcinfor_page(self, openbrowser):
        openbrowser.execute_js_scroll(Menu.menu_information_management_dom)  # 滚动条滑动主菜单资讯管理处
        openbrowser.click_my(Menu.menu_information_management)  # 点击主菜单资讯管理
        openbrowser.execute_js_scroll(Menu.menu_atcinfor_management_dom)  # 滚动条滑动到用户管理子菜单处
        openbrowser.click_my(Menu.menu_atcinfor_management)  # 点击空管资讯子菜单