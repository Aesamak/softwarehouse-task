import json

with open("flights-1m.json", "r" ,encoding="utf-8") as b:
    data = json.load(b)

keys = list(data[0].keys())

with open("sample_data4.csv", "a") as b:
   
    b.write(",".join(keys) + "\n")

    for da in data:
        b.write(",".join(str(da[key]) for key in keys) + "\n")
