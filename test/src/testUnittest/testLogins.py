'''
Created on 2017年4月10日

@author: test
'''
import unittest
from selenium import webdriver
import time

class loginTest(unittest.TestCase):
    def setUp(self):
        profileDir = r"D:\software\firefox\profile"       #配置文件导入
        profile = webdriver.FirefoxProfile(profileDir)  
        self.driver = webdriver.Firefox(profile)
        self.driver.get("http://222.209.88.121:9999/zlgxwl/login/index.html")
        time.sleep(3)
    
    def test_Login(self):
        self.driver.find_element_by_xpath(".//*[@id='loginName']").clear()
        self.driver.find_element_by_xpath(".//*[@id='loginName']").send_keys("15737957635")
        #密码
        self.driver.find_element_by_xpath(".//*[@id='pwd']").clear()
        self.driver.find_element_by_xpath(".//*[@id='pwd']").send_keys("Yan123456")
        #验证码
        self.driver.close()
        oldUrl = ("http://222.209.88.121:9999/zlgxwl/login/index.html")
        newUrl = self.driver.current_url
        i=1
        while oldUrl==newUrl and i<4 :
            self.driver.find_element_by_xpath(".//*[@id='code']").clear()
            code = input("输入验证码：")
            self.driver.find_element_by_xpath(".//*[@id='code']").send_keys(code)
        #提交
            self.driver.find_element_by_xpath("html/body/div[2]/div/div[2]/div[4]/input").click()
            time.sleep(5)
            newUrl = self.driver.current_url
            print(self.driver.title)
            print(newUrl)
            i=i+1
#        self.assertEqual(self.driver.current_url, "http://222.209.88.121:9999/zlgxwl/index.html", msg="登录失败")
    def tearDown(self):
        print("123")
#        
if __name__ == "__main__":
    unittest.main()
# 构造测试集
suite = unittest.TestSuite()
suite.addTest(loginTest("test_Login"))
# 执行测试
runner = unittest.TextTestRunner()
runner.run(suite)