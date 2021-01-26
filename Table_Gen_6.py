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
        
with open('../input/visualization-2/Edit-Distance.json','r') as file:
    ED = json.load(file)
    file.close()

with open('../input/visualization-2/Wrong_Surface_Names.json','r') as file:
    Wrong_Surface_Names = json.load(file)
    file.close()

with open('../input/visualization-2/Correct_Surface_Names.json','r') as file:
    Correct_Surface_Names = json.load(file)
    file.close()

with open('../input/visualization-2/Substrings.json','r') as file:
    Substrings = json.load(file)
    file.close()

with open('../input/visualization-2/Superstrings.json','r') as file:
    Superstrings = json.load(file)
    file.close()

with open('SN_Dict.json','r') as file:
    SN_Dict = json.load(file)
    file.close()

with open('Entity_Dict.json','r') as file:
    Entity_Dict = json.load(file)
    file.close()

mid = 0
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

    line = ""
    mid+=1
    line+=str(mid)
    line+=","
    line+=str(Entity_Dict[source])
    line+=","
    line+=str(Entity_Dict[destination])
    line+="," 
    line+=str(SN_Dict[surface_name])
    line+=","
    line+=str(sid)
    line+=","
    
   try:
      if destination in Correct_Surface_Names:
          if surface_name in Correct_Surface_Names[destination]:
              line+="Correct"
          else:
              line+="Wrong,"
              line+=str(Edit_Distances[destination][surface_name][1])
              line+=","
              line+=str(SN_Dict[Edit_Distances[destination][surface_name][0]])
              line+=","
              if surface_name in Superstrings[destination]:
                  line+="1,"
                  line+=str(SN_Dict[Superstrings[destination][surface_name]])
                  line+=","
              else:
                  line+="0,"
              if surface_name in Substrings[destination]:
                  line+="1,"
                  line+=str(SN_Dict[Substrings[destination][surface_name]])
                  line+=","
              else:
                  line+="0,"
      else:
          line+="Lesser-than-3-surface-names"   
