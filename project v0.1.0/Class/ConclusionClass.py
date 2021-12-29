from Class.GlobalMethodClass import GlobalMethodClass


class Conclusion(GlobalMethodClass):
    def __init__(self,browser):
        self.browser = browser
        pass

    def insGroups(self,health,fizkult):
        
        
        switch={
            '1':"//span[@class='mat-option-text'][text()=' I группа ']/..",
            '2':"//span[@class='mat-option-text'][text()=' II группа ']/..",
            '3':"//span[@class='mat-option-text'][text()=' III группа ']/..",
            '4':"//span[@class='mat-option-text'][text()=' IV группа ']/..",
            '5':"//span[@class='mat-option-text'][text()=' V группа ']/.."
        }
        while(not self.is_flag(switch[health])):
            self.click("//p[text()='Заключение']/..//mat-label[text()='Группа здоровья']/../../../..")
        self.click(switch[health])

    
        
        switch={
            '1':"//span[@class='mat-option-text'][text()=' I ']/..",
            '2':"//span[@class='mat-option-text'][text()=' II ']/..",
            '3':"//span[@class='mat-option-text'][text()=' III ']/..",
            '4':"//span[@class='mat-option-text'][text()=' IV ']/..",
            '-1':"//span[text()=' не допущен ']/.."
        }
        while(not self.is_flag(switch[fizkult])):
            self.click("//mat-label[text()='Группа для занятий физической культурой']/../../../..")
        self.click(switch[fizkult])


    def insZakName(self,arg):
        if (arg == 'ЗАГРЕКОВА'):
            arg = 'Васильева'
        self.insData(arg,"//mat-label[text()='Лицо, давшее заключение']/../../../input")
        self.click("//mat-option")    
    
    def insDateZakl(self,arg):
        date = arg.split('-')
        date = date[2]+date[1]+date[0]

        if(self.is_flag("//mat-label[text()=' Дата заключения ']/../../../input")):
            self.insData(date,"//mat-label[text()=' Дата заключения ']/../../../input")
        if(self.is_flag("//p[text()='ПЕДИАТР']/../../bs-date-picker//input")):
            self.insData(date,"//p[text()='ПЕДИАТР']/../../bs-date-picker//input")
        if(self.is_flag("//p[text()='НЕВРОЛОГ']/../../bs-date-picker//input")):
            self.insData(date,"//p[text()='НЕВРОЛОГ']/../../bs-date-picker//input")
        if(self.is_flag("//p[text()='ОФТАЛЬМОЛОГ']/../../bs-date-picker//input")):
            self.insData(date,"//p[text()='ОФТАЛЬМОЛОГ']/../../bs-date-picker//input")
        if(self.is_flag("//p[text()='ОТОРИНОЛАРИНГОЛОГ']/../../bs-date-picker//input")):
            self.insData(date,"//p[text()='ОТОРИНОЛАРИНГОЛОГ']/../../bs-date-picker//input")
        if(self.is_flag("//p[text()='СТОМАТОЛОГ ДЕТСКИЙ']/../../bs-date-picker//input")):
            self.insData(date,"//p[text()='СТОМАТОЛОГ ДЕТСКИЙ']/../../bs-date-picker//input")
        if(self.is_flag("//p[text()='ТРАВМАТОЛОГ-ОРТОПЕД']/../../bs-date-picker//input")):
            self.insData(date,"//p[text()='ТРАВМАТОЛОГ-ОРТОПЕД']/../../bs-date-picker//input")
        if(self.is_flag("//p[text()='ПСИХИАТР ПОДРОСТКОВЫЙ']/../../bs-date-picker//input")):
            self.insData(date,"//p[text()='ПСИХИАТР ПОДРОСТКОВЫЙ']/../../bs-date-picker//input")
        if(self.is_flag("//p[text()='ЭНДОКРИНОЛОГ ДЕТСКИЙ (С 5 ЛЕТ)']/../../bs-date-picker//input")):
            self.insData(date,"//p[text()='ЭНДОКРИНОЛОГ ДЕТСКИЙ (С 5 ЛЕТ)']/../../bs-date-picker//input")
        if(self.is_flag("//p[text()='АКУШЕР-ГИНЕКОЛОГ']/../../bs-date-picker//input")):
            self.insData(date,"//p[text()='АКУШЕР-ГИНЕКОЛОГ']/../../bs-date-picker//input")
        if(self.is_flag("//p[text()='ДЕТСКИЙ ХИРУРГ']/../../bs-date-picker//input")):
            self.insData(date,"//p[text()='ДЕТСКИЙ ХИРУРГ']/../../bs-date-picker//input")

        if(self.is_flag("//p[text()='ДЕТСКИЙ УРОЛОГ-АНДРОЛОГ (С 5 ЛЕТ)']/../../bs-date-picker//input")):
            self.insData(date,"//p[text()='ДЕТСКИЙ УРОЛОГ-АНДРОЛОГ (С 5 ЛЕТ)']/../../bs-date-picker//input")

    def insRecomend(self):
        self.insData('По возрасту',"//mat-label[text()='Рекомендации']/../../../input")

    def save(self):
        self.checkLoading()
        self.click("//button[text()=' Сохранить ']")
        self.checkLoading()
    
    def perform(self):
        self.save()
        self.click("//button[text()=' Выполнено ']")
        self.click("//button[text()='Да']")

