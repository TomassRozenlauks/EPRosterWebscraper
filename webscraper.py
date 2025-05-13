import requests
from bs4 import BeautifulSoup

default_adrese = "https://www.eliteprospects.com/team/673/dinamo-riga"



adrese = "https://www.eliteprospects.com/team/1645/latvia-u20/2023-2024"
adrese_2 = "https://www.eliteprospects.com/team/1645/latvia-u20"



playerCount = 0
goalieCount = 0
defensemenCount = 0
forwardCount = 0

playerCount_2 = 0
goalieCount_2 = 0
defensemenCount_2 = 0
forwardCount_2 = 0

roster_1 = []
roster_2 = []

print("=============== 1ST TEAM ROSTER =================")
# SCRAPING FIRST ROSTER
lapa = requests.get(adrese)
# print(lapa.status_code)
if lapa.status_code == 200:
    lapas_saturs = BeautifulSoup(lapa.content, "html.parser")
    # print(lapas_saturs.prettify())
    atradu_Player = lapas_saturs.find_all(class_="Roster_player__e6EbP")
    #print(len(atradu_Player))
    #print(atradu_Player)
    for player in atradu_Player:
        playerLink = player.find(class_="TextLink_link__RhSiC")
        if playerLink:
            playerCount += 1
            fulltext = playerLink.get_text(strip=True)
            if '(' in fulltext and ')' in fulltext:
                name = fulltext.split("(")[0]
                position = fulltext.split("(")[-1].strip(")")
                if position[0] == "G":
                    goalieCount += 1
                elif position[0] == "D":
                    defensemenCount += 1
                else:
                    forwardCount += 1
                roster_1.append({"Name": name, "Position": position})
            #print(fulltext)
            print(f"Name: {name}, Position: {position}")

print("Total goalie count: " + str(goalieCount))
print("Total defensemen count: " + str(defensemenCount))
print("Total forward count: " + str(forwardCount))
print("Total player count: " + str(playerCount))
#print(roster_1)

# SCRAPING 2ND ROSTER
print("=============== 2ND TEAM ROSTER =================")
lapa = requests.get(adrese_2)
# print(lapa.status_code)
if lapa.status_code == 200:
    lapas_saturs = BeautifulSoup(lapa.content, "html.parser")
    # print(lapas_saturs.prettify())
    atradu_Player = lapas_saturs.find_all(class_="Roster_player__e6EbP")
    #print(len(atradu_Player))
    #print(atradu_Player)
    for player in atradu_Player:
        playerLink = player.find(class_="TextLink_link__RhSiC")
        if playerLink:
            playerCount_2 += 1
            fulltext = playerLink.get_text(strip=True)
            if '(' in fulltext and ')' in fulltext:
                name = fulltext.split("(")[0]
                position = fulltext.split("(")[-1].strip(")")
                if position[0] == "G":
                    goalieCount_2 += 1
                elif position[0] == "D":
                    defensemenCount_2 += 1
                else:
                    forwardCount_2 += 1
                roster_2.append({"Name": name, "Position": position})
            #print(fulltext)
            print(f"Name: {name}, Position: {position}")

print("Total goalie count: " + str(goalieCount_2))
print("Total defensemen count: " + str(defensemenCount_2))
print("Total forward count: " + str(forwardCount_2))
print("Total player count: " + str(playerCount_2))
#print(roster_2)
print("=============== PLAYERS ON BOTH TEAMS =================")

for i in range(len(roster_1)):
    for j in range(len(roster_2)):
        if roster_1[i]==roster_2[j]:
            print(roster_1[i])
