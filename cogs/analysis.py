import discord
from discord.ext import commands
import json

class Analysis(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group()
    async def compare(self, ctx, User: discord.User = None):

def setup(client):
    client.add_cog(Analysis(client))