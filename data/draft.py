import xmltodict, json

f =open('./data.xml')
f = f.read()
o = xmltodict.parse(f)
js = json.dumps(o) # '{"e": {"a": ["text", "text"]}}'
pass