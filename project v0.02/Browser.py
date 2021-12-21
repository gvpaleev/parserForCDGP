from selenium import webdriver
from time import sleep


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

    def home(self):
        self.getURL("https://orph.egisz.rosminzdrav.ru/patient-card")
        self.examinationElement("//h5[text()='Карта ребенка']")
    def sexChild(self,arg):
        if(arg=='2'):
            self.click("//SPAN[text()='Мужской']/../../..")
            self.click("//span[text()='Женский']/..")
        
    def snilsChild(self,arg):
        if(self.examinationElement("//mat-label[text()=' СНИЛС ']")):
            self.insData(arg,"//INPUT[@id='mat-input-5']")
        
    def notSnilsChild(self):
        self.click("//input[@id='mat-checkbox-1-input']/../..")
        self.click("//mat-label[text()='Причина отсутствия СНИЛС ']/../../../..")
        self.click("//span[text()='Другое']/..")

        if(self.examinationElement("//mat-label[text()=' Введите причину отсутствия СНИЛС ']")):
            self.insData('-',"//INPUT[@id='mat-input-6']")

    def lastChild (self,arg):
        if(self.examinationElement("//mat-label[text()=' Фамилия ']")):
            self.insData(arg,"//INPUT[@id='mat-input-2']")

    def firstChild (self,arg):
        if(self.examinationElement("//mat-label[text()=' Имя ']")):
            self.insData(arg,"//INPUT[@id='mat-input-3']")
        
    def middleChild (self,arg):
        if(self.examinationElement("//mat-label[text()=' Отчество ']")):
                self.insData(arg,"//INPUT[@id='mat-input-4']")

    def birthChild(self,arg):

        dr = arg.split('-')
        if(self.examinationElement("//mat-label[text()=' Дата рождения ']")):
            self.insData('{}{}{}'.format(dr[2],dr[1],dr[0]),'//INPUT[@id="mat-input-0"]')
    
    def getCard(self):
        try:
            return self.examinationElement("//mat-icon[text()='report']/..[@mattooltip='Пациенты с таким ФИО существуют']",stop = 10)
        except:
            return False

    def cliclCard(self):
        self.click("//mat-icon[text()='report']/..[@mattooltip='Пациенты с таким ФИО существуют']")        
        element = self.browser.find_element_by_xpath("//div[@class='dup_pat_data ng-star-inserted']/a")
        url = element.get_attribute('href')
        self.getURL(url)
    #______________________________        
    
    #______________________________
    def getURL(self,url):
        self.checkLoading()
        self.browser.get(url)
    
    def click(self,xpath):
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
        
    