import requests
from bs4 import BeautifulSoup

default_adrese = "https://www.eliteprospects.com"

u18address = "/team/1644/latvia-u18"
u20address = "/team/1645/latvia-u20"
senioraddress = "/team/1643/latvia"

selected_team1 = input("Select age group for TEAM 1: U18, U20, SENIOR || DEFAULT - SENIOR")
selected_team1 = selected_team1.upper()

if selected_team1 == "U18":
    adrese = default_adrese + u18address
elif selected_team1 == "U20":
    adrese = default_adrese + u20address
else:
    adrese = default_adrese + senioraddress

selected_year1 = input("Select year for TEAM 1, formatted xxxx-xxxx+1 || DEFAULT - CURRENT SEASON")
if len(selected_year1) == 9:
    adrese += "/" + str(selected_year1)
print(adrese)

selected_team2 = input("Select age group for TEAM 2: U18, U20, SENIOR || DEFAULT - SENIOR")
selected_team2 = selected_team2.upper()

if selected_team2 == "U18":
    adrese_2 = default_adrese + u18address
elif selected_team2 == "U20":
    adrese_2 = default_adrese + u20address
else:
    adrese_2 = default_adrese + senioraddress

selected_year2 = input("Select year for TEAM 2, formatted xxxx-xxxx+1 || DEFAULT - CURRENT SEASON")
if len(selected_year2) == 9:
    adrese_2 += "/" + str(selected_year2)
print(adrese_2)

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
lapa = requests.get(adrese)
if lapa.status_code == 200:
    lapas_saturs = BeautifulSoup(lapa.content, "html.parser")
    atradu_Player = lapas_saturs.find_all(class_="Roster_player__e6EbP")
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
            print(f"Name: {name}, Position: {position}")

print("Total goalie count: " + str(goalieCount))
print("Total defensemen count: " + str(defensemenCount))
print("Total forward count: " + str(forwardCount))
print("Total player count: " + str(playerCount))

print("=============== 2ND TEAM ROSTER =================")
lapa = requests.get(adrese_2)
if lapa.status_code == 200:
    lapas_saturs = BeautifulSoup(lapa.content, "html.parser")
    atradu_Player = lapas_saturs.find_all(class_="Roster_player__e6EbP")
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
            print(f"Name: {name}, Position: {position}")

print("Total goalie count: " + str(goalieCount_2))
print("Total defensemen count: " + str(defensemenCount_2))
print("Total forward count: " + str(forwardCount_2))
print("Total player count: " + str(playerCount_2))
print("=============== PLAYERS ON BOTH TEAMS =================")

for i in range(len(roster_1)):
    for j in range(len(roster_2)):
        if roster_1[i]==roster_2[j]:
            print(roster_1[i])
            break
