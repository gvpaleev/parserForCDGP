from time import sleep
from selenium import webdriver
from Data import Data
import sys

from ProinspectionClass import Proinspection
from ChildsСardClass import ChildsCard
from ChildsCardFullClass import ChildsCardFull


data = Data('/home/admins/Документы/parserForCDGP/project v0.02/data/data.json')
browser = webdriver.Firefox(executable_path=r'./geckodriver')
childsCard = ChildsCard(browser)
childsCardFull = ChildsCardFull(browser)
inspection = Proinspection(browser)

childsCard.installHome()

iEnd = len (data.getChilds()) 
for i,child in enumerate(data.getChilds()):
    try:
        #if (saveJson['name']['last'] != 'СЕЛИВАНОВА'):
        #    continue

        print('go{}/{}'.format(i,iEnd))
    
        
        if(int(child['dateOfBirth'].split('-')[0])>2018):
            saveJson = child.copy()
            saveJson['flags'] = 'age3'
            data.logGood(saveJson,child)

            continue

        childsCard.goHome()
        childsCard.insSexChild(child['idSex'])

        if ('snils' in child):
            if(child['snils']):
                childsCard.insSnilsChild(child['snils'])
            else:
                childsCard.insNotSnilsChild()   
        else:
            childsCard.insNotSnilsChild()        

        childsCard.insFirstChild(child['name']['first'])
        childsCard.insMiddleChild(child['name']['middle'])
        childsCard.insBirthChild(child['dateOfBirth'])

        if('last' in child['name']):
            childsCard.insLastChild(child['name']['last'])

        urlFullCard = childsCard.getCard()
        # Если есть карта то переходим ...
        if(urlFullCard):

            childsCardFull.goFullCard(urlFullCard)
            #sleep(3)# Не ловится условия !!!!!!
            if(not childsCardFull.is_inspection()):
                childsCardFull.addInspection()

                childsCardFull.dateObsled(child['cards']['card']['dateOfObsled'])

                childsCardFull.setAge(child['dateOfBirth'],child['cards']['card']['dateOfObsled'])
                
                #//button[text()='Создать ']
                childsCardFull.createInspection()
                flagCread = childsCardFull.is_creadInspection()

                if(not flagCread):
                    urlInspection = childsCardFull.sellectUrl()

                else:
                    saveJson = child.copy()
                    saveJson['flags'] = 'sozdanoDo'
                    data.logGood(saveJson,child)
                    continue

            else:
                    

                urlInspection = childsCardFull.getUrlInspection()

            inspection.goProinspection(urlInspection)
            inspection.insLocation()
            inspection.insOMS()
            inspection.insNumPolis(child['polisNum'])
            inspection.save()
        
            inspection.nextForm(' Оценка развития ')

            inspection.insHeight(child['cards']['card']['height'])
            inspection.insWeight(child['cards']['card']['weight'])
            if('headSize' in child['cards']['card']):
                inspection.insOkrGol(child['cards']['card']['headSize'])
            
            inspection.violations()
            if(2021 - int(child['dateOfBirth'].split('-')[0])>=10):

                inspection.evaluationSex()
            sleep(0.5)
            if (inspection.is_psixRaz()):
                age = 2021 - int(child['dateOfBirth'].split('-')[0])
                inspection.insFormPsixRazDefold(age)    
            inspection.save()

            inspection.nextForm(' Состояние здоровья ')


            inspection.insHealthGroupBefore(child['cards']['card']['healthGroupBefore'])
            inspection.insFizkultGroupBefore(child['cards']['card']['fizkultGroupBefore'])
            
            inspection.clearDiagnos()

            if ('diagnosisBefore' in child['cards']['card'] and child['cards']['card']['diagnosisBefore']):
                diagnosBefore = child['cards']['card']['diagnosisBefore']
            
                

                if ( type(diagnosBefore['diagnosis']) == type(list()) ):
                    for  item in diagnosBefore['diagnosis']:
                        inspection.addDiagBefore()
                        
                        inspection.insDiagBef(item)
                else:
                    inspection.addDiagBefore()
                    inspection.insDiagBef(diagnosBefore['diagnosis'])
                #inspection.save()
            if ('diagnosisAfter' in child['cards']['card'] and child['cards']['card']['diagnosisAfter']) :
                diagnosisAfter = child['cards']['card']['diagnosisAfter']

                if ( type(diagnosisAfter['diagnosis']) == type(list()) ):
                    for  item in diagnosisAfter['diagnosis']:
                        inspection.addDiagAfter()
                        
                        inspection.insDiagAft(item)
                else:
                    inspection.addDiagAfter()
                        
                    inspection.insDiagAft(diagnosisAfter['diagnosis'])

            inspection.save()

            inspection.nextForm(' Исследования ')
            if('issled' in child['cards']['card']):
                if(child['cards']['card']['issled'] and child['cards']['card']['issled']['basic']):
                    dateIssled=child['cards']['card']['issled']['basic']['record'][0]['date']

                    inspection.insFormIsskedDefaut(dateIssled)
                    
            sleep(0.2)
            inspection.save()
            inspection.nextForm(' Заключение ')

            inspection.insHealthGroup(child['cards']['card']['healthGroup'])
            inspection.insFizkultGroup(child['cards']['card']['fizkultGroupBefore'])
            

            inspection.insZakName(child['cards']['card']['zakluchVrachName']['last'])

            inspection.insDateZakl(child['cards']['card']['zakluchDate'])

            inspection.insRecomend()

            inspection.save()

            inspection.perform()

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
            


print('end')