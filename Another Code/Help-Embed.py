import discord
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)

#This is because Discord.py always creates a help command by default!
client.remove_command('help')

#Help-Embed
@client.command()
async def help(ctx):
  embed = discord.Embed(title="Help-Menu", description="Help-Menu from bot", color=0x00ff00)
  embed.add_field(name="Help", value="!help - This command", inline=False)
  embed.add_field(name="Test", value="!test - Test the bot", inline=False)
  guildicon = ctx.guild.icon_url
  embed.set_thumbnail(url=guildicon)
    mess = await ctx.channel.send(embed=embed)
    await mess.add_reaction("👍")
    print(str(ctx.author) + " has executed help command")
    
#Test-Command
@client.command()
async def test(ctx):
  await ctx.channel.send(f'{ctx.author.mention} everything works')
  print(f'{ctx.author} has tested whether the bot works')


client.run('Your Token! But not here!')
