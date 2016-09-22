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
        print(lines[3], len(lines[3]))
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
    return ["No, mr Bond, I expect you to die!"]


def find_matching(original, transposed):
    """Find matching strings that exist in both lists.

    Keyword arguments:
    original -- original text as list of strings
    transposed -- transposed text as list of strings

    Returns:
    a list of strings that exist in both input lists.
    """
    # YOUR CODE HERE
    return []


read_file('secretagents.txt')
print(read_file('secretagents.txt'))