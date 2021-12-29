from selenium import webdriver
import sys


from Class.GlobalMethodClass import GlobalMethodClass
from Class.InserCardClass import InserCard
from Class.DataClass import Data
from Class.InsertOsmotrClass import InserOsmotr
from Class.InserGeneralClass import InsertGeneral
from Class.DevelopmentAssessmentClass import DevelopmentAssessment
from Class.StateHealthClass import StateHealth
from Class.ResearchesClass import Researches
from Class.ConclusionClass import Conclusion


class Main(GlobalMethodClass):
    def __init__(self):
        pass

        self.browser = webdriver.Firefox(executable_path='./geckodriver')

        self.login = '+79922800580'
        self.password = 'yz0_NX!4_'

        

    def main(self,pathData):
        data = Data(pathData)
        #self.browser.close()
        inserCard = InserCard(self.browser) 
        inserOsmotr = InserOsmotr(self.browser)
        insertGeneral = InsertGeneral(self.browser)
        developmentAssessment = DevelopmentAssessment(self.browser)
        stateHealth = StateHealth(self.browser)
        researches= Researches(self.browser)
        conclusion = Conclusion(self.browser)

        self.getURL('https://orph.egisz.rosminzdrav.ru/')
        self.click("//A[text()='Войти']")
        self.insData(self.login,"//INPUT[@id='login']")
        self.insData(self.password,"//INPUT[@id='password']")
        self.click("//BUTTON[@id='loginByPwdButton']")
        if(self.examinationElement("//a[text()=' ПАЛЕЕВ Г. В ']")):
            print('URL:https://orph.egisz.rosminzdrav.ru Ready')
        
        
        
        
        childs = data.getChilds()

        iEnd = len (childs) 

        for i,child in enumerate(childs):
            try:
                #if (saveJson['name']['last'] != 'СЕЛИВАНОВА'):
                #    continue

                print('go {}/{}'.format(i,iEnd))
            
                
                if(int(child['dateOfBirth'].split('-')[0])>2018):
                    saveJson = child.copy()
                    saveJson['flags'] = 'age3'
                    data.logGood(saveJson,child)

                    continue

                inserCard.goHome()
                inserCard.insSexChild(child['idSex'])

                if ('snils' in child):
                    if(child['snils']):
                        inserCard.insSnilsChild(child['snils'])
                    else:
                        inserCard.insNotSnilsChild()   
                else:
                    inserCard.insNotSnilsChild()        

                inserCard.insFirstChild(child['name']['first'])
                inserCard.insMiddleChild(child['name']['middle'])
                inserCard.insBirthChild(child['dateOfBirth'])

                if('last' in child['name']):
                    inserCard.insLastChild(child['name']['last'])

                urlFullCard = inserCard.getCard()
                # Если есть карта то переходим ...
                if(urlFullCard):

                    inserOsmotr.goFullCard(urlFullCard)

                    if(not inserOsmotr.is_inspection()):
                        inserOsmotr.addInspection()

                        inserOsmotr.dateObsled(child['cards']['card']['dateOfObsled'])

                        inserOsmotr.setAge(child['dateOfBirth'],child['cards']['card']['dateOfObsled'])
                        
                        #//button[text()='Создать ']
                        inserOsmotr.createInspection()
                        flagCread = inserOsmotr.is_creadInspection()

                        if(not flagCread):
                            urlInspection = inserOsmotr.sellectUrl()

                        else:
                            saveJson = child.copy()
                            saveJson['flags'] = 'sozdanoDo'
                            data.logGood(saveJson,child)
                            continue

                    else:
                            

                        urlInspection = inserOsmotr.getUrlInspection()

                    insertGeneral.goProinspection(urlInspection)
                    insertGeneral.insDefuld()
                    insertGeneral.insNumPolis(child['polisNum'])
                    
                
                    insertGeneral.nextForm(' Оценка развития ')

                    developmentAssessment.insHeightWeight(child['cards']['card']['height'],child['cards']['card']['weight'])
                    
                    if(2021 - int(child['dateOfBirth'].split('-')[0])>=10):
                        developmentAssessment.evaluationSex()


                    
                    age = 2021 - int(child['dateOfBirth'].split('-')[0])
                    developmentAssessment.insFormPsixRazDefold(age)    
                    

                    developmentAssessment.nextForm(' Состояние здоровья ')


                    stateHealth.insGroupsBefore(child['cards']['card']['healthGroupBefore'],child['cards']['card']['fizkultGroupBefore'])
                    
                    

                    if ('diagnosisBefore' in child['cards']['card'] and child['cards']['card']['diagnosisBefore']):
                        diagnosBefore = child['cards']['card']['diagnosisBefore']
                    
                        

                        if ( type(diagnosBefore['diagnosis']) == type(list()) ):
                            for  item in diagnosBefore['diagnosis']:
                                stateHealth.addDiagBefore(item)
                        else:
                            stateHealth.addDiagBefore(diagnosBefore['diagnosis'])
                        #inspection.save()


                    if ('diagnosisAfter' in child['cards']['card'] and child['cards']['card']['diagnosisAfter']) :
                        diagnosisAfter = child['cards']['card']['diagnosisAfter']

                        if ( type(diagnosisAfter['diagnosis']) == type(list()) ):
                            for  item in diagnosisAfter['diagnosis']:
                                stateHealth.addDiagAfter(item)
                        else:

                            stateHealth.addDiagAfter(diagnosisAfter['diagnosis'])


                    stateHealth.nextForm(' Исследования ')

                    if('issled' in child['cards']['card']):
                        if(child['cards']['card']['issled'] and child['cards']['card']['issled']['basic']):
                            dateIssled=child['cards']['card']['issled']['basic']['record'][0]['date']

                            researches.insFormIsskedDefaut(dateIssled)
                            
                    researches.nextForm(' Заключение ')

                    conclusion.insGroups(child['cards']['card']['healthGroup'],child['cards']['card']['fizkultGroupBefore'])
                   
                    

                    conclusion.insZakName(child['cards']['card']['zakluchVrachName']['last'])

                    conclusion.insDateZakl(child['cards']['card']['zakluchDate'])

                    conclusion.insRecomend()


                    conclusion.perform()

                    saveJson = child.copy()
                    saveJson['flags'] = 'good'
                    data.logGood(saveJson,child)
                    print('end')

                else:
                    saveJson = child.copy()
                    saveJson['flags'] = 'notCard'
                    data.logError(saveJson,child)
                    print ('Нет карты')

            except Exception:
                e = sys.exc_info()[1]
                        
                saveJson = child.copy()
                saveJson['flags'] = e.args[0]
                data.logError(saveJson,child)
                print (e.args[0])
            
            

        data.saveBuff(flagLen=0)
        print('end')
        
        
        
        
        
        
        
        
        self.browser.close()

