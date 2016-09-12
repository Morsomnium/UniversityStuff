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
        count = 0
        pos1 += jump_distance1
        pos2 += jump_distance2
        if pos1 > pos2:
            while pos1 != pos2 and pos1 > pos2:
                count += 1
                if count % sleep1:
                    pos1 += jump_distance1
                elif count % sleep2:
                    pos2 += jump_distance2
            else:
                if pos1 > pos2 :
                    a = -1
                else:
                    a = pos1
        else:
            while pos1 != pos2 and pos2 > pos1:
                count += 1
                if count % sleep1:
                    pos1 += jump_distance1
                elif count % sleep2:
                    pos2 += jump_distance2
            else:
                if pos2 > pos1:
                    a = -1
                else:
                    a = pos1

    return a

print(meet_me(1, 7, 1, 14, 5, 1))
