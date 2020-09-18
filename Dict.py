import json
import csv
import sys
import operator

PATH_INPUT_SURFACE_NAMES = '/wikipedia/output2020/sv/surface_names.csv'
reader = csv.reader(open(PATH_INPUT_SURFACE_NAMES), delimiter=",")

def gen_reader():
    for row in reader:
        yield row

index = 0
Dict = {}

with open('Dict_ru.json','r') as file:
    Dict = json.load(file)
    file.close()

for row in gen_reader():
    index += 1
    if index<=40000000:
        continue
    else:
        print(index/54237541)
        try:
            Name = row[2]
        except IndexError:
            continue
        try:
            surfaceName = row[3]
        except IndexError:
            continue

        if Name not in Dict:
            Dict[Name] = {}
            Dict[Name][surfaceName]=1
        else:
            if surfaceName not in Dict[Name]:
                Dict[Name][surfaceName]=1
            else:
                Dict[Name][surfaceName]+=1

        if(index%10000000==0):
            with open('Dict_sv.json','w') as file:
                json.dump(Dict, file)
                file.close()
with open('Dict_sv.json','w') as file:
    json.dump(Dict, file)
    file.close()
