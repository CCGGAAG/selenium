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
        base_url="https://www.baidu.com/"        
        self.driver.open(base_url)
        self.driver.wait(20)
        #logger
        self.logs =log.log.get_logger(self)
        self.driver.max_window()
        
     def __init__(self,a):
         self.a = 1   
     def test_Phone(self):
         """测试手机号码输入"""
         a = open_excel.read_excel("../test_data/data.xlsx", "demo", "testdemo", "输入框")
         self.driver.input("xpath", a,"1234")
         self.driver.set_screenshot()
         log.log.get_logger(self).info("输入成功")
         
     def test_imgIsTrue(self):
        """ 图片"""
        a = open_excel.read_excel("../test_data/data.xlsx", "demo", "testdemo", "图片")
        src = self.driver.get_attribute("xpath", a, "src")
        self.driver.open(src)
        self.driver.set_screenshot()
        
     def tearDown(self):
            self.driver.quit()
            
            self.driver.back()
            
        
if __name__ == "__main__":
    unittest.main()
