"""
Game : The Wheel of Fortune.

:Author: Egils Looga
:version: 1.2
:failed: ....
"""
import collections


def read_words(filename):
    """
    Read file and return dictionary where keys represent words and values represent the count of the given word.

    Each word is on a separate line.
    :param filename: File to read
    :return: Dictionary of word counts
    """
    with open(filename, 'r') as f:
        return collections.Counter(f.read().lower().split())


def guess(sentence, guessed_letters, word_dict):
    """
    Offer the letter which would most probably give the best result.

    :param sentence: Sentence to be guessed.
    :param guessed_letters: A list of already guessed letters
    (both revealed and not existing letters).
    :param word_dict: A dictionary of words and their counts.
    Use the output from read_words.
    :return: The letter with the best probability.
    """
    pass_list = {}
    letter_list = collections.Counter()
    sentence = sentence.split()
    for i in range(len(sentence)):
        for word in word_dict:
            if len(sentence[i]) == len(word):
                pass_list[word] = word_dict.get(word)
    for word in pass_list:
        for letter in word:
            letter_list[letter] += 1 * word_dict.get(word)
    for letter in guessed_letters:
        if letter in letter_list:
            del letter_list[letter]

    try:
        return letter_list.most_common(1)[0][0]
    except IndexError:
        return

#c = read_words('EX04.txt')
#print(guess('', [], c))