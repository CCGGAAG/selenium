
'''
Created on 2017年4月7日
@author: test
'''

from selenium import webdriver
import user
import data
import admin
import time

def getUser():
    #获取login类，调用login类的方法
    users = user.login()
    return users

def getAdmin():
    #获取admin类，调用admin类的方法
    admins = admin.admin()
    return admins

def begin(url="http://222.209.88.121:9999/zlgxwl/login/index.html"):
     #获取driver驱动
        profileDir = r"D:\software\firefox\profile"       #配置文件导入
        profile = webdriver.FirefoxProfile(profileDir)  
        driver = webdriver.Firefox(profile)
        time.sleep(3)
        driver.get(url) 
        print(driver.current_url)
        return driver         


#托运方
#tyf = getUser()
#driverT = begin()
#driverT = tyf.logins(driverT, data.name1, data.pass1)
#deiverT = tyf.goCenter(driverT)
#driverT = tyf.postGoods(driverT)

#管理员
adm1 = getAdmin()
driverA = begin("http://222.209.88.121:9999/wlpt")
driverA = adm1.loginAdmin(driverA)
driverA = adm1.goHuoYuanGuanLi(driverA)
driverA = adm1.yGoodsPass(driverA)

#承运方
#cyf = getUser()
#driverC = begin()
#driverC = cyf.logins(driverC, data.name2, data.pass2)
#driverC = cyf.goHuoYuanXinXi(driverC)
#driverC = cyf.chooseYkj(driverC)

#托运方
#driverT = tyf.goListToPay(driverT)






