"""
Tracks two bunnies as they jump.

:Author: Egils Looga.
:version: 4.3.
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
        return pos1
    elif (jump_distance1 / sleep1 > jump_distance2 / sleep2 and pos1 > pos2) or (jump_distance2 / sleep2 > jump_distance1 / sleep1 and pos2 > pos1):
        pos1 = -1
    elif jump_distance1 / sleep1 == jump_distance2 / sleep2:
        pos1 = -1
    else:
        if pos1 > pos2:
            while pos1 != pos2:
                pos1 += Fraction(jump_distance1, sleep1)
                pos2 += Fraction(jump_distance2, sleep2)
                if pos2 > pos1:
                    pos1 = -1
                    break
        elif pos2 > pos1:
            while pos1 != pos2:
                pos1 += Fraction(jump_distance1, sleep1)
                pos2 += Fraction(jump_distance2, sleep2)
                if pos1 > pos2:
                    pos1 = -1
                    break
    return pos1

print(meet_me(0, 15, 6, 5, 0, 3))
