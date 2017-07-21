'''
Created on 2017年5月25日

@author: test
'''
import logging
import sys
def logger():
        """ 获取logger"""
        logger = logging.getLogger()
        
        if not logger.handlers:
            # 指定logger输出格式
            formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
            # 文件日志
            file_handler = logging.FileHandler("log/haha.log")
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