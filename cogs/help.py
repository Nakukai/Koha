import discord 
from discord.ext import commands
import datetime

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client