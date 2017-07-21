'''
Created on 2017年4月21日

@author: test
'''
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By   
import logging
import sys

class readTexts():
    
    def logger(self,logName):
        """ 获取logger"""
        self.logger = logging.getLogger()
        logger = self.logger
        
        if not logger.handlers:
            # 指定logger输出格式
            formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
            # 文件日志
            file_handler = logging.FileHandler("../test_report/test.log")
            file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式
            # 控制台日志
            console_handler = logging.StreamHandler(sys.stdout)
            console_handler.formatter = formatter  # 也可以直接给formatter赋值
            # 为logger添加的日志处理器
            logger.addHandler(file_handler)
            logger.addHandler(console_handler)
            # 指定日志的最低输出级别，默认为WARN级别
            logger.setLevel(logging.INFO)

        return logger


    def driver(self):
        """获得driver"""
        self.driver = webdriver.Chrome()
        return self.driver    
    
    def file(self,fileName):
        """获得文件"""
        self.f = open(fileName,"w")
        return self.f
    
    def count(self,b):
        b= b+1
        return b
    def setA(self,a):
        self.a = a
        return a
    def setB(self,b):
        self.b = b
        return b
    def setC(self,c):
        self.c = c
        return c
    def setD(self,d):
        self.d = d
        return d
#    def count(self,b):
#        count=self.a+str(b)+self.c
#        return count
    def doText(self,log,file,driver,baseUrl,locatePath,titlePath,textPath):
        logger = log
        driver = driver
        driver.implicitly_wait(20)
        f= file
        driver.get(baseUrl)
        #循环写入
        while self.b<self.d:
            try:
                self.b= self.b+1
                locateXpath =self.a+str(self.b)+self.c
                print(locateXpath)
               
                WebDriverWait(driver,3,0.5).until(EC.presence_of_element_located((By.XPATH,locatePath)))
                ele=driver.find_element_by_xpath(locateXpath)
                newUrl =ele.get_attribute("href")
                logger.info(newUrl )
                driver.get(newUrl )
                
                title = WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,titlePath)))
                text = WebDriverWait(driver,3,0.5).until(EC.presence_of_element_located((By.XPATH,textPath)))
                f.write(title.text)
                f.write("\n")
                f.write(text.text)
                f.write("\n")
                logger.info(title.text)
                logger.info(self.b)
                driver.back()
            except:
                logger.error(Exception )
                driver.get(baseUrl)
                self.b=self.b-1
            
        driver.close()   
        f.close()


