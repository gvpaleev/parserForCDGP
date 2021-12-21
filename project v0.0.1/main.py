
import aiohttp
import asyncio
import ast

f = open('dic.txt', 'r')
dic = f.read()
data = ast.literal_eval(dic)
#CONST
url = 'https://orph.egisz.rosminzdrav.ru'


async def main(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            try:    
                text = await response.read()
                print(text)

            except:
                print('err')
        
if __name__ == "__main__":

    coroutin = main(url)
    asyncio.run(coroutin)