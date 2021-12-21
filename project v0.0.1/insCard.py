import sys
from selenium import webdriver
import ast
from time import clock_getres, sleep
from varname import nameof


browser = webdriver.Firefox(executable_path=r'/home/admins/Документы/project/geckodriver')

login = '+79922800580'
password = 'yz0_NX!4_'


class Data:

    def __init__(self):
        
        self.data = ast.literal_eval(open('dic.txt', 'r').read())

    def get(self):
        return self.data 
    
    def remove(self,item):
        self.data.remove(item)
        f = open("dic.txt","w")
        f.write( str(self.data) )
        f.close()

    def logGood(self,item):

        f = open("logGood.txt","a")
        f.write( str(item) )
        f.close()
        self.remove(item)

    def logError(self,item):
        f = open("logError.txt","a")
        f.write( str(item) )
        f.close()
        self.remove(item)

data = Data()

# Чесло ли?
def is_int(var):
    try:

        int(var)
        return True

    except:
        return False

#Есть ли flag ?
def is_flag(xPath):
    sleep(0.15)
    try:
        return browser.find_element_by_xpath(xPath)
    except:
        return False

#Загружен ли сайт полностью ?
def checkLoad(funcIn):

    def decorator(*arg):

        while True:
            if (is_flag("//mat-spinner[@class='mat-spinner mat-progress-spinner spinner mat-primary mat-progress-spinner-indeterminate-animation ng-star-inserted']")):
                continue

            state = browser.execute_script('return document.readyState')
            if (not  state == "complete"):
                
                sleep(0.1)
                continue
            else:
                return funcIn(*arg)            
                 

    return decorator

#Проверка наличия элемента ? Если нет, значит Error
def examinationElement(funcIn):

    def decorator(*arg):

        stop = 50
        while True:
            try:
                return funcIn(*arg) 

            except:

                if (not stop):
                    print('decorator({})'.format(arg[0]),)
                    raise ValueError('No find '+arg[0])

                stop-=1 
                sleep(0.1)
        
    return decorator

@checkLoad
def existCard():
    if (is_flag("//MAT-ICON[@class='mat-icon notranslate fio_report_icon material-icons mat-icon-no-color']")\
            or is_flag("//DIV[text()=' Возможно, данный пациент уже существует в системе ']")\
                or is_flag("//DIV[text()=' Пациент уже существует ']")):
                   
        return True
    else:
        return False
            
@checkLoad
@examinationElement
def is_element(xPath):
    return browser.find_element_by_xpath(xPath)

@checkLoad
@examinationElement
def insData(data,xpath):
    inp = browser.find_element_by_xpath(xpath)
    inp.clear()
    inp.send_keys(data)

@checkLoad
@examinationElement
def click(xpath):
    
    button =  browser.find_element_by_xpath(xpath)
    button.click()
    sleep(0.2)
    return True
    
@checkLoad
def getURL(url):
    browser.get(url)



#Вход rosminzdrav
getURL('https://orph.egisz.rosminzdrav.ru/')
click("//A[text()='Войти']")
insData(login,"//INPUT[@id='login']")
insData(password,"//INPUT[@id='password']")
click("//BUTTON[@id='loginByPwdButton']")
sleep(3)




#Цыкл по данным... Insert data ...
iEnd = len (data.get().copy()) 
for i, children in enumerate(data.get().copy()):
    

    try:
        if (not children['docSer'] or not children['docSer']):
            raise ValueError('No find docSer, docSer')
            
        print('go {}/{}'.format(i,iEnd))

        getURL('https://orph.egisz.rosminzdrav.ru/patient-card')
  

        if children['sex'] == '2':
                click("//SPAN[text()='Мужской']/../../..")
                click("//span[text()='Женский']/..")
        
       


        if(is_element("//mat-label[text()=' Фамилия ']")):
            insData(children['F'],"//INPUT[@id='mat-input-2']")




        if(is_element("//mat-label[text()=' Имя ']")):
            insData(children['I'],"//INPUT[@id='mat-input-3']")



        if(is_element("//mat-label[text()=' Отчество ']")):
            if (children['O']):
                insData(children['O'],"//INPUT[@id='mat-input-4']")

        dr = children['dr'].split('-')

        if(is_element("//mat-label[text()=' Дата рождения ']")):

                insData('{}{}{}'.format(dr[2],dr[1],dr[0]),'//INPUT[@id="mat-input-0"]')

        if children['snils'] :
            
            if(is_element("//mat-label[text()=' СНИЛС ']")):
                insData(children['snils'],"//INPUT[@id='mat-input-5']")
                
        else:

            click("//input[@id='mat-checkbox-1-input']/../..")
            click("//mat-label[text()='Причина отсутствия СНИЛС ']/../../../..")
            click("//span[text()='Другое']/..")

            if(is_element("//mat-label[text()=' Введите причину отсутствия СНИЛС ']")):
                insData('-',"//INPUT[@id='mat-input-6']")



        

        # Проверка на существования карты...
        if(existCard()):
            data.logGood(children)
            continue

        
        # открыть модальное окно для ввода карты ...
        click("//MAT-ICON[text()='add']/..")

        #Если паспорт ... если св. о рожд.
        if is_int(children['docSer'].replace(' ','')):

            insData(children['docSer'].replace(' ',''),"//INPUT[@id='mat-input-6']")  
            insData(children['docNum'],"//INPUT[@id='num_doc']")
        
        else:        
            
            click("//span[text() = '21 - Паспорт гражданина РФ']/../../..")
            
            if (children['docSer'] == 'AA' or children['docSer'] == '1АЛ'or children['docSer'] == 'АА'\
                or children['docSer'] == 'FS' or children['docSer'] == 'КР-Х' or children['docSer'] == 'AC'):
                click("//span[text()='91 - Иные документы']/..")
            else :
                click("//span[text()='03 - Свидетельство о рождении']/..")
            
            if(is_element("//mat-label[text()='Серия документа ']")):
                insData(children['docSer'],"//mat-label[text()='Серия документа ']/../../../input")
            
            if(is_element("//mat-label[text()='Номер документа ']")):
                insData(children['docNum'],"//mat-label[text()='Номер документа ']/../../../input")

# Проверка на существования карты...
        if(existCard()):
            data.logGood(children)
            continue

        # 5 сикунд на ввод даных..    
        click("//BUTTON[text()='Добавить']")

        #if (is_flag("//BUTTON[@disabled=''][text()='Добавить']")):
        #        insData('1'+children['docSer'],"//INPUT[@id='mat-input-7']")
        #        click("//BUTTON[text()='Добавить']")
        
        
        click("//span[text()='Сохранить']/..")


        #Холостое нажатия ...
        click("//div[text()=' Карты осмотра ']/div/mat-icon[text()='add']")
        data.logGood(children)
    except  Exception:
        e = sys.exc_info()[1]
        children['err']=e.args[0]
        data.logError(children)
        
        
        
        
        
        

