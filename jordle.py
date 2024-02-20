class Player:
    def __init__(self, team, conference):
        self.team = team
        self.conference = conference

# PLAYER LIST
players = {}
def create_player(name, team, conference, players_dict):
    player = Player(team, conference)
    players_dict[name] = player

create_player("lebron", "Lakers", "West", players)
create_player("giannis", "Bucks", "East", players)

# TARGET PLAYER
player = players["lebron"]

win = 0
while win == 0:
    name = input("player: ")
    if name in players:
        teamguess = players[name].team
        conferenceguess = players[name].conference
        playerguess = players[name]
        if playerguess == player:
            win += 1
            print("you win")
        else:
            if conferenceguess == player.conference:
                print(f"{conferenceguess} is correct")
            else:
                print(f"{conferenceguess} is incorrect")

            if teamguess == player.team:
                print(f"{teamguess} is correct")
            else:
                print(f"{teamguess} is incorrect")
    else:
        print("Invalid Player")
