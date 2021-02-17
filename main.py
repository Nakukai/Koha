import os
import discord
from discord.ext import commands
import asyncio

Token = ''
client = commands.Bot(command_prefix=["K!", "k!"], case_insensitive=True)
client.remove_command('help')
Prefix = "k!"

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


# UNLOADS COGS IN THE COG FILE OUT OF THE BOTS REACH
@client.command()
@commands.is_owner()
async def unload(ctx, extension):
    msg = await ctx.send("Will unload in a few seconds...")
    await asyncio.sleep(5)
    client.unload_extension(f'cogs.{extension}')
    await msg.delete()
    unloaded = await ctx.send("Successfully Unloaded")
    await unloaded.delete()

client.run(Token)
