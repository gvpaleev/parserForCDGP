from Class.GlobalMethodClass import GlobalMethodClass


class StateHealth(GlobalMethodClass):
    def __init__(self,browser):
        self.browser=browser
        pass

    def insGroupsBefore(self,health,fizkult):

        switch={
            '1':"//span[@class='mat-option-text'][text()=' I группа ']/..",
            '2':"//span[@class='mat-option-text'][text()=' II группа ']/..",
            '3':"//span[@class='mat-option-text'][text()=' III группа ']/..",
            '4':"//span[@class='mat-option-text'][text()=' IV группа ']/..",
            '5':"//span[@class='mat-option-text'][text()=' V группа ']/.."
        }
        while (not self.is_flag(switch[health])):
            self.click("//mat-label[text()='Группа здоровья']/../../../..")

        self.click(switch[health])

        
        switch={
            '1':"//span[@class='mat-option-text'][text()=' I ']/..",
            '2':"//span[@class='mat-option-text'][text()=' II ']/..",
            '3':"//span[@class='mat-option-text'][text()=' III ']/..",
            '4':"//span[@class='mat-option-text'][text()=' IV ']/..",
            '-1':"//span[text()=' не допущен ']/.."
        }

        while(not self.is_flag(switch[fizkult])):
            self.click("//mat-label[text()='Медицинская группа для занятий физической культурой']/../../../mat-select/div")
        self.click(switch[fizkult])

        
        while True:
            if(self.is_flag('//div[@ng-reflect-message="Нажмите для удаления диагноза"]')):
                self.click('//div[@ng-reflect-message="Нажмите для удаления диагноза"]')
                self.click("//button[text()='Да']")
            else:
                break


            
    def addDiagBefore(self,arg):
        self.click("//div[@formgroupname='beforeMedicalExamination']/p[text()=' Добавить диагноз ']")
        
        self.insData(arg['mkb'],"//mat-label[text()='Диагноз']/../../../input")
        self.click("//mat-option")
        self.click("//p[text()=' Изменить диагноз ']/../..//button[text()=' Сохранить ']")
        while (self.is_flag("//p[text()='По результатам проведения настоящего профилактического осмотра']/..//div[@class='mat-tooltip-trigger health-status__diagnoses-delete']")):
            self.click("//p[text()='По результатам проведения настоящего профилактического осмотра']/..//div[@class='mat-tooltip-trigger health-status__diagnoses-delete']")
            self.click("//button[text()='Да']")
    
    def addDiagAfter(self,arg):
        self.click("//p[text()='По результатам проведения настоящего профилактического осмотра']/..//p[text()=' Добавить диагноз ']")
        self.insData(arg['mkb'],"//mat-label[text()='Диагноз']/../../../input")
        self.click("//mat-option")
        #self.click("//p[text()=' Изменить диагноз ']/../..//button[text()=' Сохранить ']")

        dispNablud ={
            '0':"//div[text()=' не установлено ']/../..",
            '1':"//div[text()=' установлено ранее ']/../..",
            '2':"//div[text()=' установлено впервые ']/../.."
        }
        self.click(dispNablud[arg['dispNablud']])


        self.insData(arg['recommendNext'],"//p[text()=' Рекомендации ']/../textarea")
        self.click("//p[text()='Добавить диагноз']/../..//button[text()=' Сохранить ']")

    def save(self):
        self.checkLoading()
        self.click("//button[text()=' Сохранить ']")
        self.checkLoading()

    def nextForm(self,arg):
            self.save()
            self.checkLoading()
            self.click("//p[text()='"+arg+"']")
            self.checkLoading()