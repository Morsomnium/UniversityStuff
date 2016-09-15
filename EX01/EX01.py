"""
Tracks two bunnies as they jump.

:Author: Egils Looga.
:version: 4.0.
:failed: test_cant_catch_me.
"""
from fractions import Fraction


def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2):
    """
    Do all what you need.

    :param pos1: Start position of first bunny.
    :param jump_distance1: How long is no1s jump.
    :param sleep1: no1 jump cooldown.
    :param pos2: Start position of second bunny.
    :param jump_distance2: How long is no2s jump.
    :param sleep2: no2 jump cooldown.
    :return: its a but technically its pos1 or pos2
    """
    if pos1 == pos2:
        a = pos1
    elif (jump_distance1 / sleep1 > jump_distance2 / sleep2 and pos1 > pos2) or (jump_distance2 / sleep2 > jump_distance1 / sleep1 and pos2 > pos1):
        a = -1
    elif jump_distance1 / sleep1 == jump_distance2 / sleep2:
        a = -1
    else:
        if pos1 > pos2:
            while pos1 != pos2:
                pos1 += Fraction(jump_distance1, sleep1)
                a = pos1
                pos2 += Fraction(jump_distance2, sleep2)
                if pos2 > pos1:
                    a = -1
                    break
        elif pos2 > pos1:
            while pos1 != pos2:
                pos1 += Fraction(jump_distance1, sleep1)
                a = pos1
                pos2 += Fraction(jump_distance2, sleep2)
                if pos1 > pos2:
                    a = -1
                    break
    return a


print(meet_me(1, 15, 6, 5, 0, 3)) # -1
print(meet_me(1, 2, 1, 2, 1, 1)) # 3
print(meet_me(1, 2, 3, 4, 5, 5)) # -1
print(meet_me(10, 7, 7, 5, 8, 6)) # 25
print(meet_me(100, 7, 4, 300, 8, 6)) # 940
print(meet_me(1, 7, 1, 15, 5, 1)) # 50
print(meet_me(0, 7, 3, 3, 5, 2)) # -1
print(meet_me(0, 5, 1, 1, 5, 1)) # -1
print(meet_me(0, 6, 3, 3, 8, 4)) # -1