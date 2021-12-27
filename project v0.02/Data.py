import json
from os import error

class Data():
    def __init__(self,path):

        with open(path) as file:
            self.data = json.load(file)
            

    def getChilds(self):
        return self.data['children']['child'].copy()
    
    
    def remove(self,item):
        self.data['children']['child'].remove(item)
        
        file = open("project v0.02/data/data.json","w")\
        
        file.write(json.dumps(self.data,ensure_ascii=False))
        file.close()
        pass

    def logGood(self,item,itemRemove):
        f = open("logGood.json","a")
        f.write(json.dumps(item,ensure_ascii=False))
        f.close()
        self.remove(itemRemove)
        pass

    def logError(self,item,itemRemove):
        #f = open("logError.json","a")
        #f.write( json.dumps(item,ensure_ascii=False) )
        #f.close()
        #self.remove(itemRemove)
        pass