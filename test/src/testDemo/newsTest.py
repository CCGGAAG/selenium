'''
Created on 2017年4月6日

@author: test
'''
from   selenium     import webdriver
from goNews  import goNews
class newsTest():
    def testhead(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://222.209.88.121:9999/zlgxjy/infocenter/index.html")
        p = goNews()
        p.pPlayed(self.driver,".//*[@id='searchResult']/ul/li/div/div[1]/img")
        

test01=newsTest()
test01.testhead()
