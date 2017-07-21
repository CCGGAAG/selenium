'''
Created on 2017年4月10日

@author: test
'''
import unittest
from selenium import webdriver
import time

class loginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.get("http://222.209.88.121:9999/zlgxwl/login/index.html")
        
        
    def test_Login(self):
        """   登录模块"""
        self.driver.find_element_by_xpath(".//*[@id='loginName']").clear()
        self.driver.find_element_by_xpath(".//*[@id='loginName']").send_keys("15737957635")
        #密码
        self.driver.find_element_by_xpath(".//*[@id='pwd']").clear()
        self.driver.find_element_by_xpath(".//*[@id='pwd']").send_keys("Yan123456")
        #验证码
        oldUrl = ("http://222.209.88.121:9999/zlgxwl/login/index.html")
        newUrl = self.driver.current_url
        self.assertEqual(newUrl, oldUrl, msg="登录失败")
        
    def test_url(self):
        """首页"""
        self.driver.get("http://222.209.88.121:9999/zlgxwl/index.html")
        self.driver.find_element_by_xpath("html/body/div[3]/div/div[1]/a/img").click()
        self.driver.close()
        
    def tearDown(self):
        self.driver.quit()
   
        
if __name__ == "__main__":
    unittest.main()
