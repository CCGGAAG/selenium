import unittest
from selenium import webdriver
import time

from pyframe import pyframe as dr
from pyframe  import log
from pyframe import open_excel

class qualification(unittest.TestCase):
    def setUp(self):
         #driver
        self.driver = dr.PyFrame()
        self.driver.open(open_excel.read_excel("../test_data/data.xlsx", "url", "testqualification", "baseurl"))
        self.driver.wait(20)
        #logger
        self.logs =log.log.get_logger(self)
        self.driver.max_window()
    
    def test_qualiification3in1(self):
        '''资质认证流程'''
        #companyNameCN公司中文名
        element = self.driver.get_element_by("id",open_excel.read_excel("../test_data/data.xlsx", "qualification", "test_qualiification3in1", "companyNameCN"))
        element.clear()
        element.inputByEle(open_excel.read_excel("../test_data/data.xlsx", "qualification", "test_qualiification3in1", "companyNameCNValue"))
        #comepanyNameEN 公司英文名
        element = self.driver.get_element_by("id",open_excel.read_excel("../test_data/data.xlsx", "qualification", "test_qualiification3in1", "comepanyNameEN"))
        element.clear()
        element.inputByEle(open_excel.read_excel("../test_data/data.xlsx", "qualification", "test_qualiification3in1", "companyNameENValue"))
        #foreignTrade 外贸资质
        self.driver.click("xpath",open_excel.read_excel("../test_data/data.xlsx", "qualification", "test_qualiification3in1", "foreignTrade"), 5)
        #localArea 所在地区
        self.driver.click("xpath",open_excel.read_excel("../test_data/data.xlsx", "qualification", "test_qualiification3in1", "province"), 5)
        time.sleep(1)
        self.driver.click("xpath",open_excel.read_excel("../test_data/data.xlsx", "qualification", "test_qualiification3in1", "provinceValue"), 5)
        self.driver.click("xpath",open_excel.read_excel("../test_data/data.xlsx", "qualification", "test_qualiification3in1", "city"), 5)
        time.sleep(1)
        self.driver.click("xpath",open_excel.read_excel("../test_data/data.xlsx", "qualification", "test_qualiification3in1", "cityValue"), 5)
        self.driver.click("xpath",open_excel.read_excel("../test_data/data.xlsx", "qualification", "test_qualiification3in1", "area"), 5)
        time.sleep(1)
        self.driver.click("xpath",open_excel.read_excel("../test_data/data.xlsx", "qualification", "test_qualiification3in1", "areaValue"), 5)
        #detailAdress 详细地址
        element = self.driver.get_element_by("id",open_excel.read_excel("../test_data/data.xlsx", "qualification", "test_qualiification3in1", "detailAdress"))
        element.clear()
        element.inputByEle(open_excel.read_excel("../test_data/data.xlsx", "qualification", "test_qualiification3in1", "detailAdressValue"))
        #contact 联系人
        element = self.driver.get_element_by("id",open_excel.read_excel("../test_data/data.xlsx", "qualification", "test_qualiification3in1", "contact"))
        element.clear()
        element.inputByEle(open_excel.read_excel("../test_data/data.xlsx", "qualification", "test_qualiification3in1", "contactValue"))
        #phoneNumber 手机号码
        element = self.driver.get_element_by("id",open_excel.read_excel("../test_data/data.xlsx", "qualification", "test_qualiification3in1", "phoneNumber"))
        element.clear()
        element.inputByEle(open_excel.read_excel("../test_data/data.xlsx", "qualification", "test_qualiification3in1", "phoneNumberValue"))
        #enterpriseNature 企业性质
        self.driver.click("xpath",open_excel.read_excel("../test_data/data.xlsx", "qualification", "test_qualiification3in1", "enterpriseNature"), 5)
        time.sleep(2)
        self.driver.click("xpath",open_excel.read_excel("../test_data/data.xlsx", "qualification", "test_qualiification3in1", "enterpriseNatureValue"), 5)
        #mainBusiness 企业主营服务
        element = self.driver.get_element_by("id",open_excel.read_excel("../test_data/data.xlsx", "qualification", "test_qualiification3in1", "mainBusiness"))
        element.clear()
        element.inputByEle(open_excel.read_excel("../test_data/data.xlsx", "qualification", "test_qualiification3in1", "mainBusinessValue"))
        #nextPage 下一步
        self.driver.click("xpath",open_excel.read_excel("../test_data/data.xlsx", "qualification", "test_qualiification3in1", ""), 5)
        
        #creditCardNumber 社会信用代码
        element = self.driver.get_element_by("id",open_excel.read_excel("../test_data/data.xlsx", "qualification", "test_qualiification3in1", "creditCardNumber"))
        element.clear()
        element.inputByEle(open_excel.read_excel("../test_data/data.xlsx", "qualification", "test_qualiification3in1", "creditCardNumberValue"))
        #businessLicenseImg营业执照图片
        self.driver.input("xpath", open_excel.read_excel("../test_data/data.xlsx", "qualification", "test_qualiification3in1", "businessLicenseImg"),
                          open_excel.read_excel("../test_data/data.xlsx", "qualification", "test_qualiification3in1", "businessLicenseImgValue"))
        #openingPermitNumber开户许可证号
        element = self.driver.get_element_by("id",open_excel.read_excel("../test_data/data.xlsx", "qualification", "test_qualiification3in1", "openingPermitNumber"))
        element.clear()
        element.inputByEle(open_excel.read_excel("../test_data/data.xlsx", "qualification", "test_qualiification3in1", "openingPermitNumberValue"))
        #openingPermitImg开户许可证图片
        self.driver.input("xpath", open_excel.read_excel("../test_data/data.xlsx", "qualification", "test_qualiification3in1", "openingPermitImg"),
                          open_excel.read_excel("../test_data/data.xlsx", "qualification", "test_qualiification3in1", "openingPermitImgValue"))
        #importlicensingNumber 进出口企业代码号
        element = self.driver.get_element_by("id",open_excel.read_excel("../test_data/data.xlsx", "qualification", "test_qualiification3in1", "importlicensingNumber"))
        element.clear()
        element.inputByEle(open_excel.read_excel("../test_data/data.xlsx", "qualification", "test_qualiification3in1", "importlicensingNumberValue"))
        #foreignTradeImg外贸资质图片
        self.driver.input("xpath", open_excel.read_excel("../test_data/data.xlsx", "qualification", "test_qualiification3in1", "foreignTradeImg"),
                          open_excel.read_excel("../test_data/data.xlsx", "qualification", "test_qualiification3in1", "foreignTradeImgValue"))
        #adminEmpowerImg办理人授权图片
        self.driver.input("xpath",open_excel.read_excel("../test_data/data.xlsx", "qualification", "test_qualiification3in1", "adminEmpowerImg"),
                          open_excel.read_excel("../test_data/data.xlsx", "qualification", "test_qualiification3in1", "adminEmpowerImgImg"))
        #legalPersonIDCardImg 法人身份证图片
        self.driver.input("xpath", open_excel.read_excel("../test_data/data.xlsx", "qualification", "test_qualiification3in1", "legalPersonIDCardImg"),
                          open_excel.read_excel("../test_data/data.xlsx", "qualification", "test_qualiification3in1", "legalPersonIDCardImgImg"))
        #提交
        self.driver.click("xpath",open_excel.read_excel("../test_data/data.xlsx", "qualification", "test_qualiification3in1", "post"), 2)
        
                
    def  tearDown(self):
        self.driver.quit()               
                  
            
if __name__ == "__main__":
    unittest.main()
