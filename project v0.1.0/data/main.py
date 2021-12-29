import xmltodict, json


file = open("./data/data.json","w")\
        .write(json.dumps(\
                xmltodict.parse(open('./data/data.xml').read())\
            ,ensure_ascii=False)
        )


with open('./data/data.json') as file:
            data = json.load(file)

with open('./data/dataGood.json') as file:
            dataGood = json.load(file)

dataArr = data['children']['child'].copy()

dataGoodArr = dataGood['children']['child']

iEnd = len(dataGoodArr)

for i,itemDataGood in enumerate(dataGoodArr):

    print ( 'start {}/{}'.format(i,iEnd))


    last=itemDataGood['name']['last']
    first = itemDataGood['name']['first']
    middle = itemDataGood['name']['middle']
    dateOfBirth = itemDataGood['dateOfBirth']

    for itemData in dataArr:
        flag=True

        if( itemData['name']['last'] != last):
            continue
        if( itemData['name']['first'] !=first ):
            continue
        if(itemData['name']['middle']!= middle):
            continue
        if(itemData['dateOfBirth'] != dateOfBirth):
            continue
        
        dataArr.remove(itemData)
        break
        
data['children']['child'] = dataArr

f = open("./data/data.json","w")
f.write(json.dumps(data,ensure_ascii=False))
f.close()