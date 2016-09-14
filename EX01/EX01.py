from fractions import Fraction


def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2):
    if pos1 == pos2:
        a = pos1
    elif jump_distance1 / sleep1 > jump_distance2 / sleep2 and pos1 > pos2:
        a = -1
    elif jump_distance2 / sleep2 > jump_distance1 / sleep1 and pos2 > pos1:
        a = -1
    else:
        if pos1 > pos2:
            while pos1 != pos2:
                pos1 += Fraction(jump_distance1, sleep1)
                a = pos1
                pos2 += Fraction(jump_distance2, sleep2)
                if pos1 > pos2:
                    a = -1
        elif pos2 > pos1:
            while pos1 != pos2:
                pos1 += Fraction(jump_distance1, sleep1)
                a = pos1
                pos2 += Fraction(jump_distance2, sleep2)
                if pos2 > pos1:
                    a = -1
    return a

print(meet_me(1, 2, 1, 2, 1, 1))
print(meet_me(1, 2, 3, 4, 5, 5))
print(meet_me(10, 7, 7, 5, 8, 6))
print(meet_me(100, 7, 4, 300, 8, 6))
print(meet_me(1, 7, 1, 15, 5, 1))
