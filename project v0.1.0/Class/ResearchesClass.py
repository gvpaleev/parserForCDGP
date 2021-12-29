from Class.GlobalMethodClass import GlobalMethodClass


class Researches(GlobalMethodClass):
    def __init__(self,browser):
        self.browser = browser
        pass

    def insFormIsskedDefaut(self,date):
        date = date.split('-')
        if(self.is_flag("//p[text()='Общий анализ крови']/../..//mat-label[text()=' Введите дату ']/../../../input")):
            self.insData(date[2]+date[1]+date[0],"//p[text()='Общий анализ крови']/../..//mat-label[text()=' Введите дату ']/../../../input")
            self.insData('Норма',"//p[text()='Общий анализ крови']/../..//span[text()='Результат']/../../..//textarea")
        
        if(self.is_flag("//p[text()='Общий анализ мочи']/../..//mat-label[text()=' Введите дату ']/../../../input")):
            self.insData(date[2]+date[1]+date[0],"//p[text()='Общий анализ мочи']/../..//mat-label[text()=' Введите дату ']/../../../input")
            self.insData('Норма',"//p[text()='Общий анализ мочи']/../..//span[text()='Результат']/../../..//textarea")

        if(self.is_flag("//p[text()='Электрокардиография']/../..//mat-label[text()=' Введите дату ']/../../../input")):
            self.insData(date[2]+date[1]+date[0],"//p[text()='Электрокардиография']/../..//mat-label[text()=' Введите дату ']/../../../input")
            self.insData('Норма',"//p[text()='Электрокардиография']/../..//span[text()='Результат']/../../..//textarea")

    def save(self):
        self.checkLoading()
        self.click("//button[text()=' Сохранить ']")
        self.checkLoading()

    def nextForm(self,arg):
            self.save()
            self.checkLoading()
            self.click("//p[text()='"+arg+"']")
            self.checkLoading()
