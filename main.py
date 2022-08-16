## V0.1 of Miller Bot

import discord
import os
import requests # allows http requests for api
import json # allows data to be processed correctly from requets
import random # allows random selecting

client = discord.Client() ## Client should be named bot in future
prefix = '!!' # bot prefix

sadWords = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

starterEncouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person / bot!"
]

def getQuote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " - " + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('Logged in as: {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  
  if msg.startswith(prefix + 'Quote'):
    quote=getQuote()
    await message.channel.send(quote + ' :smile:')

  if any(word in msg for word in sadWords):
    await message.channel.send(random.choice(starterEncouragements))

client.run(os.getenv('KEY')) 


## variable or os.getinv could be used to get command prefix, allows ability to change and log