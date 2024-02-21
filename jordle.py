import pandas as pd
import random

class Player:
    def __init__(self, conference, division, team, position, height):
        self.conference = conference
        self.team = team
        self.division = division
        self.position = position
        self.height = height
        
westteams = ["Denver Nuggets","Minnesota Timberwolves","Oklahoma City Thunder", "Portland Trail Blazers", "Utah Jazz", "Golden State Warriors", "LA Clippers","Los Angeles Lakers","Phoenix Suns","Sacramento Kings","Dallas Mavericks","Houston Rockets","Memphis Grizzlies","New Orleans Pelicans","San Antonio Spurs"]
atlantic = ["Boston Celtics", "New York Knicks", "Brooklyn Nets", "Philadelphia 76ers","Toronto Raptors"]
central = ["Cleveland Cavaliers", "Chicago Bulls", "Detroit Pistons","Indiana Pacers","Milwaukee Bucks"]
southeast = ["Atlanta Hawks", "Miami Heat","Charlotte Hornets","Orlando Magic","Washington Wizards"]
northwest = ["Minnesota Timberwolves","Portland Trail Blazers","Utah Jazz","Oklahoma City Thunder","Denver Nuggets"]
pacific = ["Los Angeles Lakers","LA Clippers","Phoenix Suns","Golden State Warriors","Sacramento Kings"]
players = {}

def create_player(name, conference, division, team, position, height, players_dict):
    player = Player(conference, division, team, position, height)
    players_dict[name] = player

playerdata = pd.read_csv("nbaplayers.csv")
for i in range(len(playerdata)):
    autoname = playerdata["name"][i]
    autoteam = playerdata["team"][i]
    autoposition = playerdata["position"][i]
    autoheight = (playerdata["height"][i])
    heightadjusted = autoheight[:-2]
    heightconverted = round(int(heightadjusted) * 0.0328084 * 12)
    heightfinal = heightconverted % 12
    if int(heightadjusted) > 182.88:
        heightfinalfinal = "6'" + str(heightfinal)
    elif int(heightadjusted) > 213.36:
        heightfinalfinal = "7'" + str(heightfinal)
    else:
        heightfinalfinal = "5'" + str(heightfinal)
    if autoteam in westteams:
        autoconference = "Western Conference"
        if autoteam in northwest:
            autodivision = "Northwest"
        elif autoteam in pacific:
            autodivision = "Pacific"
        else:
            autodivision = "Southwest"
    else:
        autoconference = "Eastern Conference"
        if autoteam in atlantic:
            autodivision = "Atlantic"
        elif autoteam in central:
            autodivision = "Central"
        else:
            autodivision = "Southeast"
    create_player(autoname, autoconference, autodivision, autoteam, autoposition, heightfinalfinal, players)

playerlist = list(players.keys())
random_value = random.choice(playerlist)
player = players[random_value]

win = 0
while win == 0:
    name = input("Player: ")
    if name in players:
        playerguess = players[name]
        conferenceguess = players[name].conference
        divisionguess = players[name].division
        teamguess = players[name].team
        positionguess = players[name].position
        heightguess = players[name].height
        if playerguess == player:
            win += 1
            print("Congratulations, you win!")
        else:
            if conferenceguess == player.conference:
                print(f"You're right, the player is in the {conferenceguess}")
            else:
                print(f"{conferenceguess} is incorrect.")
            if divisionguess == player.division:
                print(f"You're right, the player is in the {divisionguess} division")
            else:
                print(f"{divisionguess} is incorrect.")
            if teamguess == player.team:
                print(f"You're right, the player is on the {teamguess}")
            else:
                print(f"{teamguess} is incorrect.")
            if positionguess == player.position:
                print(f"You're right, the player is a {positionguess}")
            else:
                print(f"{positionguess} is incorrect.")
            if heightguess == player.height:
                 print(f"You're right, the player is {heightguess}")
            else:
                print(f"{heightguess} is incorrect.")
            print("Try again: ")
    else:
        print("Invalid Player")
