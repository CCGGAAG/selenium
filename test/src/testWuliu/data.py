#coding=utf-8
'''
Created on 2017年4月6日

@author: test
'''
from selenium import webdriver
class data():
    def dataName(self):
#读取txt文件
        user_file = open('namePass.txt','r')
        values = user_file.readlines()
        user_file.close()
#创建列表
        nameList= []
       
#循环输入列表
        for serch in values:
            username = serch.split(',')[0]
            nameList.append(username)
#    print(username) 
           
            
#    print(password)
#验证列表的正确性
        print("----------------------------")
        print(nameList)
       
        return  nameList

    def dataPass(self):
#读取txt文件
        user_file = open('namePass.txt','r')
        values = user_file.readlines()
        user_file.close()
#创建列表
        
        passList = []
#循环输入列表
        for serch in values:
            
#    print(username) 
            password = serch.split(',')[1]
            passList.append(password)
#    print(password)
#验证列表的正确性
        print("----------------------------")
        
        print(passList)
        return passList


name1= data().dataName()[0]
name2= data().dataName()[1]
pass1= data().dataPass()[0]
pass2= data().dataPass()[1]

pinming = "test01"
miaoshu = "this is a test Goods"
huowuliang = "10"
zuixiaoc = "2"
zuixiaos = "3"
shixiao = "24"
yunfei = "10"
payPass1="Ls1234"
payPass2="Ls1234"   
    