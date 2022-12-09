import os
import sys
import string
import heapq

def generatepriority():
    h = []
    priority = 1
    for i in string.ascii_lowercase:
        heapq.heappush(h, (priority, i))
        priority += 1
    for j in string.ascii_uppercase:
        heapq.heappush(h, (priority, j))
        priority += 1   

    return h

#Part 1 solution for day 3
with open(os.path.join(sys.path[0], "day3input.txt"), 'r') as f:
    input = f.readlines()
    priorityheap = generatepriority()
    priority = 0
    for i in range(len(input)):
        input[i] = input[i].replace('\n','')
        firstcomp = input[i][0:(int(len(input[i])/2))]
        secondcomp = input[i][(int(len(input[i])/2)):]
        commonitem = ''
        kvalue = 0
        for j in firstcomp:
            if j in secondcomp:
                commonitem = j
                break
        for k in priorityheap:
            if commonitem == k[1]:
                priority += k[0]
                break
        print(firstcomp, secondcomp, commonitem, priority)    
    print(priority)

#Part 2 solution for day 2
    badgesum = 0
    for x in range(0, len(input), 3):
        badge = ''
        potentialbadgetypes = []
        for y in input[x]:
            if y in input[x+1]:
                potentialbadgetypes.append(y)
        for z in potentialbadgetypes:
            if z in input[x+2]:
                badge = z
                for aa in priorityheap:
                    if z == aa[1]:
                        badgesum += aa[0]
                        break
                break
    print(badgesum)

