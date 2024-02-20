import pandas as pd
class Player:
    def __init__(self, conference, team, position, height):
        self.conference = conference
        self.team = team
        self.position = position
        self.height = height

westteams = ["Denver Nuggets","Minnesota Timberwolves","Oklahoma City Thunder", "Portland Trail Blazers", "Utah Jazz", "Golden State Warriors", "LA Clippers","Los Angeles Lakers","Phoenix Suns","Sacramento Kings","Dallas Mavericks","Houston Rockets","Memphis Grizzlies","New Orleans Pelicans","San Antonio Spurs"]

players = {}
def create_player(name, conference, team, position, height, players_dict):
    player = Player(conference, team, position, height)
    players_dict[name] = player

playerdata = pd.read_csv("nbaplayers.csv")
playerdata.head()
names = playerdata["name"]
for i in range(len(playerdata)):
    autoname = playerdata["name"][i]
    autoteam = playerdata["team"][i]
    autoposition = playerdata["position"][i]
    autoheight = (playerdata["height"][i])
    heightadjusted = autoheight[:-2]
    heightconverted = (int(heightadjusted)% 1)
    print(heightconverted)
    if autoteam in westteams:
        autoconference = "Western Conference"
    else:
        autoconference = "Eastern Conference"
    create_player(autoname, autoconference, autoteam, autoposition, autoheight, players)

# TARGET PLAYER
player = players["Bam Adebayo"]

win = 0
while win == 0:
    name = input("Player: ")
    if name in players:
        playerguess = players[name]
        conferenceguess = players[name].conference
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
