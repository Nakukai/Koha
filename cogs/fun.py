import discord
from discord.ext import commands
from typing import Optional

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["av"])
    async def avatar(self, ctx, User: discord.User = None):
        userInfo = None
        if User == None:
            userInfo = ctx.author
        else:
            userInfo = User

        Embed = discord.Embed(
            color=0xFFFF00,
            description = f"{userInfo.name}'s Avatar\n"
        )
        Embed.set_image(url=userInfo.avatar_url)
        await ctx.send(embed=Embed)

def setup(client):
    client.add_cog(Fun(client))
