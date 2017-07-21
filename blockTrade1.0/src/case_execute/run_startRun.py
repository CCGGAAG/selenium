'''
Created on 2017年4月26日

@author: test
'''
import os,time
k=1
while k <2:
    now_time=time.strftime('%H_%M')
    if now_time == '17_18':
        print("开始运行脚本:")
        os.chdir("D:\eclipse\workspace\blockTrade1.0\src\case_execute")
        os.system('Python run_sprint1_all.py') #执行脚本
        print("运行完成退出")
        break
    else:
        time.sleep(10)