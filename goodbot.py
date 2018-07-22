import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import config

def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)

def getNumbers(str):
	arr = []
	for s in str.split():
		if s.isdigit():
			arr.append(s)
	return arr

client = Bot(description="goodbot", command_prefix="#", pm_help = False)

@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('--------')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
	print('--------')
	return await client.change_presence(game=discord.Game(name='I wish to die')) #This is buggy, let us know if it doesn't work.

@client.command()
async def ping(*args):

	await client.say(":ping_pong: Pong!")
	await asyncio.sleep(3)

@client.command()
async def lul(*args):

	await client.say("boink")
	await asyncio.sleep(3)

@client.event
async def on_message(message):

	#If the bot didn't send the message
	if message.author == client.user:
		return
	if message.author.bot:
		return

	#if the message has numbers
	if hasNumbers(message.content):
		input = str(message.content)

		temp = getNumbers(input)

		await client.send_message(message.channel, "It's 420 somewhere")

	await client.process_commands(message)
	await asyncio.sleep(3)

client.run(config.token)
