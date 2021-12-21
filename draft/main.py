from types import coroutine
import aiohttp
import asyncio

import pandas as pd
import numpy as np

import json
from lxml import html
from pandas.core.indexes.api import all_indexes_same

from varname import nameof
from varname.core import varname

from time import time, sleep




async def getData(url, session):
    
    async with session.get(url) as response:
        
        try:
            resText = await response.text()

            tree = html.fromstring(resText)
            obj1 = json.loads( \
                        tree.xpath("//head/script[@type='application/ld+json']")[0].text\
                    )

            obj2 = json.loads( \
                tree.xpath("//script[@id='initial-state']")[0].text\
            )    



            Владельцы = tree.xpath("//li[@class = 'CardInfoRow CardInfoRow_ownersCount']/span")[1].text
            ПТС = tree.xpath("//li[@class='CardInfoRow CardInfoRow_pts']/span")[1].text
            Привод = tree.xpath("//li[@class='CardInfoRow CardInfoRow_drive']/span")[1].text
            Руль = tree.xpath("//li[@class='CardInfoRow CardInfoRow_wheel']/span")[1].text
            Состояние  = tree.xpath("//li[@class='CardInfoRow CardInfoRow_state']/span")[1].text
            Таможня  = tree.xpath("//li[@class='CardInfoRow CardInfoRow_customs']/span")[1].text

            return await getObjects(obj1,obj2,[Владельцы,ПТС,Привод,Руль,Состояние,Таможня],url)
        except:
            return await getObjects({},{},[],url)

async def getObjects(obj1,obj2,arrArgum,url):

    if len(arrArgum) == 0 :
        return ['error']

    if not 'price' in obj1['offers']:
        
        return ['price']

    bodyType = obj1['bodyType']
    brand = obj1['brand']
    car_url = url
    color = obj1['color']
    complectation_dict = obj2['card']['vehicle_info']['complectation']
    description = obj1['description']
    engineDisplacement = obj1['vehicleEngine']['engineDisplacement']
    enginePower = obj1['vehicleEngine']['enginePower'] 
    equipment_dict = obj2['card']['vehicle_info']['equipment']
    fuelType = obj1['fuelType']
    image = obj1['image']
    mileage = obj2['card']['state']['mileage']
    modelDate = obj1['modelDate']
    model_info = obj2['card']['vehicle_info']['model_info']
    model_name =obj2['card']['vehicle_info']['model_info']['code']
    name = obj2['card']['vehicle_info']['tech_param']['human_name']
    numberOfDoors = obj1['numberOfDoors']
    parsing_unixtime = int(time())
    priceCurrency = obj1['offers']['priceCurrency']
    productionDate = obj1['productionDate']
    sell_id = 0
    super_gen = obj2['card']['vehicle_info']['tech_param']
    vehicleConfiguration = obj1['vehicleConfiguration']
    vehicleTransmission = obj1['vehicleTransmission']
    vendor = obj2['card']['vehicle_info']['vendor']
    Владельцы = arrArgum[0]
    Владение = 0# Нет инфы
    ПТС = arrArgum[1]
    Привод = arrArgum[2]
    Руль = arrArgum[3]
    Состояние  = arrArgum[4]
    Таможня  = arrArgum[5]
    price = obj1['offers']['price']

    arrData = [bodyType, brand, car_url, color, complectation_dict,
           description, engineDisplacement, enginePower, str(equipment_dict),
           fuelType, image, mileage, modelDate, model_info, model_name,
           name, numberOfDoors, parsing_unixtime, priceCurrency,
           productionDate, sell_id, super_gen, vehicleConfiguration,
           vehicleTransmission, vendor, Владельцы, Владение, ПТС,
           Привод, Руль, Состояние, Таможня,price]

    return(arrData)
    

async def main(arrUrl):

    
    connector = aiohttp.TCPConnector(force_close=True)
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=86400),connector = connector) as session:
        
        tasks=[]

        for url in arrUrl:
            
            coroutin = getData(url,session)

            tasks.append(asyncio.create_task(coroutin))
        
        return await asyncio.gather(*tasks)
        
if __name__ == "__main__":

    urlFullCar = pd.read_csv('urlFullCar.csv')['0']
    urlIfCar = pd.read_csv('urlIfCar_.csv')['0']


    for i in range(1,int(len(urlIfCar)/5000)+2):
        sleep(60)
        if (i < int(len(urlIfCar))/5000) :
            pushArr = urlIfCar[5000*(i-1):5000*i]
        else:
            pushArr = urlIfCar[5000*(i-1):len(urlIfCar)]
        
        coroutin = main(pushArr)


        t0 = time()
        data = (asyncio.run(coroutin))
        
        pd.DataFrame((np.array(data)))\
                        .to_csv('train_if_{}.csv'.format(i-1), encoding='utf-8')

        print(time()-t0)