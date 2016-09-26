"""
Decode coded lists.

:Author: Egils Looga
:version: 0.0.0
:failed: ...
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
        wid = int(len(max(lines, key=len)))
        for i in range(len(lines)):
            if len(lines[i]) < wid:
                lines[i] = lines[i].ljust(wid)
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
    list1 = read_file(text)
    list2 = []
    tab = ''
    for x in range(len(max(list1, key=len))):
        for y in range(len(list1)):
            tab += list1[y][x]
        list2.append(tab)
        tab = ''

    return list2


def find_matching(original, transposed):
    """Find matching strings that exist in both lists.

    Keyword arguments:
    original -- original text as list of strings
    transposed -- transposed text as list of strings

    Returns:
    a list of strings that exist in both input lists.
    """
    original2 = []
    for i in range(len(original)):
        original[i] = original[i].split()
    for i in range(len(transposed)):
        transposed[i] = transposed[i].split()
    for i in range(len(original)):
            original2.extend(original[i])
    print(original2)
    transposed2 = []
    for i in range(len(transposed)):
            transposed2.extend(transposed[i])
    print(transposed2)
    match = list(set(transposed2).intersection(original2))
    for i in range(len(match)):
        try:
            if len(match[i]) < 2:
                match.pop(i)
        except IndexError:
            break
    return match

#print(read_file('secretagents.txt'))
#print(transpose('secretagents.txt'))

#original = read_file("secretagents.txt")
#print(find_matching(original, transpose(original)))
