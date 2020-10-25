import asyncio
import discord
from discord.ext import commands

file = open("rules.txt","r")
rules = file.readlines()

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print("Bot is ready")

# This command will take number as an argument will show the requested rule
@bot.command()   
async def rule(ctx,*,number): 
    await ctx.send(rules[int(number)-1])

#This is a simple command to reply to the message "Hello"
@bot.command()
async def hello(ctx):
    await ctx.send("Hi")

# Will kick a member by checking for admin and mod permissions
@bot.command()
@commands.has_any_role('Administrator','Moderator')
async def kick(ctx,member : discord.Member,*,reason=None):
    await member.kick(reason=reason)

# Will only ban a member if admin is executing command
@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx,member : discord.Member,*,reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')

# Will only unban a member if admin is executing command
@bot.command()
@commands.has_permissions(administrator=True)
async def unban(ctx,*,member):
    banned_users = await ctx.guild.bans()
    member_name,member_discriminator = member.split('#') 

    for ban_entry in banned_users:
        user = ban_entry.user 

        if (user.name,user.discriminator) == (member_name,member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

# This will delete the messages on the channel with default value 10
@bot.command()
@commands.has_any_role('Admin','Moderator')
async def clear(ctx,amount=10):
    await ctx.channel.purge(limit=amount)

bot.run('NzY5NTAyNjM2NjgzOTUyMTg5.X5P9LQ.f_1DXbYfNBX6dNeADTXMh2z1GnM')
