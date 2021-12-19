import discord
from urllib.request import urlopen
import json

DISCORD_SERVER = "921972543353667644"
DISCORD_TOKEN = ""
BASE_API_URL = 'https://localhost:44389/api/'

with open('discordToken.txt', 'r') as f:
    DISCORD_TOKEN = f.readline()

if not DISCORD_TOKEN:
    exit(1)

client = discord.Client()

# NOTE TO FUTURE SELF: Per the discord library being used, these function names are required to be snake case

def monsterFormatToText(jsonObject):
    pass

@client.event
async def on_ready():
    print(f'{client.user} has connected to the server')

@client.event
async def on_message(message):
    # Splitting the message into individual words
    splitMessage = message.content.split()

    # Fail fast => make sure the user called the bot
    if splitMessage[0].lower() != '!mhr':
        return

    # Attempts to grab the name of the monster from the list, and capitalizes the first letter for the API
    monsterName = splitMessage[1].title()

    # Attempt to get the data back from the API
    response = urlopen(BASE_API_URL + monsterName)
    responseString = response.read().decode('utf-8')
    responseJson = json.loads(responseString)


    # Sending the monster name
    await message.channel.send(f'**{monsterName}**')

    monsterHabitats = responseJson['habitats']
    monsterHabitatsString = 'Found in: ' + ', '.join(monsterHabitats)

    await message.channel.send(f'_{monsterHabitatsString}_')



    print(responseJson)
    print(splitMessage)


client.run(DISCORD_TOKEN)