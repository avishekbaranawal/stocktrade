# bot.py
import os
import random
import discord
import yfinance as yf
from dotenv import load_dotenv

#1
from discord.ext import commands

load_dotenv("text.env")
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name="stock")




@bot.command(name='hello')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'Sometimes, the most enlightened response is: ',
        'Don’t cry. Say "### you” and smile”',
        (
           
            '#### you and goodnight'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)


bot.run(TOKEN)
