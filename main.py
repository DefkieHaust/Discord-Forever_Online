import os
import sys
from discord import Status
from discord.ext import commands

token = "token_here"

d = {"online": Status.online, "idle": Status.idle, "dnd": Status.dnd}
try:
  status = d[sys.argv[1].lower()]
except KeyError:
  print("Such status doesn't exist.")
  exit(1)
except IndexError:
  print("You didn't put an status.")
  exit(1)

bot = commands.Bot(command_prefix="∆", status=status)

print(f"Bot running in {sys.argv[1].lower()} mode")

@bot.event
async def on_ready():
  while True:
    e = input('Enter "exit" to terminate the bot: ')
    if e == "exit":
      os._exit(os.EX_OK)
    else:
      sys.stdout.write('\x1b[1A')
      sys.stdout.write('\x1b[2K')

bot.run(token)
