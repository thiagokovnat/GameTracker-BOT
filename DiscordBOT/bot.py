import asyncio
import discord
from discord.ext import commands
import time
from RiotAPI import RequestManager as RM
from RiotAPI import Player
from dotenv import load_dotenv
import os


client = commands.Bot(command_prefix = "!")
load_dotenv()

token = os.getenv("DISCORD-TOKEN")
guild = "RSwrcb"
riotapi = RM.PlayerTracker("LAS", os.getenv("RIOT-TOKEN"))

def createPlayerEmbed(jugador):
	embedVar = discord.Embed(title="Name", description= jugador.name.title(), color=0x00ff00)
	embedVar.add_field(name="Rank", value= f""" {jugador.league} {jugador.tier}""", inline=False)
	embedVar.add_field(name="LP", value= jugador.LP, inline=False)
	embedVar.add_field(name="Promo", value= jugador.promo, inline=False)
	embedVar.add_field(name="Hot Streak", value= jugador.hotstreak, inline=False)
	embedVar.add_field(name="Masteries", value= ", ".join(jugador.getTopMasteries()), inline=False)
	embedVar.set_thumbnail(url = jugador.image)
	return embedVar

def createChampionEmbed(champion):
	pass

@client.event
async def on_ready():
	print("Succesfully connected to guild.")


@client.command(name = "soloq", help = "gives information about a players soloq rank")
async def getSoloQStats(ctx, *args):

	summonerName = " ".join([x for x in args])

	try:
		jugador = riotapi.RankedStats(summonerName)
		jugador.setChampionMasteries(riotapi.getChampionMastery(jugador.name))

		topMasteries = jugador.getTopMasteries()

		embed = createPlayerEmbed(jugador)
		await ctx.send(embed = embed)

	except Exception as e:
		print(e)
		await ctx.send("`No user found.`")

@client.command(name = "region", help = "sets region for bot")
async def setRegion(ctx, region):

	try:
		riotapi.setRegion(region)
		await ctx.send(f"""```Region succesfully changed to: {region}```""")

	except Exception as e:
		await ctx.send("`Invalid Region`")

@client.command(name = "flex", help = "gives ranked flex stats")
async def getRankedFlex(ctx, *args):

	summonerName = " ".join([x for x in args])

	try:
		jugador = riotapi.RankedStats(summonerName, queue = "flex")
		jugador.setChampionMasteries(riotapi.getChampionMastery(jugador.name))

		embed = createPlayerEmbed(jugador)
		await ctx.send(embed = embed)

	except Exception as e:
		await ctx.send("`No user found.`")

@client.command(name = "champ", help = "gives info about a champion")
async def getChampionInfo(ctx, *args):
	pass

client.run(token)
