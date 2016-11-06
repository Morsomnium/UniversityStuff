"""Sentence generator."""
from itertools import cycle


class SentenceGenerator:

    def __init__(self, rules_string):
        rules1 = {}
        rule_rows = rules_string.split('\n')
        for row in rule_rows:
            row = row.split()
            rule = row[0]
            row = ''.join(row[2:])
            words = row.split('|')
            rules1[rule] = cycle(words)
        self.rules = rules1

    def sentence_generator(self, syntax=''):
        while syntax != '':
            yield next(self.rules[syntax])
        else:
            while True:
                yield next(cycle(['']))

a = SentenceGenerator('x = b | x | j | a \n z = f | g | h')
b = a.sentence_generator('')
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
