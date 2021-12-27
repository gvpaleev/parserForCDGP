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
        #pass
        super().checkLoading()
        super().click("//button[text()=' Сохранить ']")
        super().checkLoading()

    def nextForm(self,arg):
            super().checkLoading()
            super().click("//p[text()='"+arg+"']")
            super().checkLoading()

    def is_psixRaz(self):
        return super().is_flag("//p[text()=' Оценка психического развития для детей 0-4 лет ' ]")

    def insOkrGol(self,arg):
        if(super().is_flag("//span[text()='Окружность головы, см']/../../../input")):
            super().insData('20',"//span[text()='Окружность головы, см']/../../../input")

    def insFormPsixRazDefold(self,arg):
        super().insData(arg,"//span[text()='Познавательная функция (возраст развития)']/../../../input")
        super().insData(arg,"//span[text()='Моторная функция (возраст развития)']/../../../input")
        super().insData(arg,"//span[text()='Предречевое и речевое развитие (возраст развития)']/../../../input")
        super().insData(arg,"//span[text()='Эмоциональная и социальная (контакт с окружающим миром) функции (возраст развития)']/../../../input")
        
    
    
    
    
    
    def insHeight(self,arg):
        super().insData(arg,"//span[text()='Рост, см']/../../../input")

    def insWeight(self,arg):
        super().insData(arg,"//span[text()='Вес, кг']/../../../input")
    
    def violations(self):
        super().click("//p[text()='Вес']/../div//mat-radio-button")
        super().click("//p[text()='Рост']/../div//mat-radio-button")


    def evaluationSex(self):
        
        if(super().is_flag("//mat-select[@ng-reflect-name='p']/div")):
            super().click("//mat-select[@ng-reflect-name='p']/div")
            super().click("//span[text()=' 0 ']/..")
        
        if(super().is_flag("//mat-select[@ng-reflect-name='ax']/div")):    
            super().click("//mat-select[@ng-reflect-name='ax']/div")
            super().click("//span[text()=' 0 ']/..")
        
        if(super().is_flag("//mat-select[@ng-reflect-name='ma']/div")):
            super().click("//mat-select[@ng-reflect-name='ma']/div")
            super().click("//span[text()=' 0 ']/..")

        if(super().is_flag("//mat-select[@ng-reflect-name='me']/div")):    
            super().click("//mat-select[@ng-reflect-name='me']/div")
            super().click("//span[text()=' 0 ']/..")
        
        if(super().is_flag("//mat-select[@ng-reflect-name='fa']/div")):    
            super().click("//mat-select[@ng-reflect-name='fa']/div")
            super().click("//span[text()=' 0 ']/..")


        if(super().is_flag("//span[text()=' Отсутствует ']/..//input[@aria-checked='false']") and super().is_flag("//span[text()=' Отсутствует ']/../..")):
                super().click("//span[text()=' Отсутствует ']/../..")

    def insHealthGroupBefore(self,arg):
        super().click("//mat-label[text()='Группа здоровья']/../../../..")
        switch={
            '1':"//span[@class='mat-option-text'][text()=' I группа ']/..",
            '2':"//span[@class='mat-option-text'][text()=' II группа ']/..",
            '3':"//span[@class='mat-option-text'][text()=' III группа ']/..",
            '4':"//span[@class='mat-option-text'][text()=' IV группа ']/..",
            '5':"//span[@class='mat-option-text'][text()=' V группа ']/.."
        }
        if(not super().is_flag(switch[arg])):
            super().click("//mat-label[text()='Группа здоровья']/../../../..")
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

    def addDiagAfter(self):
        super().click("//p[text()='По результатам проведения настоящего профилактического осмотра']/..//p[text()=' Добавить диагноз ']")

    def clearDiagnos(self):
        while True:
            if(super().is_flag('//div[@ng-reflect-message="Нажмите для удаления диагноза"]')):
                super().click('//div[@ng-reflect-message="Нажмите для удаления диагноза"]')
                super().click("//button[text()='Да']")
            else:
                break
        

    def insDiagBef(self,arg):
        super().insData(arg['mkb'],"//mat-label[text()='Диагноз']/../../../input")
        super().click("//mat-option")
        super().click("//p[text()=' Изменить диагноз ']/../..//button[text()=' Сохранить ']")
        super().click("//p[text()='По результатам проведения настоящего профилактического осмотра']/..//div[@class='mat-tooltip-trigger health-status__diagnoses-delete']")
        super().click("//button[text()='Да']")

    def insDiagAft(self,arg):
        super().insData(arg['mkb'],"//mat-label[text()='Диагноз']/../../../input")
        super().click("//mat-option")
        #super().click("//p[text()=' Изменить диагноз ']/../..//button[text()=' Сохранить ']")

        dispNablud ={
            '0':"//div[text()=' не установлено ']/../..",
            '1':"//div[text()=' установлено ранее ']/../..",
            '2':"//div[text()=' установлено впервые ']/../.."
        }
        super().click(dispNablud[arg['dispNablud']])


        super().insData(arg['recommendNext'],"//p[text()=' Рекомендации ']/../textarea")
        super().click("//p[text()='Добавить диагноз']/../..//button[text()=' Сохранить ']")

        

    def insFormIsskedDefaut(self,date):
        date = date.split('-')
        if(super().is_flag("//p[text()='Общий анализ крови']/../..//mat-label[text()=' Введите дату ']/../../../input")):
            super().insData(date[2]+date[1]+date[0],"//p[text()='Общий анализ крови']/../..//mat-label[text()=' Введите дату ']/../../../input")
            super().insData('Норма',"//p[text()='Общий анализ крови']/../..//span[text()='Результат']/../../..//textarea")
        
        if(super().is_flag("//p[text()='Общий анализ мочи']/../..//mat-label[text()=' Введите дату ']/../../../input")):
            super().insData(date[2]+date[1]+date[0],"//p[text()='Общий анализ мочи']/../..//mat-label[text()=' Введите дату ']/../../../input")
            super().insData('Норма',"//p[text()='Общий анализ мочи']/../..//span[text()='Результат']/../../..//textarea")

        if(super().is_flag("//p[text()='Электрокардиография']/../..//mat-label[text()=' Введите дату ']/../../../input")):
            super().insData(date[2]+date[1]+date[0],"//p[text()='Электрокардиография']/../..//mat-label[text()=' Введите дату ']/../../../input")
            super().insData('Норма',"//p[text()='Электрокардиография']/../..//span[text()='Результат']/../../..//textarea")

    def insHealthGroup(self,arg):
        super().click("//p[text()='Заключение']/..//mat-label[text()='Группа здоровья']/../../../..")
        switch={
            '1':"//span[@class='mat-option-text'][text()=' I группа ']/..",
            '2':"//span[@class='mat-option-text'][text()=' II группа ']/..",
            '3':"//span[@class='mat-option-text'][text()=' III группа ']/..",
            '4':"//span[@class='mat-option-text'][text()=' IV группа ']/..",
            '5':"//span[@class='mat-option-text'][text()=' V группа ']/.."
        }
        if(not super().is_flag(switch[arg])):
            super().click("//p[text()='Заключение']/..//mat-label[text()='Группа здоровья']/../../../..")
        super().click(switch[arg])

    def insFizkultGroup(self,arg):
        super().click("//mat-label[text()='Группа для занятий физической культурой']/../../../..")
        switch={
            '1':"//span[@class='mat-option-text'][text()=' I ']/..",
            '2':"//span[@class='mat-option-text'][text()=' II ']/..",
            '3':"//span[@class='mat-option-text'][text()=' III ']/..",
            '4':"//span[@class='mat-option-text'][text()=' IV ']/..",
            '-1':"//span[text()=' не допущен ']/.."
        }
        super().click(switch[arg])

    def insZakName(self,arg):
        if (arg == 'ЗАГРЕКОВА'):
            arg = 'Васильева'
        super().insData(arg,"//mat-label[text()='Лицо, давшее заключение']/../../../input")
        super().click("//mat-option")

    def insDateZakl(self,arg):
        date = arg.split('-')
        date = date[2]+date[1]+date[0]

        if(super().is_flag("//mat-label[text()=' Дата заключения ']/../../../input")):
            super().insData(date,"//mat-label[text()=' Дата заключения ']/../../../input")
        if(super().is_flag("//p[text()='ПЕДИАТР']/../../bs-date-picker//input")):
            super().insData(date,"//p[text()='ПЕДИАТР']/../../bs-date-picker//input")
        if(super().is_flag("//p[text()='НЕВРОЛОГ']/../../bs-date-picker//input")):
            super().insData(date,"//p[text()='НЕВРОЛОГ']/../../bs-date-picker//input")
        if(super().is_flag("//p[text()='ОФТАЛЬМОЛОГ']/../../bs-date-picker//input")):
            super().insData(date,"//p[text()='ОФТАЛЬМОЛОГ']/../../bs-date-picker//input")
        if(super().is_flag("//p[text()='ОТОРИНОЛАРИНГОЛОГ']/../../bs-date-picker//input")):
            super().insData(date,"//p[text()='ОТОРИНОЛАРИНГОЛОГ']/../../bs-date-picker//input")
        if(super().is_flag("//p[text()='СТОМАТОЛОГ ДЕТСКИЙ']/../../bs-date-picker//input")):
            super().insData(date,"//p[text()='СТОМАТОЛОГ ДЕТСКИЙ']/../../bs-date-picker//input")
        if(super().is_flag("//p[text()='ТРАВМАТОЛОГ-ОРТОПЕД']/../../bs-date-picker//input")):
            super().insData(date,"//p[text()='ТРАВМАТОЛОГ-ОРТОПЕД']/../../bs-date-picker//input")
        if(super().is_flag("//p[text()='ПСИХИАТР ПОДРОСТКОВЫЙ']/../../bs-date-picker//input")):
            super().insData(date,"//p[text()='ПСИХИАТР ПОДРОСТКОВЫЙ']/../../bs-date-picker//input")
        if(super().is_flag("//p[text()='ЭНДОКРИНОЛОГ ДЕТСКИЙ (С 5 ЛЕТ)']/../../bs-date-picker//input")):
            super().insData(date,"//p[text()='ЭНДОКРИНОЛОГ ДЕТСКИЙ (С 5 ЛЕТ)']/../../bs-date-picker//input")
        if(super().is_flag("//p[text()='АКУШЕР-ГИНЕКОЛОГ']/../../bs-date-picker//input")):
            super().insData(date,"//p[text()='АКУШЕР-ГИНЕКОЛОГ']/../../bs-date-picker//input")
        if(super().is_flag("//p[text()='ДЕТСКИЙ ХИРУРГ']/../../bs-date-picker//input")):
            super().insData(date,"//p[text()='ДЕТСКИЙ ХИРУРГ']/../../bs-date-picker//input")

        if(super().is_flag("//p[text()='ДЕТСКИЙ УРОЛОГ-АНДРОЛОГ (С 5 ЛЕТ)']/../../bs-date-picker//input")):
            super().insData(date,"//p[text()='ДЕТСКИЙ УРОЛОГ-АНДРОЛОГ (С 5 ЛЕТ)']/../../bs-date-picker//input")

    def insRecomend(self):
        super().insData('По возрасту',"//mat-label[text()='Рекомендации']/../../../input")

    def perform(self):
        super().click("//button[text()=' Выполнено ']")
        super().click("//button[text()='Да']")
    