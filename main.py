#***************************************************************************#
#                                                                           #
# Doopliss - A Discord Bot For Me.                                          #
# https://github.com/NoraHanegan/Doopliss                                   #
# Copyright (C) 2021 Nora Hanegan. All rights reserved.                     #
#                                                                           #
# License:                                                                  #
# MIT License https://www.mit.edu/~amini/LICENSE.md                         #
#                                                                           #
#***************************************************************************#
import discord
import os
import platform

from cogs.base import Base
from cogs.fun import Fun
from cogs.marioparty import MarioParty
from cogs.toontown import Toontown
from cogs.verify import Verification
from cogs.gsheets import GSheets
from cogs.results_poster import RPoster

from discord.ext import tasks
from discord.ext import commands

#Intents
intents = discord.Intents.all()

#Define Client
bot = commands.Bot(description="Doopliss", command_prefix=commands.when_mentioned_or("/"), intents=intents, activity=discord.Game(name='around with different names'), guild_ids=[1048370760776962159])

@bot.event
async def on_ready():
  memberCount = len(set(bot.get_all_members()))
  serverCount = len(bot.guilds)
  print("                                                                ")
  print("################################################################") 
  print(f" ______                            __    _                     ")
  print(f"|_   _ `.                         [  |  (_)                    ")
  print(f"  | | `. \  .--.    .--.   _ .--.  | |  __   .--.   .--.       ")
  print(f"  | |  | |/ .'`\ \/ .'`\ \[ '/'`\ \| | [  | ( (`\] ( (`\]      ")
  print(f" _| |_.' /| \__. || \__. | | \__/ || |  | |  `'.'.  `'.'.      ")
  print(f"|______.'  '.__.'  '.__.'  | ;.__/[___][___][\__) )[\__) )     ")
  print(f"                           [__|              \___/  \___/      ")
  print("                                                                ")
  print("################################################################") 
  print("Running as: " + bot.user.name + "#" + bot.user.discriminator)
  print(f'With Client ID: {bot.user.id}')
  print("\nBuilt With:")
  print("Python " + platform.python_version())
  print("Py-Cord " + discord.__version__)


#Boot Cogs
bot.add_cog(Base(bot))
bot.add_cog(Fun(bot))
bot.add_cog(MarioParty(bot))
bot.add_cog(Toontown(bot))
bot.add_cog(Verification(bot))
bot.add_cog(GSheets(bot))
bot.add_cog(RPoster(bot))

#Run Bot
#keep_alive()
TOKEN = os.environ.get("TOKEN_DOOPLISS")
bot.run(TOKEN)
