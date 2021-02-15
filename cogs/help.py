import discord 
from discord.ext import commands
import datetime
Prefix = "k!"

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        Help_Embed = discord.Embed(
            color=0xFFFF00, 
            title="Koha - City Of Light", 
            description="Welcome to Koha. Please have a look around and tell us what you would like.\n"
                       f"`{Prefix}help Koha` - Know more about what Koha is about\n"
                       f"`{Prefix}help Fun` - Check out our fun commands you can use\n"
            )
        Help_Embed.set_footer(text=datetime.datetime.now())
        await ctx.send(embed=Help_Embed)

def setup(client):
    client.add_cog(Help(client))