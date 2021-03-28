import cassiopeia as cass
from cassiopeia import Summoner, Champion


class Player():

    def __init__(self, name, league, tier, promo, LP, hotstreak, image):
        self.name = name
        self.league = league
        self.promo = promo
        self.LP = LP
        self.tier = tier
        self.hotstreak = hotstreak
        self.image = image
        self.championMasteries = []

    def getTopMasteries(self):
        return [x for x in self.championMasteries[0:3]] if len(self.championMasteries) > 2 else self.championMasteries

    def setChampionMasteries(self, champions):
        self.championMasteries = [x.champion.name for x in champions]
