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
      Shop_Items = discord.Embed(
          color=0xef476f,
          title="Navya's Store",
          description="All the best materials in Koha right here."
      )
      Shop_Items.add_field(
          name="🔥 Stamifier",
          value=2500
      )
      Shop_Items.add_field(
          name="🍰 Transfer",
          value=1000
      )
      await ctx.send(embed=Shop_Items)

def setup(client):
    client.add_cog(Shop(client))
