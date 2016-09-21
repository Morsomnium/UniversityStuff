"""
Normalize and solve equations.

:Author: Egils Looga
:version: 1.1.1
:failed: all ;)
"""

import re
import math


def find_square(equation):
    """
    Function for finding squared part in equation.

    :param equation: where to find squared part
    :return: squared part and its position
    """
    global square
    global square_pos
    p = re.compile('(\+|-|=)?\s*[1-9]?\d*(x2)(\+|-|=|\s)')
    square = p.search(equation)
    if square is not None:
        square_pos = square.start(0)
        square = square.group().strip()
        if square[-1] == '+' or square[-1] == '-' or square[-1] == '=':
            square = square[:-1].strip()
        if square[0] == '=':
            square = square[1:].strip()
        if square[0] != '-' and square[0] != '+':
            square = '+' + square
        square = one_checker(space_insert(square).strip())
        if square_pos > eq_pos:
            square = side_swap(square)
        square = zero_checker(square)
    else:
        square = ''
        square_pos = 0
    return square, square_pos


def find_linear(equation):
    """
    Function for finding linear part in equation.

    :param equation: where to find linear part
    :return: linear part and its position
    """
    global linear
    global linear_pos
    p = re.compile('(\+|-|=)?\s*\d*x[^2]')
    linear = p.search(equation)
    if linear is not None:
        linear_pos = linear.start(0)
        linear = linear.group().strip()
        if linear[-1] == '+' or linear[-1] == '-' or linear[-1] == '=':
            linear = linear[:-1].strip()
        if linear[0] == '=':
            linear = linear[1:].strip()
        if linear[0] != '-' and linear[0] != '+':
            linear = '+' + linear
        linear = one_checker(space_insert(linear).strip())
        if linear_pos > eq_pos:
            linear = side_swap(linear)
        linear = zero_checker(linear)
    else:
        linear = ''
        linear_pos = 0


def find_free(equation):
    """
    Function for finding free part in equation.

    :param equation: where to find free part
    :return: free part and its position
    """
    global free
    global free_pos
    p = re.compile('(\+|-)?(\W|\s)?(^x|=|\+|-|\s|^)[1-9](\d+)?(^x|=|\+|-|\s|$)')
    free = p.search(equation)
    if free is not None:
        free_pos = free.start()
        free = free.group().strip()
        if free[-1] == '+' or free[-1] == '-' or free[-1] == '=':
            free = free[:-1].strip()
        if free[0] == '=':
            free = free[1:].strip()
        if free[0] != '-' and free[0] != '+':
            free = '+' + free
        free = space_insert(free)
        if free_pos > eq_pos:
            free = side_swap(free)
        free = free.strip()
    else:
        free = ''
        free_pos = 0


def space_insert(checked):
    p = re.compile('(\+|-)')
    var1 = p.search(checked)
    if var1 is not None and checked[1] != ' ':
        checked = checked[0] + ' ' + checked[1:]
    return checked


def one_checker(checked):
    d = re.compile('(\s|^)1x2?')
    if d.search(checked) is not None:
        if checked[0] == '-' or checked[0] == '+':
            checked = checked[:2] + checked[3:]
        else:
            checked = checked[1:]
    return checked


def zero_checker(checked):
    try:
        if checked[0] == '0' or checked[2] == '0':
            checked = ''
    except IndexError:
        pass
    return checked


def side_swap(var1):
    if var1[0] != '-':
        if var1[0] == '+':
            var1 = '-' + var1[1:]
        else:
            var1 = '- ' + var1
    else:
        var1 = '+' + var1[1:]
    return var1


def xminus():
    global square
    global linear
    global free
    if square != '':
        if square[0] == '-':
            square = side_swap(square)
            if linear != '':
                linear = side_swap(linear)
            if free != '':
                free = side_swap(free)
    return square, linear, free


def space_check(equation):
    for i in range(len(equation) - 1, 0, -1):
        if equation[i] == ' ' and equation[i + 1] == ' ':
            equation = equation[:i + 1] + equation[i + 2:]
    return equation


def solve_ready():
    global a
    global b
    global c
    if square != '':
        if square[2] == 'x':
            a = 1
        elif square[0] == '-':
            a = int(square[0] + square[2:-2])
        else:
            a = int(square[2:-2])
    else:
        a = 0
    if linear != '':
        if linear[2] == 'x':
            b = 1
        elif linear[0] == '-':
            b = int(linear[0] + linear[2:-1])
        else:
            b = int(linear[2:-1])
    else:
        b = 0
    if free == '':
        c = 0
    else:
        c = int(free[0] + free[2:])

    return


def normalize_equation(equation):
    global eq_pos
    eq_pos = re.search('=', equation).start()
    equation = ' ' + equation + ' '
    find_square(equation)
    find_linear(equation)
    find_free(equation)
    xminus()
    equation = '{} {} {} = 0'.format(square, linear, free).strip()
    equation = space_check(equation)
    if equation[0] == '+':
        equation = equation[2:]
    print('square:', square)
    print('linear:', linear, len(linear))
    print('free:', free)
    return equation


print(normalize_equation("2x + x2 - 3 = 0"))  # "x2 + 2x - 3 = 0"


# print(normalize_equation("0 = 3 + 1x2"))  # "x2 + 3 = 0"
# print(normalize_equation("2x + 2 = 2x2"))  # "2x2 - 2x - 2 = 0"


def solve_equation(equation):
    equation = normalize_equation(equation)
    solve_ready()
    print(a, b, c)
    if a != 0:
        d = (b ** 2) - (4 * (a * c))
        if d < 0:
            answer = 'None'
        elif d == 0:
            x1 = -b / (2 * a)
            answer = 'x = ' + repr(round(x1, 2))
        else:
            x1 = ((-b + math.sqrt(d)) / (2 * a))
            x2 = ((-b - math.sqrt(d)) / (2 * a))
            if x2 > x1:
                answer = 'x1 = ' + repr(round(x1, 2)) + ', x2 = ' + repr(round(x2, 2))
            elif x1 > x2:
                answer = 'x1 = ' + repr(round(x2, 2)) + ', x2 = ' + repr(round(x1, 2))
    elif b != 0:
        answer = 'x = ' + repr((c / (-b)))
    else:
        answer = 'None'
    return answer


print(solve_equation("9x2 -12x +4 = 0"))
