'''
Created on 2017年4月1日

@author: test
'''
import time
from   selenium     import webdriver
#driver1 = webdriver.Chrome()
driver1 = webdriver.Chrome()
'''    baidu-多行注释
driver1.get("http://www.baidu.com")
driver1.find_element_by_id("kw").send_keys("123")
driver1.find_element_by_id("su").click()
'''
driver1.get("http://www.zsteel.cc")
driver1.maximize_window()
time.sleep(7)
driver1.find_element_by_id("jiaoyi").click()
driver1.find_element_by_link_text('登录').click()
time.sleep(7)
driver1.quit()

