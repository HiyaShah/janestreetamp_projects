#!/usr/bin/env python3

from random import choice

class WordList():
    """A list of words. Typically the remaining possible solutions"""

    def __init__(self, word_file = "possible_words.txt", given_words = None):
        """construct a list of words by reading from `word_file`

        If `given_words` is None, read words from `word_file`, otherwise
        populate `self.words` with `given_words` If no `word_file` parameter is
        given, read from "possible_words.txt"

        """
        if given_words is None:
            self.words = []
            with open(f"{word_file}") as fp:
                self.words = fp.readlines()
            self.words = [w.strip() for w in self.words]
        else:
            self.words = given_words

    def get_random_word(self):
        """returns a random word from the set of words"""
        return choice(self.words)

    def __str__(self):
        return str(self.words)

    def __contains__(self, word):
        return word in self.words

    def __iter__(self):
        return self.words.__iter__()

    def __len__(self):
        return len(self.words)

    def refine(self, information):
        """updates the words to be consistent with the `information`"""
        words = []
        for word in self.words:
            if information.matches(word):
                words.append(word)
        self.words = words

    def matching(self, pattern, guess):
        """returns the set of words that couldve produced `pattern` in response to `guess`"""
        return [word
                for word in self.words
                if pattern.matches(guess, word)]
