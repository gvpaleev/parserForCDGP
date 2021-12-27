from selenium import webdriver
from time import sleep
from datetime import datetime,timedelta


class ParentsClass():

#public    
    def getURL(self,url):
        self.checkLoading()
        self.browser.get(url)
        self.checkLoading()
    
    def click(self,xpath):
        self.checkLoading()
        self.examinationElement(xpath)
        element = self.browser.find_element_by_xpath(xpath)
        element.click()
        self.checkLoading()
        sleep(0.25)

    def is_flag(self,xpath,stop = 1):
        while True:
            
            try:
                return self.browser.find_element_by_xpath(xpath)
            except:

                if (not stop):
                    return False

                stop-=1 
                sleep(0.1)
                
                

    def insData(self,data,xpath):

        self.checkLoading()
        self.examinationElement(xpath)

        inp = self.browser.find_element_by_xpath(xpath)
        inp.clear()
        inp.send_keys(data)
        self.checkLoading()

    def examinationElement(self,xpath,stop = 50):
        self.checkLoading()
        
        while True:
            try:
                return self.browser.find_element_by_xpath(xpath) 

            except:

                if (not stop):
                    print('find({})'.format(xpath))
                    raise ValueError('No find '+xpath)

                stop-=1 
                sleep(0.1)
        

#private
    def checkLoading(self):

        while True:
            if (self.is_flag("//mat-spinner")):
                continue

            state = self.browser.execute_script('return document.readyState')
            
            if (not  state == "complete"):
                continue
            else:
                return        
    