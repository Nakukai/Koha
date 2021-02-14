import discord
from discord.ext import commands
import json

class Start(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command
    async def start(self, ctx):
        pass

def setup(client):
    client.add_cog(Start(client))