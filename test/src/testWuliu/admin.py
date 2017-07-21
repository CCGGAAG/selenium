#coding=utf-8
'''
Created on 2017年4月7日

@author: test
'''
#coding=utf-8
from selenium import webdriver
import time
import user
from selenium.webdriver.common.keys import Keys                                    #键盘操作
from selenium.webdriver.common.action_chains import ActionChains #鼠标操作
from selenium.webdriver.common.by import By                                        #by定位
from selenium.webdriver.support.ui import WebDriverWait              #显式等待
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
class admin():
    def  loginAdmin(self,driver):
           #用户名
            driver.find_element_by_xpath(".//*[@id='username']").clear()
            driver.find_element_by_xpath(".//*[@id='username']").send_keys("admin")
            #密码
            driver.find_element_by_xpath(".//*[@id='password']").clear()
            driver.find_element_by_xpath(".//*[@id='password']").send_keys("123456")
            #登录
            driver.find_element_by_xpath(".//*[@id='loginForm']/input[3]").click()
            time.sleep(2)
            print(driver.current_url)
            try:
                driver.find_element_by_xpath(".//*[@id='userInfo']/a")
                print("登录成功！！！")
            except:
                print("登录失败")
            return driver
        
    def goHuoYuanGuanLi(self,driver):
        driver.find_element_by_xpath(".//*[@id='menu']/li[3]/a").click()
        WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,".//*[@id='collapse-ea2fb0dde9c8456095a14d8e5007f190']/div/ul/li[1]/a")))
        print(driver.find_element_by_xpath(".//*[@id='menu']/li[3]/a").text)
#        driver.switch_to_window(driver.window_handles[0])
        return driver
    def  yGoodsPass(self,driver):
        driver.switch_to_frame("mainFrame")
        time.sleep(3)
        print("货源管理")
        time.sleep(2)
        pinming = driver.find_element_by_xpath(".//*[@id='contentTable']/tbody/tr[1]/td[4]")
        print(pinming.text)
        driver.quit()
        #状态：待审核
        driver.find_element_by_xpath(".//*[@id='s2id_sourceStatus']/a").click()
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='select2-drop']/div/input").send_keys("待审核")
        driver.find_element_by_xpath(".//*[@id='select2-drop']/div/input").send_keys(Keys.ENTER)    
           
        #查询
        driver.find_element_by_xpath(".//*[@id='btnSubmit']").click()
        time.sleep(1)
#        a1 = driver.find_element_by_xpath(".//*[@id='contentTable']/tbody/tr[1]/td[4]/text()").text()
#        print(a1)

        #第一行的审核按钮
        driver.find_element_by_xpath(".//*[@id='contentTable']/tbody/tr[1]/td[11]/a[1]").click()
        time.sleep(3)
        driver.find_element_by_xpath(".//*[@id='btnSubmit']").click()
        
        #弹窗
        time.sleep(2)
        driver.switch_to_default_content()
     
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='jbox-state-state0']/div[2]/button[1]").click()
#        driver.find_element_by_xpath(".//*[@id='jbox-state-state0']/div[2]/button[1]")
        
        
#        move_to_element_with_offset(to_element, xoffset, yoffset) 
        
#        a1 = driver.find_element_by_class_name("jbox-body")
#        print(a1)
#        aa = driver.switch_to_alert().accept
#        driver.find_element_by_xpath(".//*[@id='jbox-state-state0']/div[2]/button[1]").click()
#        aa.find_element_by_xpath(".//*[@id='jbox-state-state0']/div[2]/button[1]").click()
#        above = driver.find_element_by_xpath(".//*[@id='jbox-state-state0']/div[2]/button[1]")
##        ActionChains(driver).move_to_element_with_offset( 800, 200)
#        ActionChains(driver).move_by_offset(200, 50)
#        ActionChains(driver).click()
#        driver.find_element_by_link_text("确定").click()
#        
        
        
#        
        
        