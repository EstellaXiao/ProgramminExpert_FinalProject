# Project description: https://www.programmingexpert.io/projects/tournament-game-generator

# 函数：数字字符串检验
def int_teller(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

# 函数：分词器
def splitter(n):
    word_bank = n.split(" ")
    return len(word_bank)


# 输入团队数量 + 偶数校验 + >2校验
while True:
    team_number = input("Enter the number of teams in the tournament: ")
    if int_teller(team_number) != True:
        print("Invalid input: please enter an int!")
    elif int(team_number) < 2:
        print("The minimum number of teams is 2. Please try again.")
    elif int(team_number) % 2 != 0:
        print("Team numbers have to be odd. Please try again.")
    else:
        break

team_num = int(team_number)
team_namelist = []

# 输入团队名称 + 校验
for i in range(team_num):
    while True:
        team_name = input(f"Enter the name for team #{i + 1}: ")
        if len(team_name) < 2:
            print("Team names must have at least 2 characters. Please try again.")
        elif splitter(team_name) > 2:
            print("Team names may have at most 2 words. Please try again.")
        else:
            team_namelist.append(team_name)
            break

# 输入比赛数量
while True:
    game_num = input("Enter the number of games played by each team: ")
    if int_teller(game_num) != True:
        print("Invalid input: please enter an int!")
    elif int(game_num) < team_num - 1:
        print("Invalid number of games. Each team plays each other at least once in the regular season, try again.")
    else:
        break

# 输入各队胜利数量
team_viclist = {}
for i in range(team_num):
    while True:
        team = team_namelist[i]
        victory = input(f"Enter the number of wins Team {team} had: ")
        if int_teller(victory) != True:
            print("Invalid input: please enter an int!")
        elif int(victory) > int(game_num):
            print(f"The maximum number of wins is {team_num}. Please try again.")
        elif int(victory) < 0:
            print(f"The minimum number of wins is 0. Please try again.")
        else:
            team_viclist.update({team:int(victory)})
            break

print("Generating the games to be played in the first round of the tournament...")

# 计算比赛阵容

comp_list = dict(sorted(team_viclist.items(), key=lambda s: s[1], reverse=True))
team_namelist_final = []
for i in comp_list.keys():
    team_namelist_final.append(i)

break_point = team_num / 2

for i in range(int(break_point)):
    home_team = team_namelist_final[i]
    away_team = team_namelist_final[team_num-i-1]
    print(f"Home: {away_team} VS Away: {home_team}")




