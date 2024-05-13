import discord
from discord.ext import commands
import DiscordUtils
import time
import pandas as pd
intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)





token = ""

message = """

** FREE NFT  **

** MAY 9TH 2022 **

MEMBERS

To register and add your name to the list of the TATOO ARTIST ** FREE NFT** set to mint on ** MAY 9TH 2022 **  go to the "free-nft channel". Then Look for and click on the "FREENFT"  button and your name will be added to the registration list.

THE TATTOO SHOP 

Link to channel: https://discord.com/channels/892703121254547457/969175022876885053

"""


@client.command()
async def dm_all(ctx, * ,args=None):
    counter = 0
    for guild in client.guilds:
        print(guild)
        if "THE TATTOO SHOP  |  FREE NFT" in str(guild):
          
            for member in guild.members:

                if counter <= 15:
                    counter +=1
                    try:
                        await member.send(f"Hey @{member.name}, \n" + message)
                        print(f"DM sent to {member.name}")
                    except:
                         print('Could not DM user, closed DMs.')
                else:
                    counter = 0
                    print("15 DM sent sleeping for 60 sec")
                    time.sleep(60)

                

        if "THE TATTOO SHOP  |  FREE NFT" in str(guild):
            break

client.run(token)