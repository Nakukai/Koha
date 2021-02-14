import os
import discord
from discord.ext import commands

Token = ''
client = commands.Bot(command_prefix=["K!", "k!"], case_insensitive=True)
client.remove_command('help')

client.run(Token)
