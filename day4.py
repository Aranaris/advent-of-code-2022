import os
import sys
import re

#Day 4 part 1 solution
with open(os.path.join(sys.path[0], "day4input.txt"), 'r') as f:
    input = f.readlines()
    fulloverlapcount = 0
    parsedinput = []
    for x in input:
        x = x.replace('\n','')
        sections = re.split('-|,', x)
        sections = list(map(int, sections))
        parsedinput.append(sections)
        if (sections[0] >= sections[2] and sections[1] <= sections[3]) \
            or (sections[2] >= sections[0] and sections[3] <= sections[1]):
            fulloverlapcount += 1
    print(fulloverlapcount)

#Day 4 part 2 solution
    partialoverlapcount = 0
    overlappingsections = []
    for assignment in parsedinput:
        for i in range(assignment[0],assignment[1]+1):
            if i in range(assignment[2], assignment[3]+1):
                partialoverlapcount += 1
                overlappingsections.append(assignment)
                break

    print(partialoverlapcount)