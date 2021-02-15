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

    @commands.command(aliases=["8ball"])
    async def eightball(self, ctx, *, question):
        responses = ("It is certain.",
                    "It is decidedly so.",
                    "Without a doubt.",
                    "Yes - definitely.",
                    "You may rely on it.",
                    "As I see it, yes.",
                    "Most likely.",
                    "Outlook good.",
                    "Yes.",
                    "Signs point to yes.",
                    "Reply hazy, try again.",
                    "Ask again later.",
                    "Better not tell you now.",
                    "Cannot predict now.",
                    "Concentrate and ask again.",
                    "Don't count on it.",
                    "My reply is no.",
                    "My sources say no.",
                    "Outlook not so good.",
                    "Very doubtful.")      
        embed = discord.Embed(colour=0XFF69B4)
        embed.add_field(name='Question', value=f'{question}', inline=False)
        embed.set_thumbnail(url=ctx.author.avatar_url)
        embed.add_field(name='Answer', value=f'{random.choice(responses)}', inline=False)
        embed.set_footer(text="This is my honest opinion about your question")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Fun(client))
