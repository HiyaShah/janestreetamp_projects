#!/usr/bin/env python3

from information import *
from wordlist import *

##################
### UNIT TESTS ###
##################

### Note that test_random_match_eq_refine means we only need to check the
### behavior of `matching`, which is simpler

given_words = ["freer", "dowry", "trait", "toddy", "fancy",
                   "civic", "quirk", "madam", "stood", "found" ]
words = WordList(given_words = given_words)

def check_matching(guess, goal, result):
    info = Information(guess = guess, goal = goal)
    new_words = words.matching(info.pat, guess = guess)
    # sort the words so that order doesnt matter
    assert list(sorted(new_words)) == list(sorted(result))

def test_matching_freer_dowry():
    check_matching("freer", "found", ["fancy", "found"])

def test_matching_freer_trait():
    check_matching("freer", "trait", ["trait"])

def test_matching_freer_toddy():
    check_matching("freer", "toddy", ["civic", "madam", "stood", "toddy"])

def test_matching_freer_fancy():
    check_matching("freer", "fancy", ["fancy", "found"])

def test_matching_freer_civic():
    check_matching("freer", "civic", ["civic", "madam", "stood", "toddy"])

def test_matching_freer_quirk():
    check_matching("freer", "quirk", ["dowry", "quirk"])

def test_matching_freer_madam():
    check_matching("freer", "madam", ["madam", "civic", "stood", "toddy"])

def test_matching_freer_stood():
    check_matching("freer", "stood",  ["stood", "madam", "civic", "toddy"])

def test_matching_freer_found_():
    check_matching("freer", "found", ["fancy", "found"])


def test_words_refine_member():
    given_words = ["freer", "dowry", "trait", "toddy", "fancy",
                   "civic", "quirk", "madam", "stood", "found"]
    words = WordList(given_words = given_words)
    info = Information(guess = "dowry", goal = "toddy")
    new_words = words.matching(info.pat, guess = "dowry")
    # sort the words so that order doesnt matter
    assert list(sorted(new_words)) == list(sorted(["toddy"]))

########################
### RANDOMIZED TESTS ###
########################

## Checking identity containment laws.
## Check every random word is member of the  list
def test_random_contains():
    words = WordList()
    for _ in range(100):
        word = words.get_random_word()
        if word not in words:
            print("Couldn't find word", word)
            assert words.get_random_word() in words

## Checking that refining the word list based on information computed from a
## given goal word doesn't accidentally remove the goal word
def test_random_refinement():
    for _ in range(100):
        words = WordList()
        guess = words.get_random_word()
        goal = words.get_random_word()
        while guess == goal:
            goal = words.get_random_word()
        words.refine(Information(guess = guess, goal = goal))
        if goal not in words:
            print("Couldn't find word", goal)
            assert goal in word

## Checking that refining the word list based on information computed from a
## given goal word doesn't accidentally remove the goal word
def test_random_match():
    words = WordList()
    for _ in range(100):
        guess = words.get_random_word()
        goal = words.get_random_word()
        while guess == goal:
            goal = words.get_random_word()
        info = Information(guess = guess, goal = goal)
        matches = words.matching(info.pat, guess)
        if goal not in matches:
            print("Couldn't find word", goal)
            assert goal in matches

## check that match and refine have the same behavior:
def test_random_match_eq_refine():
    for _ in range(100):
        words = WordList()
        guess = words.get_random_word()
        goal = words.get_random_word()
        while guess == goal:
            goal = words.get_random_word()
        info = Information(guess = guess, goal = goal)
        matches = words.matching(info.pat, guess)
        words.refine(info)
        assert matches == words.words


## check that match and refine have the same behavior:
def test_random_match_reciprocal():
    for _ in range(100):
        words = WordList()
        guess = words.get_random_word()
        goal = words.get_random_word()
        info = Information(guess=guess, goal=goal)
        words.refine(info)
        for word in words:
            assert (Information(guess=guess, goal=word)).matches(goal)
