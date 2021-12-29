from Class.GlobalMethodClass import GlobalMethodClass


class InserOsmotr(GlobalMethodClass):
    def __init__(self,browser):
        self.browser = browser
    
    def goFullCard(self,url):
        self.getURL(url)
        self.checkLoading()
        
        
        
        if(self.is_flag("//mat-label[text()=' Введите причину отсутствия СНИЛС ']/../../../input",stop=250)):
            self.insData('-',"//mat-label[text()=' Введите причину отсутствия СНИЛС ']/../../../input")


    def is_inspection(self):
        self.checkLoading()
        return   self.is_flag("//p[text()=' Заполняется ']/../a")
    
    def getUrlInspection(self):
        return self.is_flag("//p[text()=' Заполняется ']/../a").get_attribute('href')
        
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
        self.checkLoading()
        return self.is_flag("//div[text()=' Карта осмотра пациента с такой возрастной группой уже существует ']") 