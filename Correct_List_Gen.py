import json
# import matplotlib.pyplot as plt
import os

with open("Dict_sv.json","r") as file:
    data = json.load(file)
    file.close()

Correct_List = {}
i = 0
j = len(data)

for key,val in data.items():
    i+=1
    print(i/j)
    if(len(val)>1):
        Correct_List[key]={}
        count = 0

        for k,v in val.items():
            count+=v
        for k,v in val.items():
            if(v/count>=0.05):
                Correct_List[key][k] = (v,v/count)
print(len(Correct_List))

with open("Correct_List_gr1.json","w") as file:
    json.dump(Correct_List, file)
    file.close()
