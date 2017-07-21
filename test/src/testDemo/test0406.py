'''
Created on 2017年4月6日
@author: test
'''
from selenium import webdriver

class test():
    #查看图片是否存在
    def isDisplayP(self,driver,ele1):
        p1 = driver.find_element_by_xpath(ele1)
        assert p1.is_displayed()
        print(" 图片展示  Verified OK")
    #新建driver
    def begin(self,url="http://222.209.88.121:9999/zlgxjy/infocenter/index.html"):
            #  url="http://222.209.88.121:9999/zlgxjy/infocenter/index.html"   #默认的url
        driver = webdriver.Chrome()
        driver.get(url) 
        print(driver.current_url)
        return driver
      
    #页面是否正常显示，正常显示false，异常为：true
    def is404Found(self,driver ):
        flags=False
        try:
            driver.find_element_by_xpath("html/body/div")
            print("0")
            return flags
            return "123"
        except Exception:
            flags=True
            print(Exception)
            print("1")
            return flags
            
        
    #页面元素是否存在
    def isElementExist(self,olddriver,element):
        flag=True
        try:
            olddriver.find_element_by_xpath(element)
            return flag
        except:
            flag=False
            return flag
        
    #图片是否能打开
    def isOpenPic(self,driver):
            r1 = t1.isElementExist(driver,"html/body/div[1]/h1")
            #不存在即为正确读取图片
            if r1 ==False:
                print("图片正确打开   Verified OK")
            else:
                print("服务器404或者图片未找到")
#执行测试方法:
t1=test()
driver =t1.begin()
   
#t1.isDisplayP(driver,ele1=".//*[@id='searchResult']/ul/li/div/div[1]/img")    #调用图片是否存在方法
text = t1.is404Found(driver)   #调用页面是否是404方法×
print(text)
#t1.isOpenPic(driver)                #调用图片是否显示的方法
#t1.isElementExist(driver, "")   #调用页面元素是否存在的方法×
driver.quit()






