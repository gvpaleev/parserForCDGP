from ParentsClass  import ParentsClass


class ChildsCard(ParentsClass):

    def __init__(self,browser):
        super().__init__()
        self.browser = browser
    
    def installHome(self):

        login = '+79922800580'
        password = 'yz0_NX!4_'


        super().getURL('https://orph.egisz.rosminzdrav.ru/')
        super().click("//A[text()='Войти']")
        super().insData(login,"//INPUT[@id='login']")
        super().insData(password,"//INPUT[@id='password']")
        super().click("//BUTTON[@id='loginByPwdButton']")
        if(super().examinationElement("//a[text()=' ПАЛЕЕВ Г. В ']")):
            print('URL:https://orph.egisz.rosminzdrav.ru Ready')

    def goHome(self):

        self.getURL("https://orph.egisz.rosminzdrav.ru/patient-card")
        self.examinationElement("//h5[text()='Карта ребенка']")
    
    def insSexChild(self,arg):
        if(arg=='2'):
            self.click("//SPAN[text()='Мужской']/../../..")
            self.click("//span[text()='Женский']/..")
        
    def insSnilsChild(self,arg):
        if(self.examinationElement("//mat-label[text()=' СНИЛС ']")):
            self.insData(arg,"//INPUT[@id='mat-input-5']")
        
    def insNotSnilsChild(self):
        self.click("//input[@id='mat-checkbox-1-input']/../..")
        self.click("//mat-label[text()='Причина отсутствия СНИЛС ']/../../../..")
        self.click("//span[text()='Другое']/..")

        if(self.examinationElement("//mat-label[text()=' Введите причину отсутствия СНИЛС ']")):
            self.insData('-',"//INPUT[@id='mat-input-6']")

    def insLastChild (self,arg):
        if(self.examinationElement("//mat-label[text()=' Фамилия ']")):
            self.insData(arg,"//INPUT[@id='mat-input-2']")

    def insFirstChild (self,arg):
        if(self.examinationElement("//mat-label[text()=' Имя ']")):
            self.insData(arg,"//INPUT[@id='mat-input-3']")
        
    def insMiddleChild (self,arg):
        if(self.examinationElement("//mat-label[text()=' Отчество ']")):
                self.insData(arg,"//INPUT[@id='mat-input-4']")

    def insBirthChild(self,arg):

        dr = arg.split('-')
        if(self.examinationElement("//mat-label[text()=' Дата рождения ']")):
            self.insData('{}{}{}'.format(dr[2],dr[1],dr[0]),'//INPUT[@id="mat-input-0"]')
    
    def getCard(self):
        try:
            if(self.examinationElement("//mat-icon[text()='report']/..[@mattooltip='Пациенты с таким ФИО существуют']",stop = 30)):
                super().click("//mat-icon[text()='report']/..[@mattooltip='Пациенты с таким ФИО существуют']")        
                element = self.browser.find_element_by_xpath("//div[@class='dup_pat_data ng-star-inserted']/a")
                url = element.get_attribute('href')
                return url
        except:
            return False
