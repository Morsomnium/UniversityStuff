"""
Normalize and solve equations.

:Author: Egils Looga
:version: 2.1
:failed: all ;)
"""

import re
import math


def find_square(equation, eq_pos):
    """
    Function for finding squared part in equation.

    :param equation: where to find squared part
    :return: squared part and its position
    """
    #global square
    #global square_pos
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
    return square


def find_linear(equation, eq_pos):
    """
    Function for finding linear part in equation.

    :param equation: where to find linear part
    :return: linear part and its position
    """
    #global linear
    #global linear_pos
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
    return linear


def find_free(equation, eq_pos):
    """
    Function for finding free part in equation.

    :param equation: where to find free part
    :return: free part and its position
    """
    #global free
    #global free_pos
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
    return free


def space_insert(checked):
    """
    Function for space insertion.

    :param checked: input (square, linear, free)
    :return: input with space after sign
    """
    p = re.compile('(\+|-)')
    var1 = p.search(checked)
    if var1 is not None and checked[1] != ' ':
        checked = checked[0] + ' ' + checked[1:]
    return checked


def one_checker(checked):
    """
    Function for check on one multiplier.

    :param checked: input (square, linear)
    :return: input, but with 1 multiplier eliminated
    """
    d = re.compile('(\s|^)1x2?')
    if d.search(checked) is not None:
        if checked[0] == '-' or checked[0] == '+':
            checked = checked[:2] + checked[3:]
        else:
            checked = checked[1:]
    return checked


def zero_checker(checked):
    """
    Function for elimination 0 variables.

    :param checked: input (square, linear)
    :return: eliminates if 0 multiplier is present
    """
    try:
        if checked[0] == '0' or checked[2] == '0':
            checked = ''
    except IndexError:
        pass
    return checked


def side_swap(var1):
    """
    Function for swapping sides (around equation sign).

    :param var1: input (square, linear, free)
    :return: -(input)
    """
    if var1[0] != '-':
        if var1[0] == '+':
            var1 = '-' + var1[1:]
        else:
            var1 = '- ' + var1
    else:
        var1 = '+' + var1[1:]
    return var1


def xminus(square, linear, free):
    """
    Function for checking on positive square.

    :return: changes sign if square is negative
    """
    #global square
    #global linear
    #global free
    if square != '':
        if square[0] == '-':
            square = side_swap(square)
            if linear != '':
                linear = side_swap(linear)
            if free != '':
                free = side_swap(free)
    return square, linear, free


def space_check(equation):
    """
    Function for eliminating spare spaces.

    :param equation: main program input
    :return: equation with fixed spaces
    """
    for i in range(len(equation) - 1, 0, -1):
        if equation[i] == ' ' and equation[i + 1] == ' ':
            equation = equation[:i + 1] + equation[i + 2:]
    return equation


def solve_ready(square, linear, free):
    """
    Function for converting parts of equation in solve-ready state.

    :return: solve-ready multipliers
    """
    #global a
    #global b
    #global c
    print(square)
    print(linear)
    print(free)
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

    return a, b, c


def normalize_equation(equation):
    """
    Function for arranging parts of equation.

    :param equation: main program input
    :return: equation in user-friendly appearance
    """
    #global eq_pos
    eq_pos = re.search('=', equation).start()
    equation = ' ' + equation + ' '
    find_square(equation, eq_pos)
    find_linear(equation, eq_pos)
    find_free(equation, eq_pos)
    square, linear, free = xminus(find_square(equation, eq_pos), find_linear(equation, eq_pos), find_free(equation, eq_pos))
    equation = '{} {} {} = 0'.format(square, linear, free).strip()
    equation = space_check(equation)
    if equation[0] == '+':
        equation = equation[2:]
    return equation


def solve_equation(equation):
    """
    It slices, it dices and also solves equations!.

    :param equation: main program input
    :return: answer(s) for equation
    """
    eq_pos = re.search('=', equation).start()
    square, linear, free = xminus(find_square(equation, eq_pos), find_linear(equation, eq_pos), find_free(equation, eq_pos))
    a, b, c = solve_ready(square, linear, free)
    if a != 0:
        d = (b ** 2) - (4 * (a * c))
        if d < 0:
            answer = None
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
        answer = None
    return answer

testing = '1x2 + 0x - 4 = 0'
print(solve_equation(testing))
print(normalize_equation(testing))
