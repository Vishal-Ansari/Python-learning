import json

data='{"var1":"vishal","var2":56}'
print(data)
# print(data['var1'])     #it wont work

parsed=json.loads(data)
print(parsed)
print(parsed['var1'])

data2={
    "channel name":"vishal the programmer",
    "vehicles":['tractor','fortuner','swift','scooty','bike'],
    "property":['2houses','2shops'],
    "isbad": False
}

jscomp=json.dumps(data2)
print(jscomp)