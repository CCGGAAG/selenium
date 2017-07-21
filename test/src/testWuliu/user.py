#coding=utf-8
'''
Created on 2017年4月6日

@author: test
'''
#导入：webdriver、key键盘事件、by定位、显式等待、time时间、data自定义的数据类
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By   
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import data

class login():
    
    def logins(self,driver,aa,bb):
        print(aa)
        print(bb)
        #用户名
        driver.find_element_by_xpath(".//*[@id='loginName']").clear()
        driver.find_element_by_xpath(".//*[@id='loginName']").send_keys(aa)
        #密码
        driver.find_element_by_xpath(".//*[@id='pwd']").clear()
        driver.find_element_by_xpath(".//*[@id='pwd']").send_keys(bb)
        #验证码
        print(driver.current_url)
        oldUrl = ("http://222.209.88.121:9999/zlgxwl/login/index.html")
        newUrl = driver.current_url
        
        while oldUrl==newUrl :
            driver.find_element_by_xpath(".//*[@id='code']").clear()
            code = input("输入验证码：")
            driver.find_element_by_xpath(".//*[@id='code']").send_keys(code)
        #提交
            driver.find_element_by_xpath("html/body/div[2]/div/div[2]/div[4]/input").click()
            time.sleep(5)
            newUrl = driver.current_url
            print(driver.title)
            print(newUrl)
        return driver
    
    def goCenter(self,driver):
        
        driver.find_element_by_link_text("会员中心").click()
        ele = WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.LINK_TEXT,"修改基本资料")))
        print("会员中心")
        return driver    
   
    def postGoods(self,driver):
        #10秒内，每0.5秒验证一次，如果元素存在，则继续执行
        ele = WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,"html/body/div[5]/div[1]/dl[1]/dd/ul/li[1]/a")))
        ele.click()
        time.sleep(3)
        print("点击我的货源")
        
        ele1 = WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.XPATH,".//*[@id='serchForm']/div/div[1]/a")))
        ele1.click()
        print("点击发布货源")
        
        WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,".//*[@id='bidMethod']/a[2]")))
      
        
        #发盘方式
        print(driver.find_element_by_xpath(".//*[@id='publishgoodssource']/div/div/div[2]/dl/dt").text)
        print(driver.find_element_by_xpath(".//*[@id='bidMethod']/a[2]").text)
        driver.find_element_by_xpath(".//*[@id='bidMethod']/a[2]").click()
        
        #品种
        print(driver.find_element_by_xpath(".//*[@id='publishgoodssource']/div/div/div[4]/dl[1]/dt").text)
        print(driver.find_element_by_xpath(".//*[@id='sourcekinds']/button").text)
        driver.find_element_by_xpath(".//*[@id='sourcekinds']/button").click()
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='sks']/li/a").click()
        print(driver.find_element_by_xpath(".//*[@id='sks']/li/a").text)
#        print(driver.find_element_by_xpath(".//*[@id='publishgoodssource']/div/div/div[4]/dl[1]/dt").text)
#        print(driver.find_element_by_xpath(".//*[@id='sourcekinds']/button").text)
#        driver.find_element_by_xpath(".//*[@id='sourcekinds']/button").click()
#        ele2 = WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,".//*[@id='sks']/li/a")))
#        ele2.click()
#        print(ele2.text)
        #品名
        print(driver.find_element_by_xpath(".//*[@id='publishgoodssource']/div/div/div[4]/dl[2]/dt").text)
        driver.find_element_by_xpath(".//*[@id='sourcebrand']").send_keys(data.pinming)
        #描述
        print(driver.find_element_by_xpath(".//*[@id='publishgoodssource']/div/div/div[4]/dl[3]/dt").text)
        driver.find_element_by_xpath(".//*[@id='publishgoodssource']/div/div/div[4]/dl[3]/dd/input").send_keys(data.miaoshu)
        #货物量
        print(driver.find_element_by_xpath(".//*[@id='publishgoodssource']/div/div/div[4]/dl[4]/dt").text)
        driver.find_element_by_xpath(".//*[@id='amount']").send_keys(data.huowuliang)
        #运输要求
        print(driver.find_element_by_xpath(".//*[@id='publishgoodssource']/div/div/div[4]/dl[5]/dt").text)
        driver.find_element_by_xpath(".//*[@id='transportrequire']/button").click()
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='treq']/li[3]/a").click()
        
#        print(driver.find_element_by_xpath(".//*[@id='publishgoodssource']/div/div/div[4]/dl[5]/dt").text)
#        driver.find_element_by_xpath(".//*[@id='transportrequire']/button").click()
#        ele3 = WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,".//*[@id='treq']/li[1]/a")))
#        ele3.click()
        # 最小承运量
        print(driver.find_element_by_xpath(".//*[@id='minCapa']/dt").text)
        driver.find_element_by_xpath(".//*[@id='minCapacity']").send_keys(data.zuixiaoc)
        # 最小剩余量
        print(driver.find_element_by_xpath(".//*[@id='leftCapa']/dt").text)
        driver.find_element_by_xpath(".//*[@id='leftCapacity']").send_keys(data.zuixiaos)
        #发货收货地址
        print(driver.find_element_by_xpath(".//*[@id='publishgoodssource']/div/div/div[4]/dl[8]/dt").text)
        print(driver.find_element_by_xpath(".//*[@id='publishgoodssource']/div/div/div[4]/dl[11]/dt").text)
       
       #有效期
        print(driver.find_element_by_xpath(".//*[@id='yxq']/dt").text)
        driver.find_element_by_xpath(".//*[@id='due']").click()
        time.sleep(0.5)
        driver.find_element_by_xpath(".//*[@id='due']").send_keys(Keys.ENTER)
       
        
        #付款方式
       # print(driver.find_element_by_xpath(".//*[@id='publishgoodssource']/div/div/div[6]/dl[1]/dt").text)
        print(driver.find_element_by_xpath(".//*[@id='publishgoodssource']/div/div/div[5]/dl[1]/dt").text)

        
         #发票类型
       # print(driver.find_element_by_xpath(".//*[@id='publishgoodssource']/div/div/div[6]/dl[2]/dt").text)
        print(driver.find_element_by_xpath(".//*[@id='publishgoodssource']/div/div/div[5]/dl[2]/dt").text)
        driver.find_element_by_xpath(".//*[@id='invoicetype']/button").click()
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='iny']/li[2]/a").click()
        
         #运输时效
        #print(driver.find_element_by_xpath(".//*[@id='publishgoodssource']/div/div/div[6]/dl[3]/dt").text)
         #driver.find_element_by_xpath(".//*[@id='publishgoodssource']/div/div/div[6]/dl[3]/dd/input").send_keys(data.shixiao)
        print(driver.find_element_by_xpath(".//*[@id='publishgoodssource']/div/div/div[5]/dl[3]/dt").text)
        driver.find_element_by_xpath(".//*[@id='publishgoodssource']/div/div/div[5]/dl[3]/dd/input").send_keys(data.shixiao)
        
         #运费
        #print(driver.find_element_by_xpath(".//*[@id='publishgoodssource']/div/div/div[6]/dl[4]/dt").text)
        print(driver.find_element_by_xpath(".//*[@id='publishgoodssource']/div/div/div[5]/dl[4]/dt").text)
        driver.find_element_by_xpath(".//*[@id='freight']").send_keys(data.yunfei)
        
         #托运保证金
        #print(driver.find_element_by_xpath(".//*[@id='publishgoodssource']/div/div/div[6]/dl[6]/dt").text)
        print(driver.find_element_by_xpath(".//*[@id='publishgoodssource']/div/div/div[5]/dl[6]/dt").text)
        print(driver.find_element_by_xpath(".//*[@id='consign']").text)
#        print(driver.find_element_by_xpath(".//*[@id='publishgoodssource']/div/div/div[6]/dl[6]/dd/div").text)
        
        #承运保证金
        print(driver.find_element_by_xpath(".//*[@id='publishgoodssource']/div/div/div[5]/dl[7]/dt").text)
       # print(driver.find_element_by_xpath(".//*[@id='publishgoodssource']/div/div/div[6]/dl[7]/dt").text)
        print(driver.find_element_by_xpath(".//*[@id='accept']").text)
#        print(driver.find_element_by_xpath(".//*[@id='publishgoodssource']/div/div/div[6]/dl[7]/dd/div").text)
        
        #损耗约定
        #print(driver.find_element_by_xpath(".//*[@id='publishgoodssource']/div/div/div[6]/dl[8]/dt").text)
        print(driver.find_element_by_xpath(".//*[@id='publishgoodssource']/div/div/div[5]/dl[8]/dt").text)
        print(driver.find_element_by_xpath(".//*[@id='la']").text)
        
        #l理赔约定
       # print(driver.find_element_by_xpath(".//*[@id='publishgoodssource']/div/div/div[6]/dl[9]/dt").text)
        print(driver.find_element_by_xpath(".//*[@id='publishgoodssource']/div/div/div[5]/dl[9]/dt").text)
        print(driver.find_element_by_xpath(".//*[@id='ca']").text)
        
       #运输约定
        #print(driver.find_element_by_xpath(".//*[@id='publishgoodssource']/div/div/div[6]/dl[10]/dt").text)
        print(driver.find_element_by_xpath(".//*[@id='publishgoodssource']/div/div/div[5]/dl[10]/dt").text)
        print(driver.find_element_by_xpath(".//*[@id='ta']").text)
        
         #其他约定
        #print(driver.find_element_by_xpath(".//*[@id='publishgoodssource']/div/div/div[6]/dl[11]/dt").text)
        print(driver.find_element_by_xpath(".//*[@id='publishgoodssource']/div/div/div[5]/dl[11]/dt").text)
        print(driver.find_element_by_xpath(".//*[@id='oa']").text)
        
         #提交-保存-显示
        print(driver.find_element_by_xpath(".//*[@id='tijiao']").text)
        print(driver.find_element_by_xpath(".//*[@id='bachunchaogao']").text)
        
         #提交货源
        driver.find_element_by_xpath(".//*[@id='tijiao']").click()
        time.sleep(4)
        print(driver.current_url)
          #验证货源
        if  (driver.current_url)=="http://222.209.88.121:9999/zlgxwl/m/sourcelist.html":
            print("发布成功！！！")
        else :
            print("发布失败")
        return driver
    
    def goHuoYuanXinXi(self,driver): 
        driver.find_element_by_xpath("html/body/div[3]/div/div[2]/ul/li[2]/a").click()
        ele = WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.XPATH," .//*[@id='sourceForm']/div[1]/a[2]")))
        print(driver.title)
        return driver
    
    def chooseYkj(self,driver):    
        #选择一口价搜索
        driver.find_element_by_xpath(".//*[@id='faPan']/b[2]").click()
        driver.find_element_by_xpath(".//*[@id='searchSource']").click()
        time.sleep(1)
        
        #点击第一个一口价货源
        #driver.find_element_by_xpath(".//*[@id='searchResult']/div[1]/div[2]/div/b").click()
         #点击第二个一口价货源
        driver.find_element_by_xpath(".//*[@id='searchResult']/div[1]/div[3]/div/b").click()
         #点击第三个一口价货源
       # driver.find_element_by_xpath(".//*[@id='searchResult']/div[1]/div[4]/div/b").click()
        
        #进入货源详情
        WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,"html/body/div[5]/a[3]")))
        print(driver.find_element_by_xpath("html/body/div[5]/a[3]").text)
        driver.find_element_by_xpath(".//*[@id='toAccept']").click()
        #捕捉弹框信息
#        ale = driver.switch_to_alert()
#        time.sleep(5)
#        print(ale)
#        ale.accept
#        time.sleep(3)
        #提交订单
        WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,"html/body/div[8]/input")))
        print(driver.title)
        driver.find_element_by_xpath("html/body/div[8]/input").click()
       #支付保证金
        WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.XPATH," .//*[@id='lookOrder']")))
        print(driver.title)
            #支付信息
        print(driver.find_element_by_xpath(".//*[@id='countDown']").text)
        print("应付：%r"%driver.find_element_by_xpath(".//*[@id='money']").text)
        print("账户余额：%r"%driver.find_element_by_xpath(".//*[@id='yue']").text)
        print("还需充值：%r"%driver.find_element_by_xpath(".//*[@id='recharge']").text)
        driver.find_element_by_xpath(".//*[@id='password']").clear()
        driver.find_element_by_xpath(".//*[@id='password']").send_keys(data.payPass2)
        driver.find_element_by_xpath(".//*[@id='payBnt']").click()
        #支付成功
        WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.LINK_TEXT,"查看订单")))
        print("支付成功")
        return driver
    
    def  goListToPay(self,driver):
        #进入我的订单
        WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,"html/body/div[5]/div[1]/dl[1]/dd/ul/li[3]/a")))
        driver.find_element_by_xpath("html/body/div[5]/div[1]/dl[1]/dd/ul/li[3]/a").click()
        WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.XPATH," .//*[@id='btnSearch']")))
        print(driver.title)
        #选择待支付标签
        driver.find_element_by_xpath(".//*[@id='payMarginCount']").click()
        time.sleep(2)
        print(driver.title)
        return driver
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
         
       
        
        
    