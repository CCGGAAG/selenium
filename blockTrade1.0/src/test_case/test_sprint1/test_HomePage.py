'''
Created on 2017年4月26日

@author: test
'''
import unittest
from selenium import webdriver
import time

from pyframe import pyframe as dr
from pyframe  import log
from pyframe import open_excel

class homePage(unittest.TestCase):
    def setUp(self):
         #driver
        self.driver = dr.PyFrame()
        self.driver.open(open_excel.read_excel("../test_data/data.xlsx", "url", "testhomepage", "baseurl"))
        self.driver.wait(20)
        #logger
        self.logs =log.log.get_logger(self)
        self.driver.max_window()
        
    def test_head_welcome(self):
        """页眉欢迎语"""
        text = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_head_welcome", "welcome") , "text")
        self.driver.set_screenshot()     
        self.logs.info("页眉欢迎语:"+text)
        assert text != ""
       
    def test_head_login(self):
        '''页眉登录字段'''
        text= self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_head_login", "login") , "text")
        self.driver.set_screenshot()     
        self.logs.info("页眉登录字段:"+text)
        assert text != ""
    
    def test_head_loginUrl(self):
        '''页眉登录链接'''
        url = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_head_login", "login") , "href")
        self.driver.open(url)
        self.driver.set_screenshot()     
        self.logs.info("页眉登录链接:"+url)
        assert self.driver.get_title() != "404页面"
        
    def test_head_register(self):
        '''页眉注册字段'''
        text= self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_head_register", "register") , "text")
        self.driver.set_screenshot()     
        self.logs.info("页眉注册字段:"+text)
        assert text != ""
        
    def test_head_registerUrl(self):
        '''页眉注册链接'''
        url = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_head_register", "register") , "href")
        self.driver.open(url)
        self.driver.set_screenshot()     
        self.logs.info("页眉注册链接:"+url)
        assert self.driver.get_title() != "404页面"
    
    def test_head_message(self):
        '''页眉消息字段'''
        text= self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_head_message", "message") , "text")
        self.driver.set_screenshot()     
        self.logs.info("页眉消息字段:"+text)
        assert text != ""
        
    def test_head_messageUrl(self):
        '''页眉消息链接'''
        url = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_head_message", "message") , "href")
        self.driver.open(url)
        self.driver.set_screenshot()     
        self.logs.info("页眉消息链接:"+url)
        assert self.driver.get_title() != "404页面"
   
    def test_head_memberCenter(self):
        '''页眉会员中心字段'''
        text= self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_head_memberCenter", "memberCenter") , "text")
        self.driver.set_screenshot()     
        self.logs.info("页眉会员中心字段:"+text)
        assert text != ""
        
    def test_head_memberCenterUrl(self):
        '''页眉会员中心链接'''
        url = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_head_memberCenter", "memberCenter") , "href")
        self.driver.open(url)
        self.driver.set_screenshot()
        self.logs.info("页眉会员中心链接:"+url)
        assert self.driver.get_title()   != "404页面"
   
    def test_head_helpCenter(self):
        '''页眉帮助中心字段'''
        text= self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_head_helpCenter", "helpCenter") , "text")
        self.driver.set_screenshot()     
        self.logs.info("页眉帮助中心字段:"+text)
        assert text != ""
        
    def test_head_helpCenterUrl(self):
        '''页眉帮助中心链接'''
        url = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_head_helpCenter", "helpCenter") , "href")
        self.driver.open(url)
        self.driver.set_screenshot()     
        self.logs.info("页眉帮助中心链接:"+url)
        assert self.driver.get_title() != "404页面"
   
    def test_head_APP(self):
        '''页眉APP字段'''
        text= self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_head_APP", "APP") , "text")
        self.driver.set_screenshot()     
        self.logs.info("页眉APP字段:"+text)
        assert text != ""
   
    def test_head_APPImg(self):
        '''页眉app图片显示'''
        self.driver.move_to_element("xpath", open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_head_APP", "APP"))
        url = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_head_APPImg", "APPImg") , "src")
        self.driver.open(url)
        self.driver.set_screenshot()     
        self.logs.info("页眉app图片链接:"+url)
        assert self.driver.get_title() != "404页面"
      
    def test_head_tradeTime(self):
        '''页眉交易时间字段'''
        text= self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_head_tradeTime", "tradeTime") , "text")
        self.driver.set_screenshot()     
        self.logs.info("交易时间字段:"+text)
        assert text != ""
    
    def test_head_logo(self):
        '''logo显示'''
        result = self.driver.get_element_displayed("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_head_logo", "logo"))
        self.driver.set_screenshot()     
        self.logs.info("logo显示:"+str(result))
        assert result  
        
    def test_head_logoUrl(self):
        '''logo链接'''
        src = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_head_logo", "logo") , "src")
        self.driver.open(src)
        self.driver.set_screenshot()     
        self.logs.info("logo链接:"+src)
        assert self.driver.get_title() != "404页面"
        
    def test_head_searchBox(self):
        '''搜索框显示'''
        result = self.driver.get_element_displayed("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_head_searchBox", "searchBox"))
        self.driver.set_screenshot()     
        self.logs.info("搜索框显示:"+str(result))
        assert result 
        
    def test_head_searchButton(self):
        '''搜索按钮显示'''
        result = self.driver.get_element_displayed("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_head_searchButton", "searchButton"))
        self.driver.set_screenshot()     
        self.logs.info("搜索按钮显示:"+str(result))
        assert result 
        
    def test_head_searchTxt(self):
        '''热门搜索显示'''
        result = self.driver.get_element_displayed("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_head_searchTxt", "searchTxt"))
        self.driver.set_screenshot()     
        self.logs.info("热门搜索显示:"+str(result))
        assert result 
    
    def test_head_shoppingCart(self):
        '''购物车显示'''
        result = self.driver.get_element_displayed("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_head_shoppingCart", "shoppingCart"))
        self.driver.set_screenshot()     
        self.logs.info("logo显示:"+str(result))
        assert result 
        
    def test_head_shoppingCartUrl(self):
        '''购物车链接'''
        url = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_head_shoppingCart", "shoppingCart") , "href")
        self.driver.open(url)
        self.driver.set_screenshot()     
        self.logs.info("购物车链接:"+url)
        assert self.driver.get_title() != "404页面"
        
    def  test_navigation_shouYe(self):
        '''导航栏首页字段'''
        text= self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_navigation_shouYe", "shouYe") , "text")
        self.driver.set_screenshot()     
        self.logs.info("导航栏首页字段:"+text)
        assert text != ""
    
    def test_navigation_shouYeUrl(self):
        '''导航栏首页链接'''
        url = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_navigation_shouYe", "shouYe") , "href")
        self.driver.open(url)
        self.driver.set_screenshot()     
        self.logs.info("导航栏首页链接:"+url)
        assert self.driver.get_title() != "404页面"
    
    def  test_navigation_daZongJiaoYi(self):
        '''导航栏大宗交易字段'''
        text= self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_navigation_daZongJiaoYi", "daZongJiaoYi") , "text")
        self.driver.set_screenshot()     
        self.logs.info("导航栏大宗交易字段:"+text)
        assert text != ""
    
    def test_navigation_daZongJiaoYiUrl(self):
        '''导航栏大宗交易链接'''
        url = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_navigation_daZongJiaoYi", "daZongJiaoYi") , "href")
        self.driver.open(url)
        self.driver.set_screenshot()     
        self.logs.info("导航栏大宗交易链接:"+url)
        assert self.driver.get_title() != "404页面"
        
    def  test_navigation_ziYuanDan(self):
        '''导航栏资源单字段'''
        text= self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_navigation_ziYuanDan", "ziYuanDan") , "text")
        self.driver.set_screenshot()     
        self.logs.info("导航栏资源单字段:"+text)
        assert text != ""
    
    def test_navigation_ziYuanDanUrl(self):
        '''导航栏资源单链接'''
        url = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_navigation_ziYuanDan", "ziYuanDan") , "href")
        self.driver.open(url)
        self.driver.set_screenshot()     
        self.logs.info("导航栏资源单链接:"+url)
        assert self.driver.get_title() != "404页面"
            
    def  test_navigation_jingJia(self):
        '''导航栏竞价字段'''
        text= self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_navigation_jingJia", "jingJia") , "text")
        self.driver.set_screenshot()     
        self.logs.info("导航栏竞价字段:"+text)
        assert text != ""
    
    def test_navigation_jingJiaUrl(self):
        '''导航栏竞价链接'''
        url = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_navigation_jingJia", "jingJia") , "href")
        self.driver.open(url)
        self.driver.set_screenshot()     
        self.logs.info("导航栏竞价链接:"+url)
        assert self.driver.get_title() != "404页面"
        
    def  test_navigation_ziXun(self):
        '''导航栏资讯字段'''
        text= self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_navigation_ziXun", "ziXun") , "text")
        self.driver.set_screenshot()     
        self.logs.info("导航栏资讯字段:"+text)
        assert text != ""
    
    def test_navigation_ziXunUrl(self):
        '''导航栏资讯链接'''
        url = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_navigation_ziXun", "ziXun") , "href")
        self.driver.open(url)
        self.driver.set_screenshot()     
        self.logs.info("导航栏资讯链接:"+url)
        assert self.driver.get_title() != "404页面"
    
    def  test_navigation_otherPlatform(self):
        '''导航栏其他平台字段'''
        text= self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_navigation_otherPlatform", "otherPlatform") , "text")
        self.driver.set_screenshot()     
        self.logs.info("导航栏其他平台字段:"+text)
        assert text != ""
    
#    def test_goodsClassify_iron(self):
#        '''商品分类-铁矿-二级分类显示'''
#        self.driver.move_to_element("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_goodsClassify_iron", "iron"))
#        self.driver.set_screenshot() 
#    　pinMing = self.driver.get_element_displayed("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_goodsClassify_ironPinMing", "ironPinMing"))
#        gangKou = self.driver.get_element_displayed("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_goodsClassify_ironPinMing", "ironPinMing"))
#        guoJia = self.driver.get_element_displayed("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_goodsClassify_ironPinMing", "ironPinMing"))
##        if self.driver.get_element_by() :
##        elif  self.driver.get_element_by("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_goodsClassify_ironPinMing", "ironPinMing")) ：
##        elif  self.driver.get_element_by("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_goodsClassify_ironPinMing", "ironPinMing")) :
##        else:
#        self.logs.info(ele)
#        assert ele
#        
#    def test_goodsClassify_ironUrl(self):
#        '''商品分类-铁矿-品名链接'''
#        self.driver.move_to_element("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_goodsClassify_iron", "iron"))
#        self.driver.click_text_link("pb粉")
#        self.driver.set_screenshot() 
#        self.logs.info(self.driver.get_title())
#        assert self.driver.get_title() != "404页面"
#    
#    
    def test_banner_img(self):
        '''banner显示'''
        src = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_banner_img", "img") , "src")
        self.driver.open(src)
        self.driver.set_screenshot()
        self.logs.info("banner链接:"+src)
        assert self.driver.get_title() != "404页面"
        
    def test_banner_imgUrl(self):
        '''banner链接'''
        href = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_banner_img", "img") , "href")
        self.driver.open(href)
        self.driver.set_screenshot()
        self.logs.info("banner链接:"+href)
        assert self.driver.get_title() != "404页面"
        
    def test_banner_imgClickRight(self):
        '''banner右点击效果'''
        src1 = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_banner_img", "img") , "src")
        self.driver.click("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_banner_imgClickRight", "imgClickRight"), 5)
        src2 = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_banner_img", "img") , "src")
        self.driver.set_screenshot()
        self.logs.info("banner点击R1:"+src1)
        self.logs.info("banner点击R1:"+src2)
        assert src1!=src2
        
    def test_banner_imgClickLeft(self):
        '''banner左点击效果'''
        src1 = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_banner_img", "img") , "src")
        self.driver.click("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_banner_imgClickLeft", "imgClickLeft"), 5)
        src2 = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_banner_img", "img") , "src")
        self.driver.set_screenshot()
        self.logs.info("banner点击L1:"+src1)
        self.logs.info("banner点击L1:"+src2)
        assert src1!=src2
    
    def test_banner_imgClickCir(self):
        '''banner圆圈快速点击效果'''
        src1 = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_banner_img", "img") , "src")
        self.driver.click("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_banner_imgClickCir", "imgClickCir"), 5)
        src2 = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_banner_img", "img") , "src")
        self.driver.set_screenshot()
        self.logs.info("banner点击L1:"+src1)
        self.logs.info("banner点击L1:"+src2)
        assert src1!=src2
        
    def test_information_headImg(self):
        '''信息-头像显示'''
        result =self.driver.get_element_displayed("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_information_headImg", "headImg"))
        self.driver.set_screenshot()
        self.logs.info("banner点击L1:"+str(result))
        assert result
        
    def  test_information_welcome(self):
        '''信息-欢迎语'''
        text= self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_information_welcome", "welcome") , "text")
        self.driver.set_screenshot()     
        self.logs.info("信息-欢迎语:"+text)
        assert text != ""
    
    def  test_information_login(self):
        '''信息-登录字段'''
        text= self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_information_login", "login") , "text")
        self.driver.set_screenshot()     
        self.logs.info("信息-登录字段:"+text)
        assert text != ""

    def test_information_loginUrl(self):
        '''信息-登录链接'''
        url = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_information_login", "login") , "href")
        self.driver.open(url)
        self.driver.set_screenshot()     
        self.logs.info("信息-登录链接:"+url)
        assert self.driver.get_title() != "404页面"
    
    def  test_information_register(self):
        '''信息-注册字段'''
        text= self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_information_register", "register") , "text")
        self.driver.set_screenshot()     
        self.logs.info("信息-注册字段:"+text)
        assert text != ""

    def test_information_registerUrl(self):
        '''信息-注册链接'''
        url = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_information_register", "register") , "href")
        self.driver.open(url)
        self.driver.set_screenshot()     
        self.logs.info("信息-注册链接:"+url)
        assert self.driver.get_title() != "404页面"
    
    def  test_information_notice(self):
        '''信息-公告字段'''
        text= self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_information_notice", "notice") , "text")
        self.driver.set_screenshot()     
        self.logs.info("信息-公告字段:"+text)
        assert text != ""
    
    def  test_information_more(self):
        '''信息-更多字段'''
        text= self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_information_more", "more") , "text")
        self.driver.set_screenshot()     
        self.logs.info("信息-更多字段:"+text)
        assert text != ""

    def test_information_moreUrl(self):
        '''信息-更多链接'''
        url = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_information_more", "more") , "href")
        self.driver.open(url)
        self.driver.set_screenshot()     
        self.logs.info("信息-更多链接:"+url)
        assert self.driver.get_title() != "404页面"
    
    def  test_information_notice1(self):
        '''信息-第一条公告字段'''
        text= self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_information_notice1", "notice1") , "text")
        self.driver.set_screenshot()
        self.logs.info("信息-第一条公告字段:"+text)
        assert text != ""

    def test_information_notice1Url(self):
        '''信息-第一条公告链接'''
        url = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_information_notice1", "notice1") , "href")
        self.driver.open(url)
        self.driver.set_screenshot()     
        self.logs.info("信息-第一条公告链接:"+url)
        assert self.driver.get_title() != "404页面"
    
    def  test_information_notice2(self):
        '''信息-第二条公告字段'''
        text= self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_information_notice2", "notice2") , "text")
        self.driver.set_screenshot()
        self.logs.info("信息-第二条公告字段:"+text)
        assert text != ""

    def test_information_notice2Url(self):
        '''信息-第二条公告链接'''
        url = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_information_notice2", "notice2") , "href")
        self.driver.open(url)
        self.driver.set_screenshot()     
        self.logs.info("信息-第二条公告链接:"+url)
        assert self.driver.get_title() != "404页面"
    
    def  test_information_notice3(self):
        '''信息-第三条公告字段'''
        text= self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_information_notice3", "notice3") , "text")
        self.driver.set_screenshot()
        self.logs.info("信息-第三条公告字段:"+text)
        assert text != ""

    def test_information_notice3Url(self):
        '''信息-第三条公告链接'''
        url = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_information_notice3", "notice3") , "href")
        self.driver.open(url)
        self.driver.set_screenshot()     
        self.logs.info("信息-第三条公告链接:"+url)
        assert self.driver.get_title() != "404页面"
    
    def  test_information_notice4(self):
        '''信息-第四条公告字段'''
        text= self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_information_notice4", "notice4") , "text")
        self.driver.set_screenshot()
        self.logs.info("信息-第四条公告字段:"+text)
        assert text != ""

    def test_information_notice4Url(self):
        '''信息-第四条公告链接'''
        url = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_information_notice4", "notice4") , "href")
        self.driver.open(url)
        self.driver.set_screenshot()     
        self.logs.info("信息-第四条公告链接:"+url)
        assert self.driver.get_title() != "404页面"
    
    
    def test_iron_leftImg(self):
        '''铁矿左侧图显示'''
        src = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_iron_leftImg", "leftImg") , "src")
        self.driver.open(src)
        self.driver.set_screenshot()
        self.logs.info("铁矿左侧图:"+src)
        assert self.driver.get_title() != "404页面"
        
    def test_iron_tablePinMing(self):
        '''列表-品名字段'''
        text = self.driver.get_text("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_iron_tablePinMing", "tablePinMing"))
        self.driver.set_screenshot()
        self.logs.info("列表-品名字段:"+text)
        assert text=="品名"
        
    def test_iron_tableKuCun(self):
        '''列表-库存字段'''
        text = self.driver.get_text("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_iron_tableKuCun", "tableKuCun"))
        self.driver.set_screenshot()
        self.logs.info("列表-库存字段:"+text)
        assert text=="库存"
    
    def test_iron_tableCangKuMaTou(self):
        '''列表-仓库/码头字段'''
        text = self.driver.get_text("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_iron_tableCangKuMaTou", "tableCangKuMaTou"))
        self.driver.set_screenshot()
        self.logs.info("列表-仓库/码头字段:"+text)
        assert text=="仓库/码头"
      
    def test_iron_tableMaiFang(self):
        '''列表-卖方字段'''
        text = self.driver.get_text("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_iron_tableMaiFang", "tableMaiFang"))
        self.driver.set_screenshot()
        self.logs.info("列表-卖方字段:"+text)
        assert text=="卖方"
    
    def test_iron_tableJiaGe(self):
        '''列表-价格字段'''
        text = self.driver.get_text("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_iron_tableJiaGe", "tableJiaGe"))
        self.driver.set_screenshot()
        self.logs.info("列表-价格字段:"+text)
        assert text=="价格"
    
    def test_iron_priceTrendTitle(self):
        '''价格走势图title'''
        text = self.driver.get_text("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_iron_priceTrendTitle", "priceTrendTitle"))
        self.driver.set_screenshot()
        self.logs.info("价格走势图title:"+text)
        assert text=="铁矿价格走势"
    
    def test_iron_priceTrendTime(self):
        '''价格走势图time'''
        text = self.driver.get_text("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_iron_priceTrendTime", "priceTrendTime"))
        self.driver.set_screenshot()
        self.logs.info("价格走势图time:"+text)
        assert text !=""
    
    def test_iron_priceTrendChart(self):
        result =self.driver.get_element_displayed("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_iron_priceTrendChart", "priceTrendChart"))
        self.driver.set_screenshot()
        self.logs.info("价格走势图展示:"+str(result))
        assert result

    
    
    def test_coal_leftImg(self):
        '''煤炭左侧图显示'''
        src = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_coal_leftImg", "leftImg") , "src")
        self.driver.open(src)
        self.driver.set_screenshot()
        self.logs.info("煤炭左侧图:"+src)
        assert self.driver.get_title() != "404页面"
        
    def test_coal_tablePinMing(self):
        '''列表-品名字段'''
        text = self.driver.get_text("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_coal_tablePinMing", "tablePinMing"))
        self.driver.set_screenshot()
        self.logs.info("列表-品名字段:"+text)
        assert text=="品名"
        
    def test_coal_tableKuCun(self):
        '''列表-库存字段'''
        text = self.driver.get_text("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_coal_tableKuCun", "tableKuCun"))
        self.driver.set_screenshot()
        self.logs.info("列表-库存字段:"+text)
        assert text=="库存"
    
    def test_coal_tableCangKuMaTou(self):
        '''列表-仓库/码头字段'''
        text = self.driver.get_text("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_coal_tableCangKuMaTou", "tableCangKuMaTou"))
        self.driver.set_screenshot()
        self.logs.info("列表-仓库/码头字段:"+text)
        assert text=="仓库/码头"
      
    def test_coal_tableMaiFang(self):
        '''列表-卖方字段'''
        text = self.driver.get_text("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_coal_tableMaiFang", "tableMaiFang"))
        self.driver.set_screenshot()
        self.logs.info("列表-卖方字段:"+text)
        assert text=="卖方"
    
    def test_coal_tableJiaGe(self):
        '''列表-价格字段'''
        text = self.driver.get_text("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_coal_tableJiaGe", "tableJiaGe"))
        self.driver.set_screenshot()
        self.logs.info("列表-价格字段:"+text)
        assert text=="价格"
    
    def test_coal_priceTrendTitle(self):
        '''价格走势图title'''
        text = self.driver.get_text("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_coal_priceTrendTitle", "priceTrendTitle"))
        self.driver.set_screenshot()
        self.logs.info("价格走势图title:"+text)
        assert text=="煤炭价格走势"
    
    def test_coal_priceTrendTime(self):
        '''价格走势图time'''
        text = self.driver.get_text("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_coal_priceTrendTime", "priceTrendTime"))
        self.driver.set_screenshot()
        self.logs.info("价格走势图time:"+text)
        assert text !=""
    
    def test_coal_priceTrendChart(self):
        result =self.driver.get_element_displayed("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_coal_priceTrendChart", "priceTrendChart"))
        self.driver.set_screenshot()
        self.logs.info("价格走势图展示:"+str(result))
        assert result
    
    
    
    def test_coke_leftImg(self):
        '''焦炭左侧图显示'''
        src = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_coke_leftImg", "leftImg") , "src")
        self.driver.open(src)
        self.driver.set_screenshot()
        self.logs.info("焦炭左侧图:"+src)
        assert self.driver.get_title() != "404页面"
        
    def test_coke_tablePinMing(self):
        '''列表-品名字段'''
        text = self.driver.get_text("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_coke_tablePinMing", "tablePinMing"))
        self.driver.set_screenshot()
        self.logs.info("列表-品名字段:"+text)
        assert text=="品名"
        
    def test_coke_tableKuCun(self):
        '''列表-库存字段'''
        text = self.driver.get_text("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_coke_tableKuCun", "tableKuCun"))
        self.driver.set_screenshot()
        self.logs.info("列表-库存字段:"+text)
        assert text=="库存"
    
    def test_coke_tableCangKuMaTou(self):
        '''列表-仓库/码头字段'''
        text = self.driver.get_text("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_coke_tableCangKuMaTou", "tableCangKuMaTou"))
        self.driver.set_screenshot()
        self.logs.info("列表-仓库/码头字段:"+text)
        assert text=="仓库/码头"
      
    def test_coke_tableMaiFang(self):
        '''列表-卖方字段'''
        text = self.driver.get_text("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_coke_tableMaiFang", "tableMaiFang"))
        self.driver.set_screenshot()
        self.logs.info("列表-卖方字段:"+text)
        assert text=="卖方"
    
    def test_coke_tableJiaGe(self):
        '''列表-价格字段'''
        text = self.driver.get_text("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_coke_tableJiaGe", "tableJiaGe"))
        self.driver.set_screenshot()
        self.logs.info("列表-价格字段:"+text)
        assert text=="价格"
    
    def test_coke_priceTrendTitle(self):
        '''价格走势图title'''
        text = self.driver.get_text("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_coke_priceTrendTitle", "priceTrendTitle"))
        self.driver.set_screenshot()
        self.logs.info("价格走势图title:"+text)
        assert text=="焦炭价格走势"
    
    def test_coke_priceTrendTime(self):
        '''价格走势图time'''
        text = self.driver.get_text("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_coke_priceTrendTime", "priceTrendTime"))
        self.driver.set_screenshot()
        self.logs.info("价格走势图time:"+text)
        assert text !=""
    
    def test_coke_priceTrendChart(self):
        result =self.driver.get_element_displayed("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_coke_priceTrendChart", "priceTrendChart"))
        self.driver.set_screenshot()
        self.logs.info("价格走势图展示:"+str(result))
        assert result

    
    
    def test_pigIron_leftImg(self):
        '''生铁左侧图显示'''
        src = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_pigIron_leftImg", "leftImg") , "src")
        self.driver.open(src)
        self.driver.set_screenshot()
        self.logs.info("生铁左侧图:"+src)
        assert self.driver.get_title() != "404页面"
        
    def test_pigIron_tablePinMing(self):
        '''列表-品名字段'''
        text = self.driver.get_text("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_pigIron_tablePinMing", "tablePinMing"))
        self.driver.set_screenshot()
        self.logs.info("列表-品名字段:"+text)
        assert text=="品名"
        
    def test_pigIron_tableKuCun(self):
        '''列表-库存字段'''
        text = self.driver.get_text("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_pigIron_tableKuCun", "tableKuCun"))
        self.driver.set_screenshot()
        self.logs.info("列表-库存字段:"+text)
        assert text=="库存"
    
    def test_pigIron_tableCangKuMaTou(self):
        '''列表-仓库/码头字段'''
        text = self.driver.get_text("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_pigIron_tableCangKuMaTou", "tableCangKuMaTou"))
        self.driver.set_screenshot()
        self.logs.info("列表-仓库/码头字段:"+text)
        assert text=="仓库/码头"
      
    def test_pigIron_tableMaiFang(self):
        '''列表-卖方字段'''
        text = self.driver.get_text("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_pigIron_tableMaiFang", "tableMaiFang"))
        self.driver.set_screenshot()
        self.logs.info("列表-卖方字段:"+text)
        assert text=="卖方"
    
    def test_pigIron_tableJiaGe(self):
        '''列表-价格字段'''
        text = self.driver.get_text("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_pigIron_tableJiaGe", "tableJiaGe"))
        self.driver.set_screenshot()
        self.logs.info("列表-价格字段:"+text)
        assert text=="价格"
    
    def test_pigIron_priceTrendTitle(self):
        '''价格走势图title'''
        text = self.driver.get_text("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_pigIron_priceTrendTitle", "priceTrendTitle"))
        self.driver.set_screenshot()
        self.logs.info("价格走势图title:"+text)
        assert text=="生铁价格走势"
    
    def test_pigIron_priceTrendTime(self):
        '''价格走势图time'''
        text = self.driver.get_text("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_pigIron_priceTrendTime", "priceTrendTime"))
        self.driver.set_screenshot()
        self.logs.info("价格走势图time:"+text)
        assert text !=""
    
    def test_pigIron_priceTrendChart(self):
        result =self.driver.get_element_displayed("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_pigIron_priceTrendChart", "priceTrendChart"))
        self.driver.set_screenshot()
        self.logs.info("价格走势图展示:"+str(result))
        assert result
    

    
    def test_billet_leftImg(self):
        '''钢坯左侧图显示'''
        src = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_billet_leftImg", "leftImg") , "src")
        self.driver.open(src)
        self.driver.set_screenshot()
        self.logs.info("钢坯左侧图:"+src)
        assert self.driver.get_title() != "404页面"
        
    def test_billet_tablePinMing(self):
        '''列表-品名字段'''
        text = self.driver.get_text("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_billet_tablePinMing", "tablePinMing"))
        self.driver.set_screenshot()
        self.logs.info("列表-品名字段:"+text)
        assert text=="品名"
        
    def test_billet_tableKuCun(self):
        '''列表-库存字段'''
        text = self.driver.get_text("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_billet_tableKuCun", "tableKuCun"))
        self.driver.set_screenshot()
        self.logs.info("列表-库存字段:"+text)
        assert text=="库存"
    
    def test_billet_tableCangKuMaTou(self):
        '''列表-仓库/码头字段'''
        text = self.driver.get_text("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_billet_tableCangKuMaTou", "tableCangKuMaTou"))
        self.driver.set_screenshot()
        self.logs.info("列表-仓库/码头字段:"+text)
        assert text=="仓库/码头"
      
    def test_billet_tableMaiFang(self):
        '''列表-卖方字段'''
        text = self.driver.get_text("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_billet_tableMaiFang", "tableMaiFang"))
        self.driver.set_screenshot()
        self.logs.info("列表-卖方字段:"+text)
        assert text=="卖方"
    
    def test_billet_tableJiaGe(self):
        '''列表-价格字段'''
        text = self.driver.get_text("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_billet_tableJiaGe", "tableJiaGe"))
        self.driver.set_screenshot()
        self.logs.info("列表-价格字段:"+text)
        assert text=="价格"
    
    def test_billet_priceTrendTitle(self):
        '''价格走势图title'''
        text = self.driver.get_text("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_billet_priceTrendTitle", "priceTrendTitle"))
        self.driver.set_screenshot()
        self.logs.info("价格走势图title:"+text)
        assert text=="钢坯价格走势"
    
    def test_billet_priceTrendTime(self):
        '''价格走势图time'''
        text = self.driver.get_text("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_billet_priceTrendTime", "priceTrendTime"))
        self.driver.set_screenshot()
        self.logs.info("价格走势图time:"+text)
        assert text !=""
    
    def test_billet_priceTrendChart(self):
        result =self.driver.get_element_displayed("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_billet_priceTrendChart", "priceTrendChart"))
        self.driver.set_screenshot()
        self.logs.info("价格走势图展示:"+str(result))
        assert result
    
    
    def  test_hangYeZiXun_title(self):
        '''行业资讯-title字段'''
        text= self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_hangYeZiXun_title", "title") , "text")
        self.driver.set_screenshot()     
        self.logs.info("行业资讯-title字段:"+text)
        assert text =="行业资讯"
    
    def  test_hangYeZiXun_notice1(self):
        '''行业资讯-第一条资讯字段'''
        text= self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_hangYeZiXun_notice1", "notice1") , "text")
        self.driver.set_screenshot()
        self.logs.info("行业资讯-第一条资讯字段:"+text)
        assert text != ""

    def test_hangYeZiXun_notice1Url(self):
        '''行业资讯-第一条资讯链接'''
        url = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_hangYeZiXun_notice1", "notice1") , "href")
        self.driver.open(url)
        self.driver.set_screenshot()     
        self.logs.info("行业资讯-第一条资讯链接:"+url)
        assert self.driver.get_title() != "404页面"
    
    def  test_hangYeZiXun_notice2(self):
        '''行业资讯-第二条资讯字段'''
        text= self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_hangYeZiXun_notice2", "notice2") , "text")
        self.driver.set_screenshot()
        self.logs.info("行业资讯-第二条资讯字段:"+text)
        assert text != ""

    def test_hangYeZiXun_notice2Url(self):
        '''行业资讯-第二条资讯链接'''
        url = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_hangYeZiXun_notice2", "notice2") , "href")
        self.driver.open(url)
        self.driver.set_screenshot()     
        self.logs.info("行业资讯-第二条资讯链接:"+url)
        assert self.driver.get_title() != "404页面"
    
    def  test_hangYeZiXun_notice3(self):
        '''行业资讯-第三条资讯字段'''
        text= self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_hangYeZiXun_notice3", "notice3") , "text")
        self.driver.set_screenshot()
        self.logs.info("行业资讯-第三条资讯字段:"+text)
        assert text != ""

    def test_hangYeZiXun_notice3Url(self):
        '''行业资讯-第三条资讯链接'''
        url = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_hangYeZiXun_notice3", "notice3") , "href")
        self.driver.open(url)
        self.driver.set_screenshot()     
        self.logs.info("行业资讯-第三条资讯链接:"+url)
        assert self.driver.get_title() != "404页面"
    
    def  test_hangYeZiXun_notice4(self):
        '''行业资讯-第四条资讯字段'''
        text= self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_hangYeZiXun_notice4", "notice4") , "text")
        self.driver.set_screenshot()
        self.logs.info("行业资讯-第四条资讯字段:"+text)
        assert text != ""

    def test_hangYeZiXun_notice4Url(self):
        '''行业资讯-第四条资讯链接'''
        url = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_hangYeZiXun_notice4", "notice4") , "href")
        self.driver.open(url)
        self.driver.set_screenshot()     
        self.logs.info("行业资讯-第四条资讯链接:"+url)
        assert self.driver.get_title() != "404页面"
    
    def  test_hangYeZiXun_notice5(self):
        '''行业资讯-第五条资讯字段'''
        text= self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_hangYeZiXun_notice5", "notice5") , "text")
        self.driver.set_screenshot()
        self.logs.info("行业资讯-第五条资讯字段:"+text)
        assert text != ""

    def test_hangYeZiXun_notice5Url(self):
        '''行业资讯-第五条资讯链接'''
        url = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_hangYeZiXun_notice5", "notice5") , "href")
        self.driver.open(url)
        self.driver.set_screenshot()     
        self.logs.info("行业资讯-第五条资讯链接:"+url)
        assert self.driver.get_title() != "404页面"
    
    
    
    def  test_chengJiaoDongTai_title(self):
        '''成交动态-title字段'''
        text= self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_chengJiaoDongTai_title", "title") , "text")
        self.driver.set_screenshot()     
        self.logs.info("成交动态-title字段:"+text)
        assert text =="成交动态"
    
    def  test_chengJiaoDongTai_notice1(self):
        '''成交动态-第一条资讯字段'''
        text= self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_chengJiaoDongTai_notice1", "notice1") , "text")
        self.driver.set_screenshot()
        self.logs.info("成交动态-第一条资讯字段:"+text)
        assert text != ""

    def test_chengJiaoDongTai_notice1Url(self):
        '''成交动态-第一条资讯链接'''
        url = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_chengJiaoDongTai_notice1", "notice1") , "href")
        self.driver.open(url)
        self.driver.set_screenshot()     
        self.logs.info("成交动态-第一条资讯链接:"+url)
        assert self.driver.get_title() != "404页面"
    
    def  test_chengJiaoDongTai_notice2(self):
        '''成交动态-第二条资讯字段'''
        text= self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_chengJiaoDongTai_notice2", "notice2") , "text")
        self.driver.set_screenshot()
        self.logs.info("成交动态-第二条资讯字段:"+text)
        assert text != ""

    def test_chengJiaoDongTai_notice2Url(self):
        '''成交动态-第二条资讯链接'''
        url = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_chengJiaoDongTai_notice2", "notice2") , "href")
        self.driver.open(url)
        self.driver.set_screenshot()     
        self.logs.info("成交动态-第二条资讯链接:"+url)
        assert self.driver.get_title() != "404页面"
    
    def  test_chengJiaoDongTai_notice3(self):
        '''成交动态-第三条资讯字段'''
        text= self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_chengJiaoDongTai_notice3", "notice3") , "text")
        self.driver.set_screenshot()
        self.logs.info("成交动态-第三条资讯字段:"+text)
        assert text != ""

    def test_chengJiaoDongTai_notice3Url(self):
        '''成交动态-第三条资讯链接'''
        url = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_chengJiaoDongTai_notice3", "notice3") , "href")
        self.driver.open(url)
        self.driver.set_screenshot()     
        self.logs.info("成交动态-第三条资讯链接:"+url)
        assert self.driver.get_title() != "404页面"
    
    def  test_chengJiaoDongTai_notice4(self):
        '''成交动态-第四条资讯字段'''
        text= self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_chengJiaoDongTai_notice4", "notice4") , "text")
        self.driver.set_screenshot()
        self.logs.info("成交动态-第四条资讯字段:"+text)
        assert text != ""

    def test_chengJiaoDongTai_notice4Url(self):
        '''成交动态-第四条资讯链接'''
        url = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_chengJiaoDongTai_notice4", "notice4") , "href")
        self.driver.open(url)
        self.driver.set_screenshot()     
        self.logs.info("成交动态-第四条资讯链接:"+url)
        assert self.driver.get_title() != "404页面"
    
    def  test_chengJiaoDongTai_notice5(self):
        '''成交动态-第五条资讯字段'''
        text= self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_chengJiaoDongTai_notice5", "notice5") , "text")
        self.driver.set_screenshot()
        self.logs.info("成交动态-第五条资讯字段:"+text)
        assert text != ""

    def test_chengJiaoDongTai_notice5Url(self):
        '''成交动态-第五条资讯链接'''
        url = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_chengJiaoDongTai_notice5", "notice5") , "href")
        self.driver.open(url)
        self.driver.set_screenshot()     
        self.logs.info("成交动态-第五条资讯链接:"+url)
        assert self.driver.get_title() != "404页面"
    
    
    def  test_gangXinYaoWen_title(self):
        '''钢信要闻-title字段'''
        text= self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_gangXinYaoWen_title", "title") , "text")
        self.driver.set_screenshot()     
        self.logs.info("钢信要闻-title字段:"+text)
        assert text =="钢信要闻"
    
    def  test_gangXinYaoWen_notice1(self):
        '''钢信要闻-第一条资讯字段'''
        text= self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_gangXinYaoWen_notice1", "notice1") , "text")
        self.driver.set_screenshot()
        self.logs.info("钢信要闻-第一条资讯字段:"+text)
        assert text != ""

    def test_gangXinYaoWen_notice1Url(self):
        '''钢信要闻-第一条资讯链接'''
        url = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_gangXinYaoWen_notice1", "notice1") , "href")
        self.driver.open(url)
        self.driver.set_screenshot()     
        self.logs.info("钢信要闻-第一条资讯链接:"+url)
        assert self.driver.get_title() != "404页面"
    
    def  test_gangXinYaoWen_notice2(self):
        '''钢信要闻-第二条资讯字段'''
        text= self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_gangXinYaoWen_notice2", "notice2") , "text")
        self.driver.set_screenshot()
        self.logs.info("钢信要闻-第二条资讯字段:"+text)
        assert text != ""

    def test_gangXinYaoWen_notice2Url(self):
        '''钢信要闻-第二条资讯链接'''
        url = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_gangXinYaoWen_notice2", "notice2") , "href")
        self.driver.open(url)
        self.driver.set_screenshot()     
        self.logs.info("钢信要闻-第二条资讯链接:"+url)
        assert self.driver.get_title() != "404页面"
    
    def  test_gangXinYaoWen_notice3(self):
        '''钢信要闻-第三条资讯字段'''
        text= self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_gangXinYaoWen_notice3", "notice3") , "text")
        self.driver.set_screenshot()
        self.logs.info("钢信要闻-第三条资讯字段:"+text)
        assert text != ""

    def test_gangXinYaoWen_notice3Url(self):
        '''钢信要闻-第三条资讯链接'''
        url = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_gangXinYaoWen_notice3", "notice3") , "href")
        self.driver.open(url)
        self.driver.set_screenshot()     
        self.logs.info("钢信要闻-第三条资讯链接:"+url)
        assert self.driver.get_title() != "404页面"
    
    def  test_gangXinYaoWen_notice4(self):
        '''钢信要闻-第四条资讯字段'''
        text= self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_gangXinYaoWen_notice4", "notice4") , "text")
        self.driver.set_screenshot()
        self.logs.info("钢信要闻-第四条资讯字段:"+text)
        assert text != ""

    def test_gangXinYaoWen_notice4Url(self):
        '''钢信要闻-第四条资讯链接'''
        url = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_gangXinYaoWen_notice4", "notice4") , "href")
        self.driver.open(url)
        self.driver.set_screenshot()     
        self.logs.info("钢信要闻-第四条资讯链接:"+url)
        assert self.driver.get_title() != "404页面"
    
    def  test_gangXinYaoWen_notice5(self):
        '''钢信要闻-第五条资讯字段'''
        text= self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_gangXinYaoWen_notice5", "notice5") , "text")
        self.driver.set_screenshot()
        self.logs.info("钢信要闻-第五条资讯字段:"+text)
        assert text != ""

    def test_gangXinYaoWen_notice5Url(self):
        '''钢信要闻-第五条资讯链接'''
        url = self.driver.get_attribute("xpath",open_excel.read_excel("../test_data/data.xlsx", "homepage", "test_gangXinYaoWen_notice5", "notice5") , "href")
        self.driver.open(url)
        self.driver.set_screenshot()     
        self.logs.info("钢信要闻-第五条资讯链接:"+url)
        assert self.driver.get_title() != "404页面"
    
    def  tearDown(self):
        self.driver.quit()               
                  
            
if __name__ == "__main__":
    unittest.main()
