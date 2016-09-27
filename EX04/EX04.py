"""
Game : The Wheel of Fortune.

:Author: Egils Looga
:version: 0.0.0
:failed: ....
"""
import collections
import random
from heapq import nlargest

def read_words(filename):
    """
    Read file and return dictionary
    where keys represent words
    and values represent the count of the given word.

    Each word is on a separate line.
    :param filename: File to read
    :return: Dictionary of word counts
    """

    with open(filename, 'r') as f:
        return collections.Counter(f.read().lower().split())


def guess(sentence, guessed_letters, word_dict):
    """
    Offer the letter which would most probably
    give the best result.

    :param sentence: Sentence to be guessed.
    :param guessed_letters: A list of already guessed letters
    (both revealed and not existing letters).
    :param word_dict: A dictionary of words and their counts.
    Use the output from read_words.
    :return: The letter with the best probability.
    """



    return 't'


def the_game(filename, word_count):
    d = read_words(filename)
    c = collections.Counter(d)
    dictionary_size = sum(c.values())
    correct_sentence = " ".join([x for _, x in nlargest(word_count, ((random.random(), x) for x in c.elements()))])
    sentence = "".join([x if x == ' ' else '_' for x in correct_sentence])
    guessed_letters = []
    print("Correct sentence: " + correct_sentence)
    print(sentence)
    cnt = 0
    while True:
        guessed_letter = guess(sentence, guessed_letters, d)
        if guessed_letter is None or guessed_letter in guessed_letters:
            print("Nothing to guess any more, breaking.")
            break
        print('guessed:' + guessed_letter)
        guessed_letters.append(guessed_letter)
        sentence = "".join([c if c == guessed_letter else sentence[i] for i, c in enumerate(correct_sentence)])
        print("Sentence: " + sentence)
        cnt += 1
        if '_' not in sentence:
            print("Congrats! Number of guesses:" + str(cnt))
            break

c = read_words('EX04.txt')
print(list(c))