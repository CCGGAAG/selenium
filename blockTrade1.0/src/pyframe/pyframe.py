# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, os

class PyFrame(object):
    '''
    PyFrame framework is used for making webdriver easier to use.
    '''
    
    def __init__(self, browser='chrome'):
        '''
        The default web browser is "chrome"
        
        Usage:
        driver=PyUtil("chrome")
        driver=PyUtil()
        '''
        if browser == "firefox" or browser == "ff":
            driver = webdriver.Firefox()
        elif browser == "chrome":
            driver = webdriver.Chrome()
        elif browser == "internet explorer" or browser == "ie":
            driver = webdriver.Ie()
        elif browser == "opera":
            driver = webdriver.Opera()
        elif browser == 'edge':
            driver = webdriver.Edge()
        try:
            self.driver = driver
        except Exception:
            raise NameError("Not found %s browser,You can enter 'ie', 'ff', 'opera',  'edge' or 'chrome'." % browser)


    def wait_element_by(self, element_type,element_value, secs=10):
        '''
        Waiting for an element to display.

        Usage:
        driver.wait_element_by("id","su",10)
        '''
        if element_type == "id":
            WebDriverWait(self.driver,secs,1).until(EC.presence_of_element_located((By.ID, element_value)))
        elif element_type == "name":
            WebDriverWait(self.driver,secs,1).until(EC.presence_of_element_located((By.NAME, element_value)))
        elif element_type == "class":
            WebDriverWait(self.driver,secs,1).until(EC.presence_of_element_located((By.CLASS_NAME, element_value)))
        elif element_type == "link_text":
            WebDriverWait(self.driver,secs,1).until(EC.presence_of_element_located((By.LINK_TEXT, element_value)))
        elif element_type == "partial_link_text":
            WebDriverWait(self.driver,secs,1).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, element_value)))
        elif element_type == "xpath":
            WebDriverWait(self.driver,secs,1).until(EC.presence_of_element_located((By.XPATH, element_value)))
        elif element_type == "css":
            WebDriverWait(self.driver,secs,1).until(EC.presence_of_element_located((By.CSS_SELECTOR, element_value)))
        else:
            raise NameError("Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")


    def get_element_by(self,element_type,element_value):
        '''
        Judge element positioning way, and returns the element.
        
        Usage:
        driver.get_element_by("id","username")
        '''
        if element_type == "id":
            element = self.driver.find_element_by_id(element_value)
        elif element_type == "name":
            element = self.driver.find_element_by_name(element_value)
        elif element_type == "class":
            element = self.driver.find_element_by_class_name(element_value)
        elif element_type == "link_text":
            element = self.driver.find_element_by_link_text(element_value)
        elif element_type =="partial_link_text":
            element = self.driver.find_element_by_partial_link_text(element_value)
        elif element_type == "xpath":
            element = self.driver.find_element_by_xpath(element_value)
        elif element_type == "css":
            element = self.driver.find_element_by_css_selector(element_value)
        else:
            raise NameError("Please enter the correct targeting elements,'id','name','class','link_text','partial_link_text','xpath','css'.")
        return element

    def get_elements_by(self,elements_type,elements_value):
        '''
        Judge elements positioning way, and returns the elements.
        
        Usage:
        driver.get_elements_by("id","username")
        '''
        if elements_type == "id":
            elements = self.driver.find_elements_by_id(elements_value)
        elif elements_type == "name":
            elements = self.driver.find_elements_by_name(elements_value)
        elif elements_type == "class":
            elements = self.driver.find_elements_by_class_name(elements_value)
        elif elements_type == "link_text":
            elements = self.driver.find_elements_by_link_text(elements_value)
        elif elements_type =="partial_link_text":
            elements = self.driver.find_elements_by_partial_link_text(elements_value)
        elif elements_type == "xpath":
            elements = self.driver.find_elements_by_xpath(elements_value)
        elif elements_type == "css":
            elements = self.driver.find_elements_by_css_selector(elements_value)
        else:
            raise NameError("Please enter the correct targeting elementss,'id','name','class','link_text','partial_link_text','xpath','css'.")
        return elements

    
    def open(self, url):
        '''
        open web url.

        Usage:
        driver.open("https://www.163.com")
        '''
        self.driver.get(url)


    def max_window(self):
        '''
        Set browser window maximized.

        Usage:
        driver.max_window()
        '''
        self.driver.maximize_window()


    def set_window_size(self, width, height):
        '''
        Set browser window width and height.

        Usage:
        driver.set_window_size(1280,720)
        '''
        self.driver.set_window_size(width, height)


    def input(self, element_type,element_value, text):
        '''
        Operate input box.

        Usage:
        driver.input("id","su","hello world")
        '''
        self.wait_element_by(element_type,element_value)
        el = self.get_element_by(element_type,element_value)
        el.send_keys(text)


    def clear(self, element_type,element_value):
        '''
        Clear the contents of the input box.

        Usage:
        driver.clear("id","su")
        '''
        self.wait_element_by(element_type,element_value)
        el = self.get_element_by(element_type,element_value)
        el.clear()
    
    def inputByEle(self, element, text):
        '''
        Operate input box .

        Usage:
        driver.input(element,"hello world")
        '''
        element.send_keys(text)


    def clearByEle(self, element):
        '''
        Clear the contents of the input box.

        Usage:
        driver.clear()
        '''
        element.clear()
     
    def inputKeysByEle(self,element,Key_type):
        '''
        通过元素和键盘按键名称，模拟键盘的操作
        
        举个栗子：
        element.sendKeys(Keys.ENTER)
        '''
        if Key_type =="BackSpace":
            element.send_keys(Keys.BACK_SPACE)
        elif Key_type =="Space":
            element.send_keys(Keys.SPACE)
        elif Key_type =="Tab":
            element.send_keys(Keys.TAB)
        elif Key_type =="Esc":
            element.send_keys(Keys.ESCAPE)
        elif Key_type =="Enter":
            element.send_keys(Keys.ENTER)
        elif Key_type =="F5":
            element.send_keys(Keys.F5)
        elif Key_type =="Ctrl+A":
            element.send_keys(Keys.CONTROL,'a')
        elif Key_type =="Ctrl+C":
            element.send_keys(Keys.CONTROL,'c')
        elif Key_type =="Ctrl+X":
            element.send_keys(Keys.CONTROL,'x')
        elif Key_type =="Ctrl+V":
            element.send_keys(Keys.CONTROL,'v')
        else :
            raise NameError("请输入BackSpace、Space、Tab、Esc、Enter、F5、Ctrl+A、Ctrl+C、Ctrl+V、Ctrl+X")
    
    
    def inputKeys(self,element_type,element_value,Key_type):
        '''
        通过元素类型、路径、和键盘按键名称，模拟键盘的操作
        
        举个栗子：
        self.driver.find_element_by_id("kw").sendKeys(Keys.ENTER)
        '''
        self.wait_element_by(element_type,element_value)
        element = self.get_element_by(element_type,element_value)
        self.inputKeysByEle(element,Key_type)
    
    def click(self, element_type,element_value,times=1):
        '''
        It can left click any element can be clicked with any times.
        check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.click("id","su",2)
        driver.click("id","su")
        '''
        self.wait_element_by(element_type,element_value)
        el = self.get_element_by(element_type,element_value)
        while times > 0 :
            el.click()
            times-=times


    def right_click(self, element_type,element_value):
        '''
        Right click element.

        Usage:
        driver.right_click("id","su")
        '''
        self.wait_element_by(element_type,element_value)
        el = self.get_element_by(element_type,element_value)
        ActionChains(self.driver).context_click(el).perform()


    def move_to_element(self, element_type,element_value):
        '''
        Mouse over the element.

        Usage:
        driver.move_to_element("id","su")
        '''
        self.wait_element_by(element_type,element_value)
        el = self.get_element_by(element_type,element_value)
        ActionChains(self.driver).move_to_element(el).perform()
        

    def drag_and_drop(self, element_type,element_value, target_type,target_value):
        '''
        Drag an element and drops it.

        Usage:
        driver.drag_and_drop("css=>#el","css=>#ta")
        '''
        self.wait_element_by(element_type,element_value)
        element = self.get_element_by(element_type,element_value)
        self.wait_element_by( target_type,target_value)
        target = self.get_element_by( target_type,target_value)
        ActionChains(driver).drag_and_drop(element, target).perform()


    def click_text_link(self, text):
        '''
        Click the element by the link text

        Usage:
        driver.click_text_link("News")
        '''
        self.driver.find_element_by_partial_link_text(text).click()


    def close(self):
        '''
        Click the "close" button in the title bar of a pop up window or tab.

        Usage:
        driver.close()
        '''
        self.driver.close()


    def quit(self):
        '''
        Quit the driver and close all the windows.

        Usage:
        driver.quit()
        '''
        self.driver.quit()


    def submit(self, element_type, element_value):
        '''
        Submit the specified form.

        Usage:
        driver.submit("css","#id")
        '''
        self.wait_element_by(element_type, element_value)
        el = self.get_element_by(element_type, element_value)
        el.submit()

    def refresh(self):
        '''
        Refresh the current page.

        Usage:
        driver.refresh()
        '''
        self.driver.refresh()


    def execute_js(self, script):
        '''
        Execute JavaScript scripts.

        Usage:
        driver.js("window.scrollTo(200,1000);")
        '''
        self.driver.execute_script(script)


    def get_attribute(self,element_type, element_value, attribute):
        '''
        Gets the value of an element attribute,like the page address.

        Usage:
        driver.get_attribute("css","#el","type")
        '''
        el = self.get_element_by(element_type, element_value)
        return el.get_attribute(attribute)


    def get_text(self, element_type, element_value):
        '''
        Get element text information.

        Usage:
        driver.get_text("css","#el")
        '''
        self.wait_element_by(element_type, element_value)
        el = self.get_element(element_type, element_value)
        return el.text


    def get_element_displayed(self, element_type, element_value):
        '''
        Gets the element to display,The return result is true or false.

        Usage:
        driver.get_element_displayed("css","#el")
        '''
        self.wait_element_by(element_type, element_value)
        el = self.get_element_by(element_type, element_value)
        return el.is_displayed()


    def get_title(self):
        '''
        Get window title.

        Usage:
        driver.get_title()
        '''
        return self.driver.title


    def get_url(self):
        '''
        Get the URL address of the current page.

        Usage:
        driver.get_url()
        '''
        return self.driver.current_url


    def get_current_window_screenshot(self, file_path):
        '''
        Get the current window screenshot.

        Usage:
        driver.get_windows_img()
        '''
        self.driver.get_screenshot_as_file(file_path)


    def wait(self, secs):
        '''
        Implicitly wait.All elements on the page.

        Usage:
        driver.wait(10)
        '''
        self.driver.implicitly_wait(secs)


    def accept_alert(self):
        '''
        Accept warning box.

        Usage:
        driver.accept_alert()
        '''
        self.driver.switch_to.alert.accept()


    def dismiss_alert(self):
        '''
        Dismisses the alert available.

        Usage:
        driver.dismiss_alert()
        '''
        self.driver.switch_to.alert.dismiss()


    def switch_to_frame(self, element_type, element_value):
        '''
        Switch to the specified frame.

        Usage:
        driver.switch_to_frame("id","kw")
        '''
        self.wait_element_by(element_type, element_value)
        iframe_el = self.get_element_by(element_type, element_value)
        self.driver._switch_to.frame(iframe_el)


    def switch_to_default_frame(self):
        '''
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.

        Usage:
        driver.switch_to_default_frame()
        '''
        self.driver._switch_to.default_content()


    def open_new_window(self, element_type, element_value):
        '''
        Open the new window and switch the handle to the newly opened window.

        Usage:
        driver.open_new_window()
        '''
        original_windows = self.driver.current_window_handle
        el = self.get_element_by(element_type, element_value)
        el.click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != original_windows:
                self.driver._switch_to.window(handle)

    def   set_screenshot(self):
        """获取截图"""
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        #必须要打印路径HTMLTestRunner才能捕获并且生成路径，\image\**.png 是获取路径的条件，必须这样的目录
        pic_path = os.path.abspath('...') + "/test_report/img/"+now+'.png'
        print("img/"+now+".png")
        self.driver.save_screenshot(pic_path)
    
    def back(self):
        '''
        返回上一个浏览页面

        Usage:
        driver.back()
        '''
        self.driver.back()
        
    def forward(self):
        '''
       进入下一个浏览页面

        Usage:
        driver.froward()
        '''
        self.driver.forward()
        

if __name__ == '__main__':
    driver = PyFrame("chrome")


















