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
            rules[rule_name.strip()] = cyc(row)
        self.rules = rules
        print(self.rules)

    def sentence_generator(self, syntax=''):
        syntax = syntax.split()
        if len(syntax) != 0:
            while True:
                gen = ''
                for word in syntax:
                    gen += str(next(self.rules[word])) + ' '
                yield gen
        else:
            while True:
                yield ''

if __name__ == "__main__":
    a = SentenceGenerator('x = b | x | j | a \n z = f | g | h')
    b = a.sentence_generator('x z')
    print(next(b))
    print(next(b))
    print(next(b))
    print(next(b))
    print(next(b))
    print(next(b))
    print(next(b))
    print(next(b))
