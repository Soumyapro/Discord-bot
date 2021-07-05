import discord
import os
import requests
import json
import random
from keep_alive import keep_alive

client = discord.Client()

your_sad_words = ["unhappy","angry","depressed","depressing","anxiety","tired","sad"]
inspiring_statements = [
  "hang in there",
  "you are a nice person.smile always",
  "cheer up!"
]
def get_quote():

  response = requests.get("https://zenquotes.io/api/random")

  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]["a"]
  return(quote)


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if(message.author == client.user):
    return
  msg = message.content

  if(msg.startswith("hello")):
    await message.channel.send("Hey!")
  
  if(msg.startswith("how are you?")):
    await message.channel.send("i am fine")

  if(msg.startswith("inspire me")):
    quote = get_quote()
    await message.channel.send(quote)

  if any(word in msg for word in your_sad_words):
    await message.channel.send(random.choice(inspiring_statements))
keep_alive()
client.run(os.getenv('TOKEN'))


  
