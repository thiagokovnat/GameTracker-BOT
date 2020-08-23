from RiotAPI import RequestManager as RM


test = RM.PlayerTracker("LAS", " RGAPI-67e3b4c2-e609-44ea-820f-d7181d1db4f9")

name = str(input("Ingrese un jugador:"))
player = test.RankedStats(name, "solo")

print("Player Name: " + player.name)
print("Division: " + str(player.league) + " " + str(player.tier))
print("LP: " + str(player.LP))
print("Promo: " + str(player.promo))
print("HotStreak: " + str(player.hotstreak))

print("MAESTRIAS: ")
for x in player.championMasteries[:3]:
	print(x)


