import json
from os import error

class Data():
    def __init__(self,path):
        self.path= path
        with open(path+'/data.json') as file:
            self.data = json.load(file)
        
        self.buffGood =''
        self.buffError = ''
            
    def saveBuff(self,flagLen=100000):
        flagSaveData = False
        if(len(self.buffGood)>flagLen):
            f = open(self.path+"/logGood.json","a")
            f.write(self.buffGood)
            f.close()
            self.buffGood=''
            flagSaveData=True

        if(len(self.buffError)>flagLen):
            f = open(self.path+"/logError.json","a")
            f.write(self.buffError)
            f.close()
            self.buffError = ''
            flagSaveData=True

        if (flagSaveData):
            file = open(self.path+'/data.json',"w")\
            
            file.write(json.dumps(self.data,ensure_ascii=False))
            file.close()

    def getChilds(self):
        return self.data['children']['child'].copy()
    
    
    def remove(self,item):
        self.data['children']['child'].remove(item)
        
        
        pass

    def logGood(self,item,itemRemove):
        
        self.buffGood += json.dumps(item,ensure_ascii=False)
        self.remove(itemRemove)
        self.saveBuff()
        
        pass

    def logError(self,item,itemRemove):
        self.buffError+= json.dumps(item,ensure_ascii=False)
        self.remove(itemRemove)
        self.saveBuff()