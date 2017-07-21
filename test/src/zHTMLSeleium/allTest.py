#coding=utf-8      #防止中文乱码
from selenium import webdriver
#加载unittest模块
import unittest 
import time

#加载HTMLTestRunner，用于生成HTMLreuslt
import HTMLTestRunner
#加载test类
import testLogins
import testLinks



#单元测试all_test
#suite = unittest.TestSuite()
#suite.addTest(unittest.makeSuite(testLogins.loginTest))
#suite.addTest(unittest.makeSuite(testLinks.linkTest))



#discover    
def creatsuite():
    testunit = unittest.TestSuite()
    test_dir = "D:\\eclipse\\workspace\\test\\src\\zHTMLSeleium"
    discover = unittest.defaultTestLoader.discover(test_dir,pattern = "test* .py" , top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit

                
if __name__ == '__main__':
# 执行测试
    nows = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time())) 
    #打开一个文件，将result写入此file中
    fp=open("result"+nows+".html",'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='testHtml',description='result:')
    runner.run(creatsuite())
    fp.close()
    