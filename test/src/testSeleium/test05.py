from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
# 模拟鼠标操作
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

element1 = driver.find_element_by_css_selector("#id")
ActionChains(driver).context_click(element1).perform()
ActionChains(driver).send
