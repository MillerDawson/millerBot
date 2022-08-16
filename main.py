import discord # discord.py
import os
import requests # allows http requests for api
import json # allows data to be processed correctly from requets
import random # allows random selecting
from replit import db # allows replit db to be used

# VARIABLES

client = discord.Client() ## Client should be named bot in future
prefix = '!!' # bot prefix

sadWords = ["sad", "depressed", "unhappy", "angry", "miserable", "depressing"]

starterEncouragements = [
  "Cheer up!",
  "Hang in there.",
  "You are a great person / bot!"
]

if "responding" not in db.keys():
    db["responding"] = True

# PROCEDURES

def getQuote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " - " + json_data[0]['a']
  return(quote)

def updateEncouragement(encouragingMessage): # adds encouragement to db
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouragingMessage)
    db["encouragements"] = encouragements # saves db
  else:
    db["encouragements"] = [encouragingMessage]

def deleteEncouragement(index): # remove encouragement from db
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
    db["encouragements"] = encouragements

@client.event
async def on_ready():
  print('Logged in as: {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content
  msgSend = message.channel.send

  if db["responding"]:
    options = starterEncouragements
    if "encouragements" in db.keys():
      options = options + db["encouragements"].value
      
    if any(word in msg for word in sadWords):
      await msgSend(random.choice(options))

  if msg.startswith(prefix + 'Quote'):
      quote=getQuote()
      await msgSend(quote + ' :smile:')
  
  if msg.startswith(prefix + 'new '):
    encouragingMessage = msg.split(prefix + 'new ',1)[1]
    updateEncouragement(encouragingMessage)
    await msgSend("New Encouraging Message Added!")

  if msg.startswith(prefix + 'delete '):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split(prefix + 'delete',1)[1])
      deleteEncouragement(index)
      encouragements = db["encouragements"]
    await msgSend(encouragements)

  if msg.startswith(prefix + 'list'):
    await msgSend(db["encouragements"])

  if msg.startswith(prefix + 'autoreply'):
    autoStatus = msg.split(prefix + 'autoreply ',1)[1]
    if autoStatus == "on" or autoStatus == "On":
        if db["responding"] == True:
          await msgSend("Auto Reply is already enabled!")
        else:
          await msgSend("Auto Reply is now enabled!")
          db["responding"] = True

  if msg.startswith(prefix + 'autoreply'):
    autoStatus = msg.split(prefix + 'autoreply ',1)[1]
    if autoStatus == "off" or autoStatus == "Off":
        if db["responding"] == False:
          await msgSend("Auto Reply is already disabled!")
        else:
          await msgSend("Auto Reply is now disabled!")
          db["responding"] = False

client.run(os.getenv('KEY')) 