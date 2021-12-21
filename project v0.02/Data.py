import json

class Data():
    def __init__(self,path):

        with open(path) as file:
            self.data = json.load(file)

    def getChilds(self):
        return self.data['children']['child']
        