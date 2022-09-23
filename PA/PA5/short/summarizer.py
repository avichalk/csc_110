#Author: Avichal Kaul
#Description: Reads a gamelog file and summarizes the events that take place within it.
#Comments: I didn't realize that to get feedback on Gradescope you had to click
## on the submission, and just found out I've been losing marks for basically
## no reason except formatting. I tried to follow the style guidelines more
## closely for this one.

filename = input('enter gamelog file name:\n')

def main(filename):
    read_lines(filename)
    format_output()

def read_lines(filename):
    ##opening the file
    file =  open(filename, mode='r')
    lines=file.readlines()
    lines=[i.strip('\n') for i in lines]
    ## changing variables to global so
    ## they can be accessed by the other function
    global first_team, second_team, team_1_score
    global team_2_score, whowon, whodidntwin
    global no_of_scoring_players
    global first, last
    ## setting all values to 0 and
    ## creating some lists to store info
    no_of_scoring_players=[] ## list of all players who scored with duplicates removed
    team_back_and_forth=[] ## back and forth of which team scored, for convenience
    team_1_score=0
    team_2_score=0
    first_team=0
    second_team=0
    whowon=0
    whodidntwin=0
    howthemplayersscored=[] ##the list of how the players scored as given in the logfile
    a=0
    ## this bit gets the names of the players
    ## who scored and processes them to
    ## remove duplicates
    for i in lines:
        i=i.split(' ')
        team_back_and_forth.append(i[0])
        if int(i[-1])!=0:
            howthemplayersscored.append(i[1])
    [no_of_scoring_players.append(i)\
    for i in howthemplayersscored\
    if i not in no_of_scoring_players]
    ##figures out who the first team to score was
    ## and the second too
    first_team=team_back_and_forth[0]
    while a<int(len(howthemplayersscored)-1):
        if team_back_and_forth[a]!=first_team:
            second_team=team_back_and_forth[a]
        a+=1
    ## processes our lines to give us the
    ## team scores and who won
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
    ## gets the first and last players
    ## to score
    first=howthemplayersscored[0]
    last=howthemplayersscored[-1]


def format_output():
    ## formats and prints the output
    print(whowon, 'won!')
    print(first_team, 'scored', team_1_score, 'points.')
    print(second_team, 'scored', team_2_score, 'points.')
    print(len(no_of_scoring_players), 'players scored.')
    print(first, 'scored first.')
    print(last, 'scored last.')

main(filename)