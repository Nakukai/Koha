'''
MAIN FILE DIRECTORY FOR ALL ATTACK AND POINT GAINING RELATED MATERIAL

Anything related to earning points in user's accounts will be done here

It'll consist of different commands for attack, defense, survival etc...

Commands will be fully described within each command codeline for elaboration.
'''         

import discord
from discord.ext import commands
import json

class Main(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def battle(self, ctx, Opponent: discord.User = None):
        if Opponent == None:
            await ctx.send("Please mention an opponent with the command")
        else:
            pass

def setup(client):
    client.add_cog(Main(client))