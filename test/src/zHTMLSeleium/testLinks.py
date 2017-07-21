'''
Created on 2017年4月13日

@author: test
'''
import unittest
from selenium import webdriver
import time

class linkTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url="http://222.209.88.121:9999/zlgxwl/login/index.html"
        self.driver.implicitly_wait(20)
        self.driver.get(self.base_url)
        
    
    def test_now(self):
        """当前页面url"""
        driver = self.driver
        nowurl = driver.current_url
        assert nowurl == self.base_url
        
    def test_Title(self):
        """当前页面title"""
        driver = self.driver
        assert driver.title == "登录"
        
    def Yes(self):
        """不是test开头的方法"""
        driver = self.driver
        driver.get("http://www.baidu.com")
        
    def tearDown(self):
        self.driver.quit()
     
        
if __name__ == "__main__":
    unittest.main()
    
