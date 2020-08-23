import asyncio
import discord
from discord.ext import commands
import time
from RiotAPI import RequestManager as RM


client = commands.Bot(command_prefix = "!")

token = Discord-TOKEN
guild = "RSwrcb"
riotapi = RM.PlayerTracker("LAS", TOKEN)



@client.event
async def on_ready():
	print("Succesfully connected to guild.")


@client.command(name = "soloq", help = "gives information about a players soloq rank")
async def getSoloQStats(ctx, *args):

	summonerName = ""
	for word in args:
		summonerName += word + " "

	try:
		jugador = riotapi.getRankedSummoner(summonerName)
		jugador.setChampionMasteries(riotapi.getChampionMastery(jugador.name))

		topMasteries = jugador.getTopMasteries()

		await ctx.send(f"""``` Name: {jugador.name.title()}.```""")
		await ctx.send(f"""` Rank: {jugador.league} {jugador.tier}`""")
		await ctx.send(f"""` LP: {jugador.LP}`""")
		await ctx.send(f"""` Promo: {str(jugador.promo)}`""")
		await ctx.send(f"""` Hot Streak: {str(jugador.hotstreak)}`""")
		await ctx.send(f"""` Masteries: {[x for x in topMasteries]}`""")
   
	except Exception as e:
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

	summonerName = ""
	for word in args:
		summonerName += word + " "

	try:
		jugador = riotapi.getRankedFlexSummoner(summonerName)
		jugador.setChampionMasteries(riotapi.getChampionMastery(jugador.name))

		topMasteries = jugador.getTopMasteries()

		await ctx.send(f"""``` Name: {jugador.name.title()}.```""")
		await ctx.send(f"""` Rank: {jugador.league} {jugador.tier}`""")
		await ctx.send(f"""` LP: {jugador.LP}`""")
		await ctx.send(f"""` Promo: {str(jugador.promo)}`""")
		await ctx.send(f"""` Hot Streak: {str(jugador.hotstreak)}`""")
		await ctx.send(f"""` Masteries: {[x for x in topMasteries]}`""")

	except Exception as e:

		await ctx.send("`No user found.`")


client.run(token)

