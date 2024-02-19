players = ["antetokounmpo","james","doncic","durant","jokic","booker","curry","davis","edwards","george","leonard","towns","adebayo","haliburton","lillard","tatum","banchero","barnes","brown","brunson","maxey","mitchell","randle","young","embiid"]
team =["bucks","lakers","mavericks","suns","nuggets","suns","warriors","lakers","timberwolves","clippers","clippers","timberwolves","heat","pacers","bucks","celtics","magic","raptors","celtics","knicks","sixers","cavaliers","knicks","hawks","sixers"]
conference = ["east","west","west","west","west","west","west","west","west","west","west","west","east","east","east","east","east","east","east","east","east","east","east","east","east"]
player = players[15]

win = 0
while win == 0:
    name = input("player: ")
    guessindex = (players.index(name))
    teamguess = team[guessindex]
    conferenceguess = conference[guessindex]
    playerguess = players[guessindex]
    if playerguess == player:
        win += 1
    elif conferenceguess == conference[15]:
        print(f"{conferenceguess} is correct")
        if teamguess == team[15]:
            print(f"{teamguess} is correct")
    else:
        print(f"{conferenceguess} is incorrect")
        print(f"{teamguess} is incorrect")

if win == 1:
    print("you win")
