from time import time, sleep
import asyncio 
import aiohttp

import requests
import json
from lxml import html

import pandas as pd
import numpy as np

import asyncio

from requests.api import get 



urlFullCar = pd.read_csv('urlFullCar.csv')['0']
urlIfCar = pd.read_csv('urlIfCar_.csv')['0']

print(len(urlFullCar))
print(len(urlIfCar))

async def get_date(url,session):
    obj1, obj2 , arr = await get_contens(url,session)

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
    Владельцы = arr[0]
    Владение = 0# Нет инфы
    ПТС = arr[1]
    Привод = arr[2]
    Руль = arr[3]
    Состояние  = arr[4]
    Таможня  = arr[5]
    price = obj1['offers']['price']

    timArr = [bodyType, brand, car_url, color, complectation_dict,
           description, engineDisplacement, enginePower, str(equipment_dict),
           fuelType, image, mileage, modelDate, model_info, model_name,
           name, numberOfDoors, parsing_unixtime, priceCurrency,
           productionDate, sell_id, super_gen, vehicleConfiguration,
           vehicleTransmission, vendor, Владельцы, Владение, ПТС,
           Привод, Руль, Состояние, Таможня,price]

    return(timArr)



async def get_contens(url,session):
    
    await asyncio.sleep(0.1)
    




async def main(urlArr):
    
    dataArr = []

    tasks = []

    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=1)) as session:
        for url in urlArr:

            try:
                task = asyncio.create_task(get_date(url,session))
                tasks.append(task)
            except:
                print("Опа! Неожиданная ошибка!")

        print('stop for!')
        pd.DataFrame((np.array(await asyncio.gather(*tasks))))\
                    .to_csv('train.csv', encoding='utf-8')





if __name__ == '__main__':
    t0 = time()
    asyncio.run(main(urlIfCar))
    print(time()-t0)

