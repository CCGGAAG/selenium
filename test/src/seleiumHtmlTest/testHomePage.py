import unittest
from selenium import webdriver
import time
import base_tools

class homePage(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url="http://222.209.88.121:9999/zlgxwl/index.html"           #首页
        self.driver.implicitly_wait(20)
        self.driver.get(self.base_url)
        
    def test_logoImgDisplay(self):
        """logo图片是否预留位置"""
        driver =self.driver
        t1 = driver.find_element_by_xpath("html/body/div[3]/div/div[1]/a/img")
        assert t1.is_displayed()
               
    def test_LogoImgTrue(self):
        """ logo图片是否存在"""
        base_tools.toolsBase.imgIs404(self,self.driver,"html/body/div[3]/div/div[1]/a/img")

    def test_LogoImgUrl(self):
        """点击图片的跳转页面"""
        driver =self.driver
        driver.find_element_by_xpath("html/body/div[3]/div/div[1]/a/img").click()
        newUrl =driver.current_url
        assert newUrl=="http://222.209.88.121:9999/zlgxwl/"
        
    def test_wellComeText(self):
        """ 欢迎访问中联钢信！交易时间：**:**-**:**"""
        base_tools.toolsBase.textIsNotNull(self,self.driver, "html/body/div[1]/div/p")
        
    def tearDown(self):
        self.driver.quit()  
        
if __name__ == "__main__":
    unittest.main()
