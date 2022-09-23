file =  open('log1.txt', mode='r')
lines=file.readlines()
lines=[i.strip('\n') for i in lines]
no_of_scoring_players=[]
team_back_and_forth=[]
team_1_score=0
team_2_score=0
first_team=0
second_team=0
whowon=0
whodidntwin=0
howthemplayersscored=[]
a=0
for i in lines:
    i=i.split(' ')
    team_back_and_forth.append(i[0])
    if int(i[-1])!=0:
        howthemplayersscored.append(i[1])
[no_of_scoring_players.append(i) for i in howthemplayersscored if i not in no_of_scoring_players]
print(len(no_of_scoring_players))
first_team=team_back_and_forth[0]
while a<int(len(howthemplayersscored)-1):
    if team_back_and_forth[a]!=first_team:
        second_team=team_back_and_forth[a]
    a+=1
print(first_team)
print(second_team)
for i in lines:
    i=i.split(' ')
    if i[0]==first_team:
        team_1_score+=int(i[-1])
    elif i[0]==second_team:
        team_2_score+=int(i[-1])
    if team_1_score>team_2_score:
        whowon=first_team
        whodidntwin=second_team
    else:
        whowon=second_team
        whodidntwin=first_team
print(team_1_score, team_2_score)
print(whowon,whodidntwin)
print(howthemplayersscored[0], howthemplayersscored[-1])



