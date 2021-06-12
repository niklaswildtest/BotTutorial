import discord
from discord import commands
import os
import youtube_dl

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)

#MusicBot
@client.command()
async def play(ctx, url: str):
    if not ctx.author.voice:
        await ctx.author.send('You have to be in a voice channel for this command!')
        return
    if os.path.isfile('song.mp3'):
        try:
            os.remove("song.mp3")
        except PermissionError:
            await ctx.author.send("Wait until the song that is already playing ends!")
            return

    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice.channel != voice_channel:
        voice = await voice.move_to(voice_channel)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    [os.rename(file, 'song.mp3') for file in os.listdir('.') if file.endswith('.mp3')]
    if voice.is_playing:
        voice.stop()
    voice.play(discord.FFmpegPCMAudio("song.mp3"))


@client.command()
async def join(ctx):
    if not ctx.author.voice:
        await ctx.author.send('You are in no voice channel!')
        return
    voice_channel = ctx.author.voice.channel
    await voice_channel.connect()
    await asyncio.sleep(300)
    await ctx.author.send('You haven't interacted with the bot for too long! That's why I left the channel!')
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        return


@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.author.send("The bot is in no channel!")


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.author.send("There is no music playing at the moment!")


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.author.send("No music was paused!")


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()

    
client.run('Your Token! But not here!')
