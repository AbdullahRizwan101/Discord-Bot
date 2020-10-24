import discord
from discord.ext import commands

file = open("rules.txt","r")
rules = file.readlines()

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("Bot is ready")


#This command will take number as an argument will show the requested rule
@bot.command()   
async def rule(ctx,*,number): 
    await ctx.send(rules[int(number)-1])

#This is a simple command to reply to the message "Hello"
@bot.command()
async def hello(ctx):
    await ctx.send("Hi")

@bot.command()
async def 

bot.run('NzY5NTAyNjM2NjgzOTUyMTg5.X5P9LQ.Fw7O6j0KmlWnSN0NXEuQQgM05Ss')