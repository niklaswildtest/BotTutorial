import discord
import asyncio
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!')

#Start-and-change-status
@client.event
async def on_ready():
    print(f'Status: Online as {client.user}!')
    client.loop.create_task(status_task())
    
    async def status_task():
    while True:
        await client.change_presence(activity=discord.Game("Computers are cool {-;"), status=discord.Status.online)
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game("I am a Bot 🤖"), status=discord.Status.online)
        await asyncio.sleep(10)

        
#JoinMessage
@client.event
async def on_member_join(member):
    await member.send(f"Welcome to **{member.guild}**!")
    print(f"{member.name} is joined to {member.guild}")
    
    
#Ban-and-kick
@commands.has_permissions(kick_members=True)
@client.command()
async def kick(ctx, user: discord.Member, *, reason="No Reason"):
        await user.kick(reason=reason)
        print(f'{ctx.author} has {user.name} kicked!')
        kick = discord.Embed(title=f":boot: Kicked {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
        await ctx.message.delete()
        await ctx.channel.send(embed=kick)
        await user.send(embed=kick)


@commands.has_permissions(ban_members=True)
@client.command()
async def ban(ctx, user: discord.Member, *, reason="No Reason"):
        await user.ban(reason=reason)
        print(f'{ctx.author} has {user.name} banned!')
        ban = discord.Embed(title=f":boot: Banned {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}")
        await ctx.message.delete()
        await ctx.channel.send(embed=ban)
        await user.send(embed=ban)

        
#Shutdown
@client.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.channel.send("Bot is shutting down ...\r\n"
                           "This can take a few minutes ...")
    await ctx.bot.logout()
    print(str(ctx.author) + " has terminated bot")
   
  
client.run('Your Token! But not here!')
Test
