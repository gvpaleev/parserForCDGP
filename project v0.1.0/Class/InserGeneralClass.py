from Class.GlobalMethodClass import GlobalMethodClass


class InsertGeneral(GlobalMethodClass):
    def __init__(self,browser) :
        self.browser=browser
        pass

    def goProinspection(self,url):
        self.getURL(url)
        self.checkLoading()

    def insDefuld(self):
        
        self.insData('Череповец',"//mat-label[text()='Место постоянного пребывания']/../../../input")
        self.click("//mat-option[@title='Вологодская Область, г. Череповец']")
        self.insData('35003',"//mat-label[text()='Страховая медицинская организация']/../../../input")
        self.click("""//mat-option[@title='35003 - ВОЛОГОДСКИЙ ФИЛИАЛ АКЦИОНЕРНОГО ОБЩЕСТВА "СТРАХОВАЯ КОМПАНИЯ "СОГАЗ-МЕД" - Вологодская область']""")

    def insNumPolis(self,arg):
        self.insData(arg,"//span[text()='Номер полиса']/../../../input")
    
    def save(self):
        self.checkLoading()
        self.click("//button[text()=' Сохранить ']")
        self.checkLoading()

    def nextForm(self,arg):
            self.save()
            self.checkLoading()
            self.click("//p[text()='"+arg+"']")
            self.checkLoading()