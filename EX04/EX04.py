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
    words = read_words(word_dict)
    pass_list = []
    sentence = sentence.split()
    for x in range(len(sentence)):
        for i in range(len(words)):
            if len(list(words)[i]) == len(sentence[i]):
                pass_list.extend(list(words)[i])

    return 't'

#c = read_words('EX04.txt')
#print(list(c))