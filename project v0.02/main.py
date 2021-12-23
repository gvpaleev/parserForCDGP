from time import sleep
from selenium import webdriver
from Data import Data

from ProinspectionClass import Proinspection
from ChildsСardClass import ChildsCard
from ChildsCardFullClass import ChildsCardFull


data = Data('/home/admins/Документы/parserForCDGP/project v0.02/data/data.json')
browser = webdriver.Firefox(executable_path=r'./geckodriver')
childsCard = ChildsCard(browser)
childsCardFull = ChildsCardFull(browser)
inspection = Proinspection(browser)

childsCard.installHome()

for child in data.getChilds():
    if (not child['name']['last'] == 'МИХАЙЛОВА'):
        continue
    
    if(int(child['dateOfBirth'].split('-')[0])>2018):
        continue

    childsCard.goHome()
    childsCard.insSexChild(child['idSex'])

    if ('snils' in child):
        childsCard.insSnilsChild(child['snils'])
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
        
        inspection.violations()
        if(2021 - int(child['dateOfBirth'].split('-')[0])>=10):

            inspection.evaluationSex()
        inspection.save()

        #inspection.nextForm(' Состояние здоровья ')


        #inspection.insHealthGroupBefore(child['cards']['card']['healthGroupBefore'])
        #inspection.insFizkultGroupBefore(child['cards']['card']['fizkultGroupBefore'])
        
        #if ('diagnosisBefore' in child['cards']['card']):
        #    diagnosBefore = child['cards']['card']['diagnosisBefore']
        #
        #    inspection.addDiagBefore()
        #    inspection.insDiagBef(diagnosBefore['diagnosis']['mkb'])
        #    inspection.save()
        

        inspection.nextForm(' Исследования ')
        
        dateIssled=child['cards']['card']['issled']['basic']['record'][0]['date']

        inspection.insFormIsskedDefaut(dateIssled)

        inspection.save()
        inspection.nextForm(' Заключение ')
        print('end')

    else:
        print ('Нет карты')

print('end')