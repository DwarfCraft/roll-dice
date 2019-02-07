import json
import os
import random

data_file = 'npc.json' 

with open(data_file, 'r') as f:
    json_data = json.load(f)
    for key in json_data.keys():
        print (random.choice(json_data[key]))


