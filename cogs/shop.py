import random
import discord
import os
import json
from discord.ext import commands

class Shop(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def shop(self, ctx):
        pass

def setup(client):
    client.add_cog(Shop(client))