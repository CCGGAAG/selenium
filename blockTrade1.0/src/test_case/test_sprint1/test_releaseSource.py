'''
Created on 2017年5月2日

@author: test
'''
import unittest
from selenium import webdriver
import time

from pyframe import pyframe as dr
from pyframe  import log
from pyframe import open_excel

class releaseSource(unittest.TestCase):
    def setUp(self):
         #driver
        self.driver = dr.PyFrame()
        self.driver.open(open_excel.read_excel("../test_data/data.xlsx", "url", "testhomepage", "baseurl"))
        self.driver.wait(20)
        #logger
        self.logs =log.log.get_logger(self)
        self.driver.max_window()
        
    def test_postGoods(self):
        #commonPost
        self.driver.click("xpath", open_excel.read_excel("../test_data/data.xlsx", "releaseSource", "test_postGoods", "commonPost"), 5)
        #goodsType
        self.driver.click("xpath", open_excel.read_excel("../test_data/data.xlsx", "releaseSource", "test_postGoods", ""), 5)
        #boatName
        element = self.driver.get_element_by("id",open_excel.read_excel("../test_data/data.xlsx", "releaseSource", "test_postGoods", ""))
        element.clear()
        element.inputByEle(open_excel.read_excel("../test_data/data.xlsx", "releaseSource", "test_postGoods", ""))
        #goodsClass
        self.driver.click("xpath", open_excel.read_excel("../test_data/data.xlsx", "releaseSource", "test_postGoods", ""), 5)
        # indexType
        self.driver.click("xpath", open_excel.read_excel("../test_data/data.xlsx", "releaseSource", "test_postGoods", ""), 5)
        time.sleep(1)
        self.driver.click("xpath", open_excel.read_excel("../test_data/data.xlsx", "releaseSource", "test_postGoods", ""), 5)
        #indexQuality
        self.driver.input("xpath", "", "")
        self.driver.input("xpath", "", "")
        self.driver.input("xpath", "", "")
        self.driver.input("xpath", "", "")
        self.driver.input("xpath", "", "")
        self.driver.input("xpath", "", "")
        #originPlace
        self.driver.click("xpath", open_excel.read_excel("../test_data/data.xlsx", "releaseSource", "test_postGoods", ""), 5)
        time.sleep(1)
        self.driver.click("xpath", open_excel.read_excel("../test_data/data.xlsx", "releaseSource", "test_postGoods", ""), 5)
        #currency
        element = self.driver.get_element_by("id",open_excel.read_excel("../test_data/data.xlsx", "releaseSource", "test_postGoods", ""))
        element.clear()
        element.inputByEle(open_excel.read_excel("../test_data/data.xlsx", "releaseSource", "test_postGoods", ""))
        #goodsName
        element = self.driver.get_element_by("id",open_excel.read_excel("../test_data/data.xlsx", "releaseSource", "test_postGoods", ""))
        element.clear()
        element.inputByEle(open_excel.read_excel("../test_data/data.xlsx", "releaseSource", "test_postGoods", ""))
        #moreOrLess
        element = self.driver.get_element_by("id",open_excel.read_excel("../test_data/data.xlsx", "releaseSource", "test_postGoods", ""))
        element.clear()
        element.inputByEle(open_excel.read_excel("../test_data/data.xlsx", "releaseSource", "test_postGoods", ""))
        #endingTime
        self.driver.click("xpath", open_excel.read_excel("../test_data/data.xlsx", "releaseSource", "test_postGoods", ""), 5)
        time.sleep(1)
        self.driver.click("xpath", open_excel.read_excel("../test_data/data.xlsx", "releaseSource", "test_postGoods", ""), 5)
        #price
        #priceType
        #offerQuantity
        #MOQ
        #payType
        #payTime
        #partOrWarehourse
        #goodsImg
        #post
        
        
        
        
    def  tearDown(self):
        self.driver.quit()               
                  
            
if __name__ == "__main__":
    unittest.main()
