def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2):

    if sleep1>sleep2:
        a = sleep1
        posA = pos1
        jumpA = jump_distance1
        b = sleep2
        posB = pos2
        jumpB = jump_distance2
    else:
        a = sleep2
        posA = pos2
        jumpA = jump_distance2
        b = sleep1
        posB = pos1
        jumpB = jump_distance1

    if pos1 != pos2:
        for x in range(0, a) :
            