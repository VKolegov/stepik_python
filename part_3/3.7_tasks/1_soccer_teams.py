n = int(input())

teamsData = {}
for i in range(n):
    game = input().strip().split(sep=";")

    team1 = game[0]
    team2 = game[2]

    if team1 not in teamsData:
        teamsData[team1] = {"points": 0, "games": 0, "wins": 0, "losses": 0, "ties": 0}
    if team2 not in teamsData:
        teamsData[team2] = {"points": 0, "games": 0, "wins": 0, "losses": 0, "ties": 0}

    teamsData[team1]["games"] += 1
    teamsData[team2]["games"] += 1

    team1Goals = int(game[1])
    team2Goals = int(game[3])

    if team1Goals > team2Goals:
        teamsData[team1]["points"] += 3
        teamsData[team1]["wins"] += 1
        teamsData[team2]["losses"] += 1
    elif team1Goals < team2Goals:
        teamsData[team2]["points"] += 3
        teamsData[team2]["wins"] += 1
        teamsData[team1]["losses"] += 1
    else:
        teamsData[team2]["ties"] += 1
        teamsData[team1]["ties"] += 1
        teamsData[team1]["points"] += 1
        teamsData[team2]["points"] += 1

for teamName, teamData in teamsData.items():
    print(teamName + ":", end="")
    print(teamData["games"], teamData["wins"], teamData["ties"], teamData["losses"], teamData["points"])
