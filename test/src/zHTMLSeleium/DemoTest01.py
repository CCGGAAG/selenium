'''
Created on 2017年4月12日

@author: test
'''
#coding=utf-8      #防止中文乱码
from selenium import webdriver
import HTMLTestRunner
import unittest
import time

class  demo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        base_url = "http://www.baidu.com"
        self.driver.get(base_url)
        self.driver.implicitly_wait(20)
        self.verficationErrors=[]
        self.accept_next_alert=True
        
    def test_PicIsLocate(self):
        """图片存在"""
        driver = self.driver
        driver.current_url
        driver.find_element_by_xpath(".//*[@id='lg']/img")
        
    def test_SecIsLocate(self):
        """ 输入框存在"""
        driver = self.driver
        driver.find_element_by_xpath(".//*[@id='form']/span[1]")
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verficationErrors) 
        
if __name__ == '__main__':
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(demo("test_PicIsLocate"))
    suite.addTest(demo("test_SecIsLocate"))
    
    # 执行测试
#    runner = unittest.TextTestRunner()
#    runner.run(suite)
    
    #获取当前时间，这样便于下面的使用。
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time())) 
    #打开一个文件，将result写入此file中
    fp=open("result"+now+".html",'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='测试结果',description='result:')
    
    runner.run(suite) 
    fp.close()
        