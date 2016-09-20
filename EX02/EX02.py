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
    p = re.compile('(\+|-|=)?\s*[1-9]?\d*(x2)')
    square = p.search(equation)
    if square is not None:
        square_pos = square.start(0)
        square = square.group().strip()
        if square[-1] == '+' or square[-1] == '-' or square[-1] == '=':
            square = square[:-1].strip()
        if square[0] == '=':
            square = square[1:].strip()
        square = one_checker(space_insert(square).strip())
        if square_pos > eq_pos:
            square = side_swap(square)
    else:
        square = ''
        square_pos = 0
    return square, square_pos


def find_linear(equation):
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
        linear = one_checker(space_insert(linear).strip())
        if linear_pos > eq_pos:
            linear = side_swap(linear)
    else:
        linear = ''
        linear_pos = 0


def find_free(equation):
    global free
    global free_pos
    p = re.compile('(\+|-)?(\W|\s)?[^x][1-9](\d+)?[^x]')
    free = p.search(equation)
    if free is not None:
        free_pos = free.start()
        free = free.group().strip()
        print(free, '++22++')
        if free[-1] == '+' or free[-1] == '-' or free[-1] == '=':
            free = free[:-1].strip()
        if free[0] == '=':
            free = free[1:].strip()
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
    print(checked)
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
    print(square[0])
    if square[0] == '-':
        square = side_swap(square)
        if linear != '':
            linear = side_swap(linear)
        if free != '':
            free = side_swap(free)
    return square, linear, free


def normalize_equation(equation):
    global eq_pos
    eq_pos = re.search('=', equation).start()
    equation = ' ' + equation + ' '
    find_square(equation)
    find_linear(equation)
    find_free(equation)
    xminus()
    equation = '{} {} {} = 0'.format(square, linear, free).strip()
    if equation[0] == '+':
        equation = equation[2:]
    print('square:', square)
    print('linear:', linear, len(linear))
    print('free:', free)
    return equation

# print(normalize_equation("x2 + 2x = 3"))  # "x2 + 2x - 3 = 0"
print(normalize_equation("0 = 3 + 1x2"))  # "x2 + 3 = 0"
# print(normalize_equation("2x + 2 = 2x2"))  # "2x2 - 2x - 2 = 0"


def solve_equation(equation):
    return
