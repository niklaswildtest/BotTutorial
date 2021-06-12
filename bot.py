import discord
import asyncio
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!')

client.run('')