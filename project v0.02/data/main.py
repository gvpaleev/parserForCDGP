import xmltodict, json


file = open("project v0.02/data/data.json","w")\
        .write(json.dumps(\
                xmltodict.parse(open('project v0.02/data/data.xml').read())\
            ,ensure_ascii=False)
        )

