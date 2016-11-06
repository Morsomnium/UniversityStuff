"""Sentence generator."""
#from itertools import cycle


def cyc(lis):
    while True:
        for i in lis:
            yield i


class SentenceGenerator:

    def __init__(self, rules_string):
        rules = {}
        rule_rows = rules_string.split('\n')
        for row in rule_rows:
            rule_name, row = row.split(' = ')
            row = [i for i in row.split() if i != '|']
            rules[rule_name.strip()] = row
        self.rules = rules
        #print(type(self.rules['x']))

    def sentence_generator(self, syntax=''):
        temp_iter = cyc(self.rules[syntax])
        while True:
            yield next(temp_iter)
        else:
            while True:
                yield ''

"""a = SentenceGenerator('x = b | x | j | a \n z = f | g | h')
b = a.sentence_generator('x')
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
"""