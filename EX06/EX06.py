"""
Map-drawer.

:Author: Egils Looga
:version: 0.0
:failed:
"""


def craft_map(course, views):
    """
    Create a map from the moves and the associated views.

    :param course: where to head
    :param views: what to see
    :return: drawn map
    """
    print(len(course), len(views))
    head = {'NE': [1, 1], 'E': [1, 0], 'SE': [1, -1], 'S': [0, -1], 'SW': [-1, -1], 'W': [-1, 0], 'NW': [-1, 1],
            'N': [0, 1]}
    maps = {}
    posx, posy = 0, 0
    for x in views:
        for y in x:
            for n, z in enumerate(y):
                if z == '8' or z == '0':
                    y[n] = ' '
    for n, i in enumerate(course):
        posx += head[i][0]
        posy += head[i][1]
        maps[posx, posy] = views[n][1][1]
        maps[posx - 1, posy] = views[n][1][0]
        maps[posx + 1, posy] = views[n][1][2]
        maps[posx, posy - 1] = views[n][2][1]
        maps[posx, posy + 1] = views[n][0][1]
        maps[posx - 1, posy + 1] = views[n][0][0]
        maps[posx - 1, posy - 1] = views[n][2][0]
        maps[posx + 1, posy + 1] = views[n][0][2]
        maps[posx + 1, posy - 1] = views[n][2][2]
        print(posx, posy)
    width = sorted(maps, reverse=True)[0][0] - sorted(maps)[0][0]
    height = sorted(maps, reverse=True, key=lambda coord: coord[1])[0][1] - sorted(maps, key=lambda coord: coord[1])[0][1]
    rev_map = [['' for j in range(width + 1)] for i in range(height + 1)]
    for n, row in enumerate(rev_map):
        print(rev_map[n])
    print(len(rev_map), len(rev_map[0]))
    print(width, height)
    print(sorted(maps))
    print(sorted(maps, key=lambda coord: coord[1]))
    for key in sorted(maps):
        #print(key)
        rev_map[key[1] - sorted(maps, key=lambda coord: coord[1])[0][1]][key[0] - sorted(maps)[0][0]] = maps[key]
    for x in rev_map:
        for n, y in enumerate(x):
            if y == '':
                x[n] = '?'
    for n, row in enumerate(rev_map):
        print(rev_map[n])
    right_map = []
    for i in range(len(rev_map) - 1, -1, -1):
        right_map.append(rev_map[i])
    print('')
    for m, x in enumerate(right_map):
        for n, y in enumerate(x):
            if y == ' ' and m % 2 == 0 and n % 2 == 0:
                x[n] = '~'
            elif y == ' ' and m % 2 == 1 and n % 2 == 1:
                x[n] = '~'
            elif y == ' ' and m % 2 == 0 and n % 2 == 1:
                x[n] = '-'
            elif y == ' ' and m % 2 == 1 and n % 2 == 0:
                x[n] = '-'
    for n, row in enumerate(right_map):
        print(right_map[n])
    for i in range(len(right_map)):
        right_map[i] = ''.join(right_map[i])

    str_map = ''
    str_map = '\n'.join(right_map)
    print(str_map, '123')

    return str_map


"""craft_map(["NE", "E", "W", "SW", "N", "N", "N", "N", "N", "NE", "NE", "E", "E", "E", "E",
           "SE", "SE", "SE", "S", "S", "SW", "SW", "W", "W", "W", "W", "W"],
          [[[' ', ' ', 'x'], [' ', '0', ' '], [' ', ' ', ' ']],
           [[' ', 'x', '.'], [' ', '0', 'x'], [' ', ' ', ' ']],
           [[' ', ' ', 'x'], [' ', '0', ' '], [' ', ' ', ' ']],
           [[' ', ' ', ' '], [' ', '0', ' '], [' ', ' ', ' ']],
           [[' ', ' ', ' '], [' ', '0', ' '], [' ', ' ', ' ']],
           [[' ', ' ', 'x'], [' ', '0', ' '], [' ', ' ', ' ']],
           [[' ', ' ', ' '], [' ', '0', 'x'], [' ', ' ', ' ']],
           [[' ', ' ', ' '], [' ', '0', ' '], [' ', ' ', 'x']],
           [[' ', ' ', ' '], [' ', '0', ' '], [' ', ' ', ' ']],
           [[' ', ' ', ' '], [' ', '0', ' '], [' ', ' ', ' ']],
           [[' ', ' ', ' '], [' ', '0', ' '], [' ', ' ', ' ']],
           [[' ', ' ', ' '], [' ', '0', ' '], [' ', ' ', 'x']],
           [[' ', ' ', ' '], [' ', '0', ' '], [' ', 'x', 'x']],
           [[' ', ' ', ' '], [' ', '0', ' '], ['x', 'x', ' ']],
           [[' ', ' ', ' '], [' ', '0', ' '], ['x', ' ', ' ']],
           [[' ', ' ', ' '], [' ', '0', ' '], ['x', ' ', ' ']],
           [[' ', ' ', ' '], [' ', '0', ' '], ['x', ' ', ' ']],
           [[' ', ' ', ' '], [' ', '0', ' '], ['X', ' ', ' ']],
           [[' ', ' ', ' '], ['X', '0', ' '], [' ', ' ', ' ']],
           [['X', ' ', ' '], [' ', '0', ' '], [' ', ' ', ' ']],
           [['x', ' ', ' '], [' ', '0', ' '], [' ', ' ', ' ']],
           [['x', ' ', ' '], [' ', '0', ' '], [' ', ' ', ' ']],
           [['x', 'x', ' '], [' ', '0', ' '], [' ', ' ', ' ']],
           [['X', 'x', 'x'], [' ', '0', ' '], [' ', ' ', ' ']],
           [['x', 'X', 'x'], [' ', '0', ' '], [' ', ' ', ' ']],
           [[' ', 'x', 'X'], [' ', '0', ' '], [' ', ' ', ' ']],
           [[' ', ' ', 'x'], [' ', '0', ' '], [' ', ' ', ' ']]])"""
