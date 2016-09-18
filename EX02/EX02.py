"""
Normalize and solve equations.

:Author: Egils Looga
:version: 0.3
:failed: all ;)
"""


import re
from string import Template


def find_square(equation):
    p = re.compile('[+-=]\s*\d*x2\s*')
    square = p.search(equation)
    if square is not None:
        square_pos = square.start(0)
        square = square.group().strip()
    else:
        square = ''
        square_pos = 0
    return square, square_pos

def find_linear(equation):
    p = re.compile('[+-=]\s*\d*x[^2]')
    linear = p.search(equation)
    if linear is not None:
        linear_pos = linear.start(0)
        linear = linear.group().strip()
    else:
        linear = ''
        linear_pos = 0
    return linear, linear_pos

def find_free(equation):
    p = re.compile('[+-=]\s*[^x]\d+\s*')
    free = p.search(equation)
    if free is not None:
        free_pos = free.start()
        free = free.group().strip()
    else:
        free = ''
        free_pos = 0
    return free, free_pos

def normalize_equation(equation):
    equation = ' ' + equation + ' '
    find_free(equation)
    find_linear(equation)
    find_square(equation)
    equation = '{} {} {} = 0'.format(find_square(equation)[0], find_linear(equation)[0], find_free(equation)[0])
    print('square:' , find_square(equation)[0])
    print('linear:', find_linear(equation)[0])
    print('free:', find_free(equation)[0])
    return equation

print(normalize_equation("13x2+65656x - 37378=0"))
# print(normalize_equation("2x2 + 2x = 3"))
# print(normalize_equation("x2 + 2x = 3"))  # "x2 + 2x - 3 = 0"
# print(normalize_equation("0 = 3 + 1x2"))  # "x2 + 3 = 0"
# print(normalize_equation("2x + 2 = 2x2"))  # "2x2 - 2x - 2 = 0"


def solve_equation(equation):
    return


    """equation = ' ' + equation + ' '
    for i in range(len(equation)):
        if equation[i] == "=":
            eqPos = i
        if equation[i] == 'x' and equation[i + 1] == '2':
            if equation[i - 1].isspace() is False and equation[i - 1].isdigit() and equation[i - 2:i] != ' 1':
                x = 1
                while equation[i - x].isdigit():
                    square = equation[i - x:i + 2]
                    x += 1
                print('square', square)
            else:
                square = equation[i:i + 2]
                print(square)
        if equation[i].isdigit() and equation[i - 1].isalpha() is False and equation[i + 1].isalpha() is False:
            x = 1
            while equation[i - 1].isdigit() is False and equation[i + x].isdigit():
                free = equation[i:i + x + 1]
                x += 1
                if equation[i + x].isalpha():
                    free = ''
                    break
                print('digit', free)
        if equation[i] == 'x' and equation[i + 1].isdigit() is False:
            x = 1
            while equation[i - x].isdigit():
                linear = equation[i - x:i + 1]

        # print(i)
    """'4'"""
    equation = Template('$squ $fre')
    equation = equation.substitute(squ=square, fre=free)
"""