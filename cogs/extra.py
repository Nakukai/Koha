import discord
from discord.ext import commands

class Extra(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def invite(self, ctx):
        Invitation = discord.Embed(
            color=0xFFB6C1, 
            description="**Want me to join your amazing server?**\n"
                        "[Tap here to invite me](%s)" % 
                        ("https://discord.com/api/oauth2/authorize?client_id=783865415746977824&permissions=3533888&scope=bot"))
        await ctx.send(embed=Invitation)

    @commands.command()
    async def support(self, ctx):
        Mayuport = discord.Embed(
            color=0xFF0000, 
            description="**Have you found any bugs or just need help with something?**\n"
                        "[Tap here to join](%s)" % ("https://discord.gg/5zpHR7JpZA"))
        await ctx.send(embed=Mayuport)

    @commands.command()
    async def supporter(sef, ctx):
        await ctx.send("**Coming in Mayu V 0.0.3**")

def setup(client):
    client.add_cog(Extra(client))
