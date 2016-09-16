"""
Normalize and solve equations.

:Author: Egils Looga
:version: 0.1.
:failed: none
"""


def normalize_equation(equation):
    equation = ' ' + equation + ' '
    for i in range(len(equation)):
        if equation[i] == "=":
            eqPos = i
        if equation[i] == 'x' and equation[i+1] == '2':
            if equation[i-1].isspace() is False and equation[i-1].isdigit() and equation[i-2:i] != ' 1':
                x = 1
                while equation[i-x].isdigit():
                    square = equation[i-x:i+2]
                    x += 1
                print('square', square)
            else:
                square = equation[i:i+2]
                print(square)
        """left_side = equation[0: i]
            right_side = equation[i+1:len(equation)+1]
            equation = right_side + '=' + left_side
            print(left_side, right_side) """
        if equation[i].isdigit() and equation[i-1].isalpha() is False and equation[i+1].isalpha() is False:
            x = 1
            while equation[i-1].isdigit() is False and equation[i+x].isdigit():
                free = equation[i:i + x + 1]
                x += 1
                if equation[i+x].isalpha():
                    free = ''
                    break
                print('digit',free)
        if equation[i] == 'x' and equation[i+1].isdigit() is False:
            x = 1
            while equation[i-x].isdigit():
                linear = equation[i-x:i+1]

        # print(i)
    """square = '2'
    linear = '3'
    free = '4'"""
    equation = '{} {} {} = 0'.format(square, linear, free)

    return equation

print(normalize_equation("11x2 323 "))
#print(normalize_equation("2x2 + 2x = 3"))
#print(normalize_equation("x2 + 2x = 3"))  # "x2 + 2x - 3 = 0"
#print(normalize_equation("0 = 3 + 1x2"))  # "x2 + 3 = 0"
#print(normalize_equation("2x + 2 = 2x2"))  # "2x2 - 2x - 2 = 0"

def solve_equation(equation):
    return