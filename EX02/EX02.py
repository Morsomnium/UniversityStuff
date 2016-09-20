"""
Normalize and solve equations.

:Author: Egils Looga
:version: 0.4
:failed: all ;)
"""


import re


def find_square(equation):
    global square
    global square_pos
    p = re.compile('([+-=])*\s*[1-9]?\d*(x2)')
    square = p.search(equation)
    if square is not None:
        square_pos = square.start(0)
        square = square.group().strip()
        if square[0] == '=':
            square = square[1:]
        if square_pos > eq_pos:
            if square[0] != '-':
                square = '-' + square[1:]
            else:
                square = '+' + square[1:]
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
        if linear[-1] == '+' or linear[-1] == '-' or linear[-1] == '=':
            linear = linear[:-1]
        if linear[0] == '=':
            linear = linear[1:]
        if linear_pos > eq_pos:
            if linear[0] != '-':
                linear = '-' + linear[1:]
            else:
                linear = '+' + linear[1:]
    else:
        linear = ''
        linear_pos = 0
    return linear, linear_pos


def find_free(equation):
    p = re.compile('(\+|-)(\W|\s)?[1-9](\d+)?(\W|$|\s)')
    free = p.search(equation)
    if free is not None:
        free_pos = free.start()
        free = free.group().strip()
        if free[-1] == '+' or free[-1] == '-' or free[-1] == '=':
            free = free[:-1]
        if free[0] == '=':
            free = free[1:]
    else:
        free = ''
        free_pos = 0
    return free, free_pos


def space_insert(checked):
    p = re.compile('(\+|-)\s')
    var1 = p.search(checked)
    if var1 is None and len(checked) > 0 and(checked[0] == '+' or checked[0] == '-'):
        checked = checked[0] + ' ' + checked[1:]
    return checked


def one_checker(checked):
    d = re.compile('1(x2|x)')
    if d.search(checked) is not None and(d.search(checked).group()[:-1] == '1' or d.search(checked).group()[:-2] == '1'):
        if checked[0] == '-' or checked[0] == '+':
            checked = checked[:2] + checked[3:]
        else:
            checked = checked[1:]
    return checked


def normalize_equation(equation):
    global eq_pos
    eq_pos = re.search('=', equation).start()
    equation = ' ' + equation + ' '
    square = one_checker(space_insert(find_square(equation)[0]))
    linear = one_checker(space_insert(find_linear(equation)[0]))
    free = space_insert(find_free(equation)[0])
    equation = '{} {} {} = 0'.format(square, linear, free).strip()
    print('square:', square)
    print('linear:', linear, len(linear))
    print('free:', free)
    return equation

print(normalize_equation("- 3 =4864648464x2 + 15151x"))
# print(normalize_equation("2x2 + 2x = 3"))
# print(normalize_equation("x2 + 2x = 3"))  # "x2 + 2x - 3 = 0"
# print(normalize_equation("0 = 3 + 1x2"))  # "x2 + 3 = 0"
# print(normalize_equation("2x + 2 = 2x2"))  # "2x2 - 2x - 2 = 0"


def solve_equation(equation):
    return
