import os
import sys

# Day 2 part 1
# A = Rock
# B = Paper
# C = Scissors
# X = Rock
# Y = Paper
# Z = Scissors
# 1 point for Rock
# 2 points for Paper
# 3 points for Scissors
# 0 for Loss
# 3 for Draw
# 6 for Win

with open(os.path.join(sys.path[0], "day2input.txt"), 'r') as f:
    strategyguide = f.readlines()
    totalscore = 0
    for round in strategyguide:
        roundpoints = 0
        elfchoice = round[0]
        playerchoice = round[2]
        print (elfchoice, playerchoice)
        if playerchoice == 'X':
            roundpoints += 1
            if elfchoice == 'A':
                roundpoints += 3
            elif elfchoice == 'B':
                roundpoints += 0
            elif elfchoice == 'C':
                roundpoints += 6
        elif playerchoice == 'Y':
            roundpoints += 2
            if elfchoice == 'A':
                roundpoints += 6
            elif elfchoice == 'B':
                roundpoints += 3
            elif elfchoice == 'C':
                roundpoints += 0
        elif playerchoice == 'Z':
            roundpoints += 3
            if elfchoice == 'A':
                roundpoints += 0
            elif elfchoice == 'B':
                roundpoints += 6
            elif elfchoice == 'C':
                roundpoints += 3
        print(roundpoints)
        totalscore += roundpoints
    print(totalscore)

# Day 2 part 2
# A = Rock
# B = Paper
# C = Scissors
# X = Lose
# Y = Draw
# Z = Win
# 1 point for Rock
# 2 points for Paper
# 3 points for Scissors
# 0 for Loss
# 3 for Draw
# 6 for Win

with open(os.path.join(sys.path[0], "day2input.txt"), 'r') as f:
    strategyguide = f.readlines()
    totalscore = 0
    for round in strategyguide:
        roundpoints = 0
        elfchoice = round[0]
        roundoutcome = round[2]
        print (elfchoice, playerchoice)
        if roundoutcome == 'X':
            roundpoints += 0
            if elfchoice == 'A':
                roundpoints += 3
            elif elfchoice == 'B':
                roundpoints += 1
            elif elfchoice == 'C':
                roundpoints += 2
        elif roundoutcome == 'Y':
            roundpoints += 3
            if elfchoice == 'A':
                roundpoints += 1
            elif elfchoice == 'B':
                roundpoints += 2
            elif elfchoice == 'C':
                roundpoints += 3
        elif roundoutcome == 'Z':
            roundpoints += 6
            if elfchoice == 'A':
                roundpoints += 2
            elif elfchoice == 'B':
                roundpoints += 3
            elif elfchoice == 'C':
                roundpoints += 1
        print(roundpoints)
        totalscore += roundpoints
    print(totalscore)