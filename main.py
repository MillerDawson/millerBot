## V0.1 of Miller Bot

import discord
import os

client = discord.Client() ## Client should be named bot in future

@client.event
async def on_ready():
  print('Logged in as: {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!!Hello'):
    await message.channel.send('Hello there :smile:')

client.run(os.getenv('KEY')) 


## variable or os.getinv could be used to get command prefix, allows ability to change and log