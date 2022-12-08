import os
import sys

with open(os.path.join(sys.path[0], "day1input.txt"), 'r') as f:
    inputarray = f.readlines()
    elfcalories = [0]
    elfcounter = 0
    topthreeelves = [0, 0, 0]
    maxelf = 0
    secondelf = 0
    thirdelf = 0
    for i in range(len(inputarray)):
        if inputarray[i] == '\n':
            elfcounter += 1
            elfcalories.append(0)
        else: 
            inputarray[i] = inputarray[i].replace('\n','')
            elfcalories[elfcounter] = elfcalories[elfcounter] + int(inputarray[i])
        if maxelf <= elfcalories[elfcounter]:
            if topthreeelves[0] == elfcounter:
                maxelf = elfcalories[elfcounter]
            else:
                thirdelf = secondelf
                topthreeelves[2] = topthreeelves[1]
                secondelf = maxelf
                topthreeelves[1] = topthreeelves[0]
                maxelf = elfcalories[elfcounter]
                topthreeelves[0] = elfcounter
        elif secondelf <= elfcalories[elfcounter]:
            if topthreeelves[1] == elfcounter:
                secondelf = elfcalories[elfcounter]
            else:
                thirdelf = secondelf
                topthreeelves[2] = topthreeelves[1]
                secondelf = maxelf
                topthreeelves[1] = topthreeelves[0]
        elif thirdelf <= elfcalories[elfcounter]:
            thirdelf = elfcalories[elfcounter]
            topthreeelves[2] = elfcounter

    print(elfcalories)
    print(maxelf)
    print(topthreeelves)
    print(maxelf, secondelf, thirdelf)
    print(maxelf + secondelf + thirdelf)

    #print(f.readlines())
    #print(data)

