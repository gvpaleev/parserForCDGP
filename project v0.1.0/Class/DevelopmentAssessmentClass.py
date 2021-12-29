from Class.GlobalMethodClass import GlobalMethodClass


class DevelopmentAssessment(GlobalMethodClass):
    def __init__(self,browser):
        self.browser=browser
        pass

    def insHeightWeight(self,Height,Weight):
        self.checkLoading()
        self.insData(Height,"//span[text()='Рост, см']/../../../input")
        self.insData(Weight,"//span[text()='Вес, кг']/../../../input")
        if(self.is_flag("//span[text()='Окружность головы, см']/../../../input")):
            self.insData('20',"//span[text()='Окружность головы, см']/../../../input")
        
        self.click("//p[text()='Вес']/../div//mat-radio-button")
        self.click("//p[text()='Рост']/../div//mat-radio-button")
        
        self.checkLoading()
        
    def evaluationSex(self):
        
        if(self.is_flag("//mat-select[@ng-reflect-name='p']/div")):
            self.click("//mat-select[@ng-reflect-name='p']/div")
            self.click("//span[text()=' 0 ']/..")
        
        if(self.is_flag("//mat-select[@ng-reflect-name='ax']/div")):    
            self.click("//mat-select[@ng-reflect-name='ax']/div")
            self.click("//span[text()=' 0 ']/..")
        
        if(self.is_flag("//mat-select[@ng-reflect-name='ma']/div")):
            self.click("//mat-select[@ng-reflect-name='ma']/div")
            self.click("//span[text()=' 0 ']/..")

        if(self.is_flag("//mat-select[@ng-reflect-name='me']/div")):    
            self.click("//mat-select[@ng-reflect-name='me']/div")
            self.click("//span[text()=' 0 ']/..")
        
        if(self.is_flag("//mat-select[@ng-reflect-name='fa']/div")):    
            self.click("//mat-select[@ng-reflect-name='fa']/div")
            self.click("//span[text()=' 0 ']/..")


        if(self.is_flag("//span[text()=' Отсутствует ']/..//input[@aria-checked='false']") and self.is_flag("//span[text()=' Отсутствует ']/../..")):
                self.click("//span[text()=' Отсутствует ']/../..")

    def insFormPsixRazDefold(self,arg):
        if(self.is_flag("//p[text()=' Оценка психического развития для детей 0-4 лет ' ]")):
            self.insData(arg,"//span[text()='Познавательная функция (возраст развития)']/../../../input")
            self.insData(arg,"//span[text()='Моторная функция (возраст развития)']/../../../input")
            self.insData(arg,"//span[text()='Предречевое и речевое развитие (возраст развития)']/../../../input")
            self.insData(arg,"//span[text()='Эмоциональная и социальная (контакт с окружающим миром) функции (возраст развития)']/../../../input")

    def save(self):
        self.checkLoading()
        self.click("//button[text()=' Сохранить ']")
        self.checkLoading()

    def nextForm(self,arg):
            self.save()
            self.checkLoading()
            self.click("//p[text()='"+arg+"']")
            self.checkLoading()