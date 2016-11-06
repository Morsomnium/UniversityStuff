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

    def sentence_generator(self, syntax):
        while True:
            yield next(self.rules[syntax])

"""a = SentenceGenerator('x = b | c | d | e \n z = f | g | h')
b = a.sentence_generator('x')
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))"""
