#!/usr/bin/env python3

from termcolor import colored

class Color():
    """Produces ANSI colorized strings"""

    @staticmethod
    def green(s):
        """converts the string `s` to an ANSI green string"""
        return colored(s, "green")

    @staticmethod
    def yellow(s):
        """converts the string `s` to an ANSI yellow string"""
        return colored(s, "yellow")

class Code():
    """ A `Code` represents the outcome of one letter in a wordle game.

    For each letter:
    - Code.miss() conveys that the letter is correctly placed
      and at the correct position (i.e. green)
    - Code.hit()  conveys that the letter is in the word,
      but incorrectly placed (i.e. yellow)
    - Code.mem()  conveys that the letter is not in the word (i.e. grey)

    NOTE: It is considered DANGEROUS AND UNSAFE to use the literal codes `-1`,
    `0` and `1`. Please instead use the static methods `Code.miss()`,
    `Code.hit()` and `Code.mem()`.
    """

    @staticmethod
    def miss():
        """Code indicating the letter is not in the word (GREY)

        The `miss` code conveys that the letter is not in the word (i.e. grey).
        Its underlying value is -1. DO NOT USE THE TRUE VALUE.
        """
        return -1

    @staticmethod
    def hit ():
        """Code indicating the letter is correctly placed (GREEN)

        The `hit` code conveys that the letter in the word at the indicated
        position (i.e. green). Its underlying value is 1. DO NOT USE THE TRUE
        VALUE.
        """
        return 1
    @staticmethod
    def mem ():
        """Code indicating the letter is in the worrd but incorrectly placed (YELLOW)

        The `mem` code (for "member") conveys that the letter in the word at the
        indicated position (i.e. yellow). Its underlying value is 0. DO NOT USE
        THE TRUE VALUE.
        """
        return 0

    @staticmethod
    def code(idx, letter, goal):
        """Computes the code for the `idx`th `letter` of the guess word when the correct
        word is `goal`
        """
        if goal[idx] == letter:
            return Code.hit()
        elif letter in goal:
            return Code.mem()
        else:
            return Code.miss()

class Pattern():
    """The pattern of outcomes expressed as `Code`s for a wordle guess"""

    def __init__(self, pattern = None, guess = None, goal = None):
        """Initialize Pattern.

        One of `pattern` or `guess` and `goal` must be provided. Will trigger an
        assertion error if insufficient arguments are procided.

        given a an option list of `Code`s (which is by default
        empty)

        """
        assert guess is not None and goal is not None or pattern is not None
        if pattern is None:
            self.pattern = [
                Code.code(idx, letter, goal)
                for (idx, letter) in enumerate(guess)
            ]
        else:
            self.pattern = pattern

    def __getitem__(self, i):
        """Gets the `i`th element of the pattern"""
        return self.pattern[i]

    def matches(self, guess, word):
        """Checks that `word` and `guess` are consistent w.r.t the pattern.

        Returns True if `word` could be a solution to the wordle problem and
        have produced the pattern held in `self` in response to the player
        guessing `guess`.

        """
        for (idx,code) in enumerate(self.pattern):
            if code == Code.hit():
                try:
                    if word[idx] != guess[idx]:
                        return False
                except e:
                    print(word, idx, guess)
                    raise e
            if code == Code.miss():
                if guess[idx] in word:
                    return False
            if code == Code.mem():
                if guess[idx] not in word \
                   or guess[idx] == word[idx]:
                    return False
        return True

    
class Information():
    """Information maintains a `guess` word and the `Pattern` associated with that guess."""

    def __init__(self, goal, guess):
        """Create Information

        The `goal` is the secret word that drives the wordle game, and
        `guess` is the player's guess.

        PRECONDITIONS:
        - `guess` is not None
        - `goal` is not None
        - length of `guess` and `goal_word` must be the same
        """
        assert guess is not None
        assert goal is not None
        assert len(goal) == len(guess)
        self.guess = guess
        self.pat = Pattern(guess = guess, goal = goal)


    def __str__(self):
        string = ""
        for (i,code) in enumerate(self.pat):
            if code == Code.hit():
                string += Color.green(self.guess[i])
            elif code == Code.mem():
                string += Color.yellow(self.guess[i])
            else:
                string += self.guess[i]
        return string

    def matches(self, word):
        """Returns True if `word` could have yielded `self.pat` for guess `self.guess`"""
        return self.pat.matches(self.guess, word)

def patterns():
    """constructs a list of all 3^5 possible patterns in no particular order"""
    outcomes = [()]
    for i in range(5):
        outcomes = [
            pattern + (code,)
            for pattern in outcomes
            for code in [Code.hit(), Code.miss(), Code.mem()]
        ]
    return [Pattern(outcome) for outcome in outcomes]

print(Information.patterns())