# coding=utf-8
'''
Created on 2017年4月13日

@author: test
'''
import unittest
from selenium import webdriver
import time

from pyframe import pyframe as dr
from pyframe  import log
from pyframe import open_excel

class login(unittest.TestCase):
     def setUp(self):
         #driver
        self.driver = dr.PyFrame()
        base_url="https://www.zsteel.cc/zlgxwl/reg/index.html"        
        self.driver.open(base_url)
        self.driver.wait(20)
        #logger
        self.logs =log.log.get_logger(self)
        self.driver.max_window()
        
     def test_Phone(self):
         """测试手机号码输入"""
         self.driver.click("xpath", ".//*[@id='cerCheck']/li[1]")
         self.driver.input("xpath", ".//*[@id='image1']","C:\Users\test\Pictures\123.jpg")
#         a = open_excel.read_excel("../test_data/data.xlsx", "demo", "testdemo", "输入框")
#         self.driver.set_screenshot()
#         self.driver.input("xpath", a,"123")
#         self.driver.set_screenshot()
#         self.logs.info("输入成功")
        
     def tearDown(self):
            self.driver.quit()
            
        
if __name__ == "__main__":
    unittest.main()
