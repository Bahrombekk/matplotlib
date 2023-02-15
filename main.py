import json
file_path = "data.json"
f=open(file_path)
data_str=f.read()
data=json.loads(data_str)
values=data.values()
a=data.get('a', 0)
b=data.get('b',0)
n={
    "sum":a+b
} 
adf=json.dumps(n, indent=4)
f1=open("result.json", "w")
f1=f1.write(adf)
# test

