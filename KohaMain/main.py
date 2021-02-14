import os
import discord
from discord.ext import commands

Token = ''
client = commands.Bot(command_prefix=["K!", "k!"], case_insensitive=True)
client.remove_command('help')

# EVENTS THAT OCCUR ON STARTUP
@client.event
async def on_ready():
    print("Mayu V 0.0.1 is live")
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# LOADS THE COGS IN THE COGS FILE INTO THE BOT FOR USE
@client.command()
@commands.is_owner()
async def load(ctx, extension):
    msg2 = await ctx.send("Will load in a few seconds...")
    await asyncio.sleep(5)
    client.load_extension(f'cogs.{extension}')
    await msg2.delete()
    loaded = await ctx.send("Successfully loaded")
    await loaded.delete()

client.run(Token)
