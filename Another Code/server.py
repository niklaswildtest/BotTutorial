import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)

#This command shows you which servers your bot is on!
#Server-Command
@client.command()
async def server(ctx):
  for guild in client.guilds:
    print(str(guild.name))
    
    
client.run('Your Token! But not here!')
