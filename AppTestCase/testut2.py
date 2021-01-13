# coding = utf-8
# Author:李昰 
# Date：2021/1/7 14:56
import uiautomator2 as ut2
devices = ut2.connect("f0bc0371")
devices.screen_on()#打开手机
devices.app_stop("com.atnc.vfr")#关闭app
devices.app_clear("com.atnc.vfr")#清除数据
devices.app_start("com.atnc.vfr","com.uzmap.pkg.EntranceActivity")#启动app
import time
time.sleep(3)
#devices(description="6s | 跳转").click()
devices(resourceId="real_name").send_keys("24368")
devices(resourceId="IDCard").send_keys("123456")
devices(resourceId="login").click()