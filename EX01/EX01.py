"""
def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2):

    speed1 = jump_distance1/sleep1
    speed2 = jump_distance2/sleep2

    if (pos1>pos2 and speed1>speed2):
        a = -1
    elif (pos1==pos2):
        a = pos1
    else:
        pos1 += jump_distance1
        pos2 += jump_distance2
        sleepCount = 0
        if (sleep1>sleep2):
            for x in range(1, sleep1):
                if (sleep2<sleepCount):
                    sleepCount += 1
                else:
                    sleepCount +=1
                    pos2 += jump_distance2
        else:
            for x in range(0, sleep2):

    return a"""

def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2):
    if pos1 == pos2 :
        a = pos1
    elif jump_distance1/sleep1 > jump_distance2/sleep2 and pos1 > pos2 :
        a = -1
    elif jump_distance2/sleep2 > jump_distance1/sleep1 and pos2 > pos1 :
        a = -1
    else:
        for x in range (10) :
            pos1 += jump_distance1 / sleep1
            a = pos1
            pos2 += round(jump_distance2 / sleep2, 6)
            b = pos2
            print(a, b)

    return b

#print(meet_me(1, 7, 1, 15, 5, 1)) #50
#print(meet_me(1, 2, 1, 2, 1, 1)) #3
#print(meet_me(1, 2, 3, 4, 5, 5)) #-1
#print(meet_me(100, 7, 4, 300, 8, 6)) #940
print(meet_me(10, 7, 7, 5, 8, 6)) #25
#print(meet_me(1, 7, 1, 14, 5, 1))
