import json
import csv
import sys
import operator
from collections import OrderedDict

PATH_INPUT_SURFACE_NAMES = '/wikipedia/output2020/en/fake/surface_names.csv'
reader = csv.reader(open(PATH_INPUT_SURFACE_NAMES), delimiter=",")

def gen_reader():
    for row in reader:
        yield row

sn_index = 0
entity_index = 0
SN_Dict = OrderedDict()
Entity_Dict = OrderedDict()

# with open('Dict_en.json','r') as file:
#    Dict = json.load(file)
#    file.close()

for row in gen_reader():
    try:
        Source = row[1]
    except IndexError:
        continue
    try:
        Dest = row[2]
    except IndexError:
        continue
    try:
        surfaceName = row[3]
    except IndexError:
        continue

    if Source not in Entity_Dict:
        entity_index += 1
        Entity_Dict[Source] = entity_index
    
    if Dest not in Entity_Dict:
        entity_index += 1
        Entity_Dict[Dest] = entity_index
    
    if surfaceName not in SN_Dict:
        sn_index+=1
        SN_Dict[surfaceName] = sn_index
    
with open('SN_Dict.json','w') as file:
    json.dump(SN_Dict, file)
    file.close()

with open('Entity_Dict.json','w') as file:
    json.dump(Entity_Dict, file)
    file.close()
