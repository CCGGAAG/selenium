#coding=utf-8
#
import unittest
import testLogins
from test.test_class import AllTests
import HTMLTestRunner
import time


#单元测试all_test
#suite = unittest.TestSuite()
#suite.addTest(testLogins.loginTest("test_Login"))
#if __name__ == '__main__':
## 执行测试
#    runner = unittest.TextTestRunner()
#    runner.run(suite)


#discover    
def creatsuite():
    testunit = unittest.TestSuite()
    test_dir = "D:\\eclipse\\workspace\\test\\src\\testUnittest"
    discover = unittest.defaultTestLoader.discover(test_dir,pattern = "test* .py" , top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
            
if __name__ == '__main__':
# 执行测试
#    now = time.strftime("%Y-%m-%M-%H_%M_%S",time.localtime(time.time())) 
#    fp=open("result"+now+".html",'wb')
#    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='测试结果',description='result:')
#    
#    runner.run(AllTests) 
#    fp.close()
        
    
    runner = unittest.TextTestRunner()
    runner.run(alltests)
    