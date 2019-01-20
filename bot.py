import discord
from discord.ext import commands
import random
import configparser

config = configparser.ConfigParser()
config.read('pybot.ini')


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

bot.run(TOKEN)
