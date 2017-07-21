'''
Created on 2017年4月6日

@author: test
'''
class goNews():
#验证图片是否显示，输入XPath，输出结果
    def pPlayed(self,driver1,inputXpath):
        driver = driver1
        inputXpath1=inputXpath
        p1 =driver.find_element_by_xpath(inputXpath1)
        assert p1.is_displayed()
        return (" 图片展示  Verified OK")
    
    def quitPage(self):
        driver = self.driver
        driver.quit()
        driver.quitPage()