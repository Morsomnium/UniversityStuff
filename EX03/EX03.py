"""
Decode coded lists.

:Author: Egils Looga
:version: 1.8.1
:failed: not_square
"""


def read_file(filename):
    """Read file contents into a list of strings.

    Keyword arguments:
    filename -- the filename as string from where to read data

    Returns:
    the contents of the file as a list of strings.
    For example,
    ["first line", "second line", "third line"]
    """
    with open(filename, 'r') as f:
        lines = []
        for line in f:
            if line[-1] == '\n':
                lines.append(line[:-1])
            else:
                lines.append(line)
    return lines


def transpose(text):
    """Change rows into columns.

    Keyword arguments:
    text -- a list of strings (each row is a string)

    Returns:
    a list of string that is transposed (each row has been turned into column)
    For example:
    ["AAA", "BBB", "CCC"] => ["ABC", "ABC", "ABC"]
    or ["AA", "B", "C"] => ["ABC", "A"]
    or ["A", "B", "CC"] => ["ABC", "  C"]
    """
    # YOUR SOLUTION HERE
    wid = int(len(max(text, key=len)))
    for i in range(len(text)):
        if len(text[i]) < wid:
            text[i] = text[i].ljust(wid)
    list1 = text
    list2 = []
    tab = ''
    for x in range(len(max(list1, key=len))):
        for y in range(len(list1)):
            tab += list1[y][x]
        list2.append(tab)
        tab = ''
    print('list2:', list2)
    for i in range(len(list2)):
        while list2[i][-1] == ' ':
            list2[i] = list2[i][:-1]
    return list2


def magic_touch(thing):
    """
    Word separator.

    :param thing: input
    :return: output after touch
    """
    another_thing = []
    for i in range(len(thing)):
        thing[i] = thing[i].split()
        another_thing.extend(thing[i])
    return another_thing


def find_matching(original, transposed):
    """Find matching strings that exist in both lists.

    Keyword arguments:
    original -- original text as list of strings
    transposed -- transposed text as list of strings

    Returns:
    a list of strings that exist in both input lists.
    """
    result = []
    wid = int(len(max(original, key=len)))
    for i in range(len(original)):
        if len(original[i]) < wid:
            original[i] = original[i].ljust(wid)
    original = magic_touch(original)
    transposed = magic_touch(transposed)
    """
    for i in range(len(original)):
        original[i] = original[i].split()
        original2.extend(original[i])
    for i in range(len(transposed)):
        transposed[i] = transposed[i].split()
        transposed2.extend(transposed[i])"""
    # print('orig2:', original2)
    # print('orig:', original)
    # print('trans2:', transposed2)
    match = list(set(transposed).intersection(original))
    for i in range(len(original) - 1, 0, -1):
        if original[i] not in match:
            original.pop(i)
    for i in range(len(original) - 1, 0, -1):
        if len(original[i]) < 2:
            original.pop(i)
    for i in range(len(original)):
        if i % 2 == 1:
            result.append(original[i - 1] + ' ' + original[i])
    return result

# print('read file:', read_file('secretagents.txt'))
# print(transpose(read_file('secretagents.txt')))

# original = read_file("secretagents.txt")
# print(find_matching(original, transpose(original)))
