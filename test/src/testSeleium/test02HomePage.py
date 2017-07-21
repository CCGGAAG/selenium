'''
Created on 2017年4月5日

@author: test
'''
from   selenium     import webdriver
driver1=webdriver.Chrome()
try:
    driver1.get("http://222.209.88.121:9999/zlgxwl/")
    driver1.set_window_size(1200, 800)
    '''
#titile名
    title=str(driver1.title())
    print("打印title:%r"%title)
#url
    now_url= driver1.current_url()
    print(now_url)
    '''
    text=driver1.find_elements_by_css_selector(#copyright)
    print(text)
except Exception:
    print(Exception)
    raise
