import discord
from discord.ext import commands
import json

class Analysis(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def compare(self, ctx, User: discord.User = None):
        if User == None:
            await ctx.send("Please ping someone after the command")
        else:
            pass

def setup(client):
    client.add_cog(Analysis(client))