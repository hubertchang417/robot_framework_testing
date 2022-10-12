from email.charset import add_charset
from lib2to3.pgen2 import driver
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import re
from robot.libraries.BuiltIn import BuiltIn


class Custom_GoogleSearch1:
    ROBOT_LIBRARY_SCOPE = 'SUITE'
    
    def __init__(self) -> None:
        self.driver = ""
    
    @property
    def driver(self):
        return self._driver
    
    @driver.setter
    def driver(self,site):
        if site != '':
            self._driver = webdriver.Chrome()
            self._driver.maximize_window()
            self._driver.get(site)
    
    def go_start(self,site):
        self.driver = site
    
    def search_target(self,target):
        se = self.driver.find_element(By.XPATH,"//input[@class='gLFyf gsfi']")
        se.send_keys(target)
        se_bnt = self.driver.find_element(By.XPATH,"//input[@class='gNO89b']")
        se_bnt.click()
    
    def find_site(self, target, count = 1):
        #target = '維基百科'
        if count>5:
            # robot log
            BuiltIn.log_to_console(f'Target Not Found! (From Page1 to Page 5)')
            return

        main_lists = self.driver.find_element(By.XPATH,"//div[@class='v7W49e']")
        lists_title = main_lists.find_elements(By.XPATH,"//h3[@class='LC20lb MBeuO DKV0Md']")
        #lists_http = main_lists.find_elements(By.XPATH,"//div[@class='TbwUpd NJjxre']/cite[@class='iUh30 qLRx3b tjvcx']")
        
        idx = 0
        pre_pos=0
        
        while idx<len(lists_title):
            #scroll to title
            for i in range(pre_pos,lists_title[idx].location['y']-75,20):
                self.driver_scroll_to(i) 
            
            self.driver_scroll_to(lists_title[idx].location['y']-75)
            ActionChains(self.driver).move_to_element(lists_title[idx]).perform()
            #check title if found target
            if lists_title[idx].text.find(target) != -1:
                lists_title[idx].click()
                break
            
            pre_pos = lists_title[idx].location['y']-75
            #print(lists_title[idx].location,lists_title[idx].text)
            sleep(0.5)
            idx+=1
        #not found in this page
        if idx==len(lists_title):
            #scroll to bot
            bottom_height = self.driver.execute_script("return document.body.scrollHeight;")
            for i in range(pre_pos,bottom_height,40):
                self.driver_scroll_to(i)

            #click next page
            next_page = self.driver.find_element(By.XPATH,"//a[@id='pnnext']")
            next_page.click()
            #call find site
            self.find_site(target,count+1)
    def driver_scroll_to_bottom(self, speed = 50): 
        
        max_height = self.driver.execute_script("return document.body.scrollHeight;")
        
        for i in range(0,max_height,speed):
            self.driver_scroll_to(i)
            sleep(0.1)
        
    def driver_scroll_to(self, y, x=0):
        self.driver.execute_script(f"window.scrollTo({x}, {y})")
        sleep(0.1)
    
    def driver_close(self):
        self.driver.close()
if __name__ == "__main__":
    
    webb=Custom_GoogleSearch1()
    webb.driver='http://www.google.com.tw'
    webb.search_target('nas')
    webb.find_site('維基百科')
    webb.driver_scroll_to_bottom(100)
    #ActionChains(webb.driver).
    #webb.driver.execute_script("window.scrollTo(0, 500)") 
    webb.driver_close()