
from Browser import Browser
from Data import Data

data = Data('/home/admins/Документы/parserForCDGP/project v0.02/data/data.json')

firefox = Browser('./geckodriver')

for child in data.getChilds():
    

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
        pass
    else:
        print ('ss')
        pass

print('end')