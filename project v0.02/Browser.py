from selenium import webdriver
from time import sleep
from datetime import datetime,timedelta


class Browser():

    def __init__(self,path):
        self.browser = webdriver.Firefox(executable_path=r''+path)

        self.login = '+79922800580'
        self.password = 'yz0_NX!4_'


        self.getURL('https://orph.egisz.rosminzdrav.ru/')
        self.click("//A[text()='Войти']")
        self.insData(self.login,"//INPUT[@id='login']")
        self.insData(self.password,"//INPUT[@id='password']")
        self.click("//BUTTON[@id='loginByPwdButton']")
        if(self.examinationElement("//a[text()=' ПАЛЕЕВ Г. В ']")):
            print('URL:https://orph.egisz.rosminzdrav.ru Ready')

    
    
    def cliclCard(self):
        self.click("//mat-icon[text()='report']/..[@mattooltip='Пациенты с таким ФИО существуют']")        
        element = self.browser.find_element_by_xpath("//div[@class='dup_pat_data ng-star-inserted']/a")
        url = element.get_attribute('href')
        self.getURL(url)
        sleep(1)
        self.checkLoading()
        if(self.is_flag("//mat-label[text()=' Введите причину отсутствия СНИЛС ']")):
            self.insData('-',"//INPUT[@id='mat-input-6']")



    
    #______________________________        
    
        def is_FilledIn(self):
        if(self.is_flag("//p[text()=' Заполняется ']")):
            return   self.is_flag("//p[text()=' Заполняется ']/../a")
        else:
            return False
    #______________________________
    def getURL(self,url):
        self.checkLoading()
        self.browser.get(url)
    
    def click(self,xpath):
        self.checkLoading()
        self.examinationElement(xpath)
        element = self.browser.find_element_by_xpath(xpath)
        element.click()
        sleep(0.25)

    def checkLoading(self):

        while True:
            if (self.is_flag("//mat-spinner[@class='mat-spinner mat-progress-spinner spinner mat-primary mat-progress-spinner-indeterminate-animation ng-star-inserted']")):
                continue

            state = self.browser.execute_script('return document.readyState')
            
            if (not  state == "complete"):
                continue
            else:
                return          

    def is_flag(self,xPath):
        sleep(0.1)
        try:
            return self.browser.find_element_by_xpath(xPath)
        except:
            return False

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
        
    