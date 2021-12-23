from ParentsClass  import ParentsClass


class Proinspection(ParentsClass):
    def __init__(self,browser):
        super().__init__()
        self.browser = browser


    def goProinspection(self,url):
        super().getURL(url)
        super().checkLoading()
    
    def insLocation(self):
        super().insData('Череповец',"//mat-label[text()='Место постоянного пребывания']/../../../input")
        super().click("//mat-option[@title='Вологодская Область, г. Череповец']")

    def insOMS(self):
        super().insData('35003',"//mat-label[text()='Страховая медицинская организация']/../../../input")
        super().click("""//mat-option[@title='35003 - ВОЛОГОДСКИЙ ФИЛИАЛ АКЦИОНЕРНОГО ОБЩЕСТВА "СТРАХОВАЯ КОМПАНИЯ "СОГАЗ-МЕД" - Вологодская область']""")

    def insNumPolis(self,arg):
        super().insData(arg,"//span[text()='Номер полиса']/../../../input")

    def save(self):
        
        super().click("//button[text()=' Сохранить ']")

    def nextForm(self,arg):
            super().click("//p[text()='"+arg+"']")
            super().checkLoading()

    def insHeight(self,arg):
        super().insData(arg,"//span[text()='Рост, см']/../../../input")

    def insWeight(self,arg):
        super().insData(arg,"//span[text()='Вес, кг']/../../../input")
    
    def violations(self):
        super().click("//p[text()='Вес']/../div//mat-radio-button")
        super().click("//p[text()='Рост']/../div//mat-radio-button")


    def evaluationSex(self):

        super().click("//mat-select[@ng-reflect-name='p']/div")
        super().click("//span[text()=' 0 ']/..")
        super().click("//mat-select[@ng-reflect-name='ax']/div")
        super().click("//span[text()=' 0 ']/..")
        super().click("//mat-select[@ng-reflect-name='ma']/div")
        super().click("//span[text()=' 0 ']/..")
        super().click("//mat-select[@ng-reflect-name='me']/div")
        super().click("//span[text()=' 0 ']/..")

        super().click("//span[text()=' Отсутствует ']/../..")

    def insHealthGroupBefore(self,arg):
        super().click("//span[text()='I группа']/../../..")
        switch={
            '1':"//span[@class='mat-option-text'][text()=' I группа ']/..",
            '2':"//span[@class='mat-option-text'][text()=' II группа ']/..",
            '3':"//span[@class='mat-option-text'][text()=' III группа ']/..",
            '4':"//span[@class='mat-option-text'][text()=' IV группа ']/..",
            '5':"//span[@class='mat-option-text'][text()=' V группа ']/.."
        }
        super().click(switch[arg])

    def insFizkultGroupBefore(self,arg):
        super().click("//mat-label[text()='Медицинская группа для занятий физической культурой']/../../../mat-select/div")
        switch={
            '1':"//span[@class='mat-option-text'][text()=' I ']/..",
            '2':"//span[@class='mat-option-text'][text()=' II ']/..",
            '3':"//span[@class='mat-option-text'][text()=' III ']/..",
            '4':"//span[@class='mat-option-text'][text()=' IV ']/..",
            '-1':"//span[text()=' не допущен ']/.."
        }
        super().click(switch[arg])

    def addDiagBefore(self):
        super().click("//div[@formgroupname='beforeMedicalExamination']/p[text()=' Добавить диагноз ']")

    def insDiagBef(self,arg):
        super().insData(arg,"//mat-label[text()='Диагноз']/../../../input")
        super().click("//mat-option")
        super().click("//p[text()=' Изменить диагноз ']/../..//button[text()=' Сохранить ']")
        super().click("//p[text()='По результатам проведения настоящего профилактического осмотра']/..//div[@class='mat-tooltip-trigger health-status__diagnoses-delete']")
        super().click("//button[text()='Да']")

    def insFormIsskedDefaut(self,date):
        date = date.split('-')
        super().insData(date[2]+date[1]+date[0],"//p[text()='Общий анализ крови']/../..//mat-label[text()=' Введите дату ']/../../../input")
        super().insData('Норма',"//p[text()='Общий анализ крови']/../..//span[text()='Результат']/../../..//textarea")
        super().insData(date[2]+date[1]+date[0],"//p[text()='Общий анализ мочи']/../..//mat-label[text()=' Введите дату ']/../../../input")
        super().insData('Норма',"//p[text()='Общий анализ мочи']/../..//span[text()='Результат']/../../..//textarea")