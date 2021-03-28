from .Player import Player
import json
import cassiopeia as cass
from cassiopeia import Summoner, Champion
import pandas as pd

validRegions = ["LAN","LAS","BR","EUW","EUE"]

class PlayerTracker():

	def __init__(self, region, key):
		if region.upper() not in validRegions:
			raise Exception("Invalid Region")

		cass.set_riot_api_key(key)
		cass.set_default_region(region)

		self.region = region

	def setRegion(self, region):
		if region.upper() not in validRegions:
			raise Exception("Invalid Region")
		else:
			self.region = region


	def getSummoner(self, summonerName):
		summoner = Summoner(name = summonerName, region = self.region)
		return summoner

	def getRankedSummoner(self, summonerName):
		summoner = self.getSummoner(summonerName)
		entries = summoner.league_entries

		if entries.fives.promos is not None:
			return Player(summonerName, entries.fives.tier,entries.fives.division, True, entries.fives.league_points, entries.fives.hot_streak, summoner.profile_icon.url)
		else:
			return Player(summonerName, entries.fives.tier,entries.fives.division, False, entries.fives.league_points, entries.fives.hot_streak, summoner.profile_icon.url)

	def getRankedFlexSummoner(self, summonerName):
		summoner = self.getSummoner(summonerName)
		entries = summoner.league_entries

		if entries.fives.promos is not None:
			return Player(summonerName, entries.flex.tier,entries.flex.division, True, entries.flex.league_points, entries.flex.hot_streak, summoner.profile_icon.url)
		else:
			return Player(summonerName, entries.flex.tier,entries.flex.division, False, entries.flex.league_points, entries.flex.hot_streak, summoner.profile_icon.url)

	def getChampion(self, championName):
		champion = Champion(name = championName, region = self.region)
		return champion

	def getChampionMastery(self, summonerName):
		summoner = self.getSummoner(summonerName)
		master = summoner.champion_masteries
		pro = master.filter(lambda cm: cm.level >= 5)

		return pro

	def RankedStats(self, summonerName, queue = "solo"):

		if queue.lower() == "solo":
			player = self.getRankedSummoner(summonerName)
		elif queue.lower() == "flex":
			player = self.getRankedFlexSummoner(summonerName)
		else:
			raise Exception("Invalid Queue")

		masteries = self.getChampionMastery(summonerName)
		player.setChampionMasteries(masteries)

		return player

	def getChampionInfo(self, championName):
		champ = Champion(name = championName, region = self.region)
		print(champ.name)
		return champ
