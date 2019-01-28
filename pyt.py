import random
import configparser
import json
import re

config = configparser.ConfigParser()
config.read('pybot.ini')

pokemon_file = 'pokemon.json'
json_data = {}

wish_list = 'wish.json'
wish_data = {}

TOKEN = config['dnd']['token']

description = '''ninjaBot in Python'''
#bot = commands.Bot(command_prefix='?', description=description)

def r(die : str):
    (num,dice) = die.split("d")
    print(num)
    print(dice)
    for i in range(int(num)):
        result = random.randint(1, int(dice))
        print("You rolled a: " + str(result))

def roll(die : int):
    result = random.randint(1, die)
    print("You rolled a: " + str(result))
#bot.run(TOKEN)
def load_pokemon():
    with open(pokemon_file, 'r') as f:
        json_data = json.load(f)
        for p in json_data:
            if (search('un', p['name'])):
                print(p['name'])

def search(search : str, pokemon : str):
    if search.lower() in pokemon.lower():
        return True
    else:
        return False

def read_file(file_name : str):
    with open(file_name, 'r') as input_file:
        file_data = json.load(input_file)
    return file_data

def add(item : str, what : str):
    wish_data = read_file(wish_list)
    if not item in wish_data:
        print("Not found: " + item)
        wish_data[item] = {}
    data = {'name': what}
    if not 'want' in wish_data[item]:
        print("Not in list: ")
        wish_data[item]['want'] = []
    item_present = False
    for wish_item in wish_data[item]['want']:
        print(wish_item)
        if what in wish_item['name']:
           item_present = True
           print("Found: " + what)
        else:
           print("Not present: " + what)
    if not (item_present):
       wish_data[item]['want'].append(dict(name=what)) 
       print("Adding to wishlist: " + what)

    with open(wish_list, 'w') as outfile:
        json.dump(wish_data, outfile)        

def show(who):
    item_data = read_file(wish_list)
    print(item_data)
    for item in item_data[who]['want']:
        print('Want:' + item['name'])

### Testing Area
who = "kal"
what = ['squirtle', 'dialga', 'shuckle']
for item in what:
    add(who, item)
show(who)
#roll(20)
#r("3d6")
#load_pokemon()

