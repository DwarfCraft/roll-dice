import discord
from discord.ext import commands
import random
import configparser
import json
import time

config = configparser.ConfigParser()
config.read('pybot.ini')

pokemon_file = 'pokemon.json'
json_data = {}

TOKEN = config['dnd']['token']

description = '''ninjaBot in Python'''
bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def hello():
    """Says world"""
    await bot.say("world")


@bot.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await bot.say(left + right)

@bot.command()
async def roll(die : int):
    result = random.randint(1, die)
    await bot.say("You rolled a: " + str(result))

@bot.command()
async def r(die : str):
    (num,dice) = die.split("d")
    for i in range(int(num)):
        result = random.randint(1, int(dice))
        await bot.say("You rolled a: " + str(result))

@bot.command()
async def pogo(poke_to_find : str):
    with open(pokemon_file, 'r') as f:
        json_data = json.load(f)
        for p in json_data:
            if (search(str(poke_to_find), p['name'])):
                await bot.say("Found: " + str(p['name']))
                await bot.say("- Max CP: " + str(p['maxCP']))
                for poke_type in p['types']:
                    await bot.say("--- Type: " + str(poke_type['name']))
                time.sleep(0.5)

def search(search : str, pokemon : str):
    if search.lower() in pokemon.lower():
        return True
    else:
        return False

bot.run(TOKEN)
