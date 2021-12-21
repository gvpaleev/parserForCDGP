from lxml import etree
from varname import nameof


xmlFile = '/home/admins/Документы/project/data/DISP_LIST.xml'
xmlFileErr = '/home/admins/Документы/project/data/DISP_LIST_ERR.xml'
data = []

def  getData(element):
    if element is None:
        return False
    else:
        return element.text

for file in [xmlFile,xmlFileErr]:

    root = etree.parse(file)
    childrens = root.xpath('//child')

    for children in childrens:
        

        name = children.find("name")

        F = getData (name.find("last"))
        I = getData (name.find("first"))
        O = getData (name.find("middle"))
        
        dr = getData (children.find("dateOfBirth"))

        sex = getData (children.find("idSex"))

        docSer = getData (children.find('documentSer'))

        docNum = getData (children.find('documentNum'))

        snils = getData (children.find('snils'))

        polisNum = getData (children.find('polisNum'))

        cardsArr =[]
        if (int(dr.split('-')[0])<= 2018):

            cards = children.findall('cards/card')

            for card in cards:
        
                dateOfObsled = getData (card.find('dateOfObsled'))

                height = getData (card.find('height'))
                weight = getData(card.find('weight'))

                healthGroupBefore = getData(card.find('healthGroupBefore'))
                fizkultGroupBefore = getData(card.find('fizkultGroupBefore'))
                healthGroup = getData(card.find('healthGroup'))
                fizkultGroup = getData(card.find('fizkultGroup'))
                zakluchDate = getData(card.find('zakluchDate'))
                
                zakluchVrachName = card.find('zakluchVrachName')
                
                zakluchVrachName = {
                    "F":getData(zakluchVrachName.find('last')),
                    "I":getData(zakluchVrachName.find('first')),
                    "O":getData(zakluchVrachName.find('middle'))
                }

                diagnosisBefore = card.find('diagnosisBefore')
                if(diagnosisBefore):
                    timArr = []
                    for item in diagnosisBefore.findall('diagnosis'):

                        mkb = getData(item.find('mkb'))
                        dispNablud = getData(item.find('dispNablud'))

                        timArr . append({
                            nameof(mkb):mkb,
                            nameof(dispNablud):dispNablud
                        })    

                    diagnosisBefore = timArr

                

                diagnosisAfter = card.find('diagnosisAfter')
                
                if(diagnosisAfter):
                    timArr =[]  
                    for item in diagnosisAfter.findall('diagnosis'):

                        mkb = getData(item.find('mkb'))
                        firstTime = getData(item.find('firstTime'))
                        dispNablud = getData(item.find('dispNablud'))
                        needVMP = getData(item.find('needVMP'))
                        needSMP = getData(item.find('needSMP'))
                        needSKL = getData(item.find('needSKL'))

                        timArr . append({
                            nameof(mkb):mkb,
                            nameof(firstTime):firstTime,
                            nameof(dispNablud):dispNablud,
                            nameof(needVMP):needVMP,
                            nameof(needSMP):needSMP,
                            nameof(needSKL):needSKL
                        })  
                    diagnosisAfter = timArr
                

                dataIssled = getData(card.find('issled/basic/record/date'))
                resultIssled = getData(card.find('issled/basic/record/result'))

        else:
            cardsArr = False
        


        data.append({
            nameof(F):F,
            nameof(I):I,
            nameof(O):O,
            nameof(dr):dr,
            nameof(sex):sex,
            nameof(docSer):docSer,
            nameof(docNum):docNum,
            nameof(snils):snils,
            nameof(cardsArr):cardsArr

        })


f = open("dic.txt","w")
f.write( str(data) )
f.close()