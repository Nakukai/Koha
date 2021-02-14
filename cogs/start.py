import discord
from discord.ext import commands
import json
import random

Palettes = ["Koyoku", "Murato", "Kaiyoi", "Pinkai", "Kirayaka", "Mishizen", "Namikai"]

class Start(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command
    async def start(self, ctx):
        # VARIABLES
        data = {}
        Skills = {}
        Inventory = {}
        Quiz = {}
        InSystem = False
        Success = None

        data['Users'].append(
            ,{
                "User_ID" : ctx.author.id,
                "Palette" : random.choice(Palettes),
                "Status" : "None",
                "Cari" : 0,
                "Level" : 0,
                "Tier" : "None",
                "Points" : 0
            }
        )

        Skills['Users'].append(
            ,{
                "User_ID" : ctx.author.id,
                "Skills" : [
                    {}
                ]
            }
        )

        Inventory['Users'].append(
            "User_ID" : ctx.author.id,
            "Inventory" : {
                "Cut" : "active"
            }
        )

        JsonData = open("storage/users.json", "r")
        Users = json.loads(JsonData.read())
        for i in range(len(Users['Users'])):
            if ctx.author.id == Users['Users'][i]['User_ID']:
                InSystem = True
                break
            else:
                Insystem = False

        if Insystem == True:
            await ctx.send("You're already part of the colors.")
        elif Insystem == False:
            Days = datetime.utcnow() - ctx.author.created_at
            if Days < 30:
                TooYoung = discord.Embed(color=0xFFFF00, description="We cannot accept you into our system as your account is too young. "
                                                                    f"Please type {Prefix}!verify to join our verification server for accounts about 2 weeks old.")
            elif Days > 30:
                with open('storage/users.json', 'w') as f:
                    json.dump(data, f)
                    f.close()
                with open('storage/inv.json') as x:
                    json.dump(Inventory, x)
                    x.close()
                with open('storage/skills.json') as y:
                    json.dump(Skills, y)
                    y.close()
                for i in range(len(Users['Users'])):
                    if ctx.author.id == Users['Users'][i]['User_ID']:
                        Success = True
                        break
                    else:
                        Success = False

        if Success == True:
            await ctx.send("**Welcome To Koha - City Of Light**")
        elif Success == False:
            await ctx.send("Error. Please type `k!invite` for help.")
        elif Success == None:
            pass

def setup(client):
    client.add_cog(Start(client))