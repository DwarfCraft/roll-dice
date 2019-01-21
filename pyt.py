import random
import configparser
import json

config = configparser.ConfigParser()
config.read('pybot.ini')

pokemon_file = 'pokemon.json'
json_data = {}
TOKEN = config['dnd']['token']

description = '''ninjaBot in Python'''
#bot = commands.Bot(command_prefix='?', description=description)

def add(left : int, right : int):
    """Adds two numbers together."""
    print(left + right)

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


roll(20)
load_pokemon()

