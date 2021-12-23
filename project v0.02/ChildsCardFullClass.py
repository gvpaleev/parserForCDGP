from time import sleep
from ParentsClass  import ParentsClass


class ChildsCardFull(ParentsClass):
    def __init__(self,browser):
        super().__init__()
        self.browser = browser
    
    def goFullCard(self,url):
        super().getURL(url)
        super().checkLoading()
        sleep(2)
        if(super().is_flag("//mat-label[text()=' Введите причину отсутствия СНИЛС ']/../../../input")):
            super().insData('-',"//mat-label[text()=' Введите причину отсутствия СНИЛС ']/../../../input")


    def is_inspection(self):
        super().checkLoading()
        return   super().is_flag("//p[text()=' Заполняется ']/../a")
    
    def getUrlInspection(self):
        return super().is_flag("//p[text()=' Заполняется ']/../a").get_attribute('href')
        
    def addInspection(self):
        self.click("//div[text()=' Карты осмотра ']/div/mat-icon[text()='add']")

    def dateObsled(self,arg):
        date = arg.split('-')
        self.insData(date[2]+date[1]+date[0],"//div[text()=' Создание карты осмотра ']/..//div/div/input[@placeholder='00.00.0000']")


    def setAge(self,before,after):
        before = before.split('-')
        after = after.split('-')
        
        age = 2021 - int(before[0]) 

        self.click("//label[text()='Возрастная группа:']/..//div/div")
        if (age<5):
            self.click("//span[text()=' {} года ']/..".format(age))
        else:
            self.click("//span[text()=' {} лет ']/..".format(age))
    
    def createInspection(self):
        self.click("//button[text()='Создать ']")
        self.checkLoading()
        
    def sellectUrl(self):
        return self.browser.current_url

    def is_creadInspection(self):
        return super().is_flag("//div[text()=' Карта осмотра пациента с такой возрастной группой уже существует ']") 
