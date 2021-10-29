import discord
import random
from os import getenv
import traceback

client = discord.Client()

def dice(args):
    text = ''
    if len(args) == 0:
        text += str(random.randint(1, 6))
    elif len(args) == 1 and str.isdigit(args[0]):
        n = int(args[0])
        text += str(random.randint(1, n)) if n >= 1 else 'please input a number greater than 0'
    elif len(args) == 2 and str.isdigit(args[0]) and str.isdigit(args[1]):
        n1 = int(args[0])
        n2 = int(args[1])
        n1, n2 = (n2, n1) if n1 > n2 else (n1, n2)
        text += str(random.randint(n1, n2))
    else:
        text += 'invalid input'
    return text

def exec_command(ctx):
    args = ctx.content.replace('　', ' ').split(' ')
    while '' in args:
        args.remove('')
    command = args[0]
    text = ''
    if command == "/dice":
        text += dice(args[1:])
    elif command == "/gacha":
        text += random.choice(args[1:]) if len(args) > 1 else "please input element eg. /gacha hoge fuga"
    return text

@client.event
async def on_ready():
    print('start bot')

@client.event
async def on_message(ctx):
    if ctx.author.bot:
        return
    text = exec_command(ctx)
    if text:
        await ctx.channel.send(text)