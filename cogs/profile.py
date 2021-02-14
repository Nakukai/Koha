import discord
from discord.ext import commands
import json

class Profile(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def profile(self, ctx):
        pass

def setup(client):
    client.add_cog(Profile(client))