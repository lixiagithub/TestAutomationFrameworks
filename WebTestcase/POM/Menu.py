# coding = utf-8
# Author:李昰 
# Date：2021/1/13 10:47
from selenium.webdriver.common.by import By

class Menu():
    menu_scrollBar = (By.XPATH, '// *[ @ id = "wrapper"] / nav / div[3] / div[2]')  # 菜单div滚动条

    menu_system_management = (By.XPATH, '//*[@id="side-menu"]/li[11]/a')  # 主菜单系统管理
    menu_user_management_dom = '#side-menu > li.active > ul > li:nth-child(5) > a'  # 用户管理document定位
    menu_user_management = (By.XPATH, '//*[@id="side-menu"]/li[11]/ul/li[5]')  # 用户管理


    '''封装点击用户管理子菜单，进入用户管理页面'''
    def into_user_page(self, openbrowser):
        openbrowser.click_my(Menu.menu_system_management)  # 点击主菜单系统管理
        openbrowser.execute_js_scroll(Menu.menu_user_management_dom)  # 滚动条滑动到用户管理子菜单处
        openbrowser.click_my(Menu.menu_user_management)  # 点击用户管理子菜单
