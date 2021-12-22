
from typing import Counter
from Browser import Browser
from Data import Data

data = Data('/home/admins/Документы/parserForCDGP/project v0.02/data/data.json')

firefox = Browser('./geckodriver')

for child in data.getChilds():
    
    if(int(child['dateOfBirth'].split('-')[0])>2018):
        continue
    firefox.home()

    firefox.sexChild(child['idSex'])

    if ('snils' in child):
        firefox.snilsChild(child['snils'])
    else:
        firefox.notSnilsChild()
        

    firefox.firstChild(child['name']['first'])

    firefox.middleChild(child['name']['middle'])

    firefox.birthChild(child['dateOfBirth'])

    if('last' in child['name']):
        firefox.lastChild(child['name']['last'])

    if(firefox.getCard()):

        firefox.cliclCard()

        

        firefox.addInspection()

        firefox.dateObsled(child['cards']['card']['dateOfObsled'])

        firefox.setAge(child['dateOfBirth'],child['cards']['card']['dateOfObsled'])
        
        firefox.create()
        print ('1')
    else:
        print ('ss')

print('end')