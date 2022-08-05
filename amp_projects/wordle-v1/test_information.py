#!/usr/bin/env python3

from information import *
from hypothesis import given, settings, strategies as st

def test_information_dowry_freer_trait():
    assert Information(guess="dowry", goal="freer").matches("trait")

def test_information_dowry_freer_toddy():
    assert not Information(guess="dowry", goal="freer").matches("toddy")

def test_information_dowry_freer_lorry():
    assert not Information(guess="dowry", goal="freer").matches("lorry")

def test_information_freer_stood_madam():
    assert Information(guess="freer", goal="stood").matches("madam")

def test_information_dowry_diggy_dasby():
    # dont think dasby is a word but ok
    assert Information(guess="dowry", goal="diggy").matches("dasby")


#########################
### Randomized Tests ###
#########################

words = st.text(
    st.characters(max_codepoint=1000, blacklist_categories=('Cc', 'Cs')),
    min_size=5, max_size=5).map(lambda s: s.strip()).filter(lambda s: len(s) == 5)

@given(words, words)
def test_pattern_matches_itself(guess, goal):
    assert Pattern(guess=guess, goal=goal).matches(guess, goal)

@given(words,words)
def test_information_matches_itself(guess, goal):
    assert Information(guess=guess, goal=goal).matches(goal)
