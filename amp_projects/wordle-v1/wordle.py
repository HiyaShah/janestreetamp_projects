#!/usr/bin/env python3

from random import choice

from information import *
from wordlist import WordList


class Wordle():
    """The Wordle Game State

    this class manages and processes player guesses
    """

    def __init__(self, word = None):
        """Creates a Wordle Game

        The optional `word` argument specifies the game word. If no word is
        given, a random word is drawn from the word list.
        """
        self.guesses = []
        if word is None:
            self.word = WordList().get_random_word()
        else:
            self.word = word

    def string_guess(self, guess):
        """Converts a guess to a colorized string corresponding to the information content."""
        return str(Information(goal_word = self.word, guess = guess))

    def __str__(self):
        """
        converts the set of guessed words to a string
        """
        return "-----\n" \
            +  "\n".join(map(self.string_guess, self.guesses)) \
            +   "\n-----\n"

    def guess(self, guess):
        """A guess is made and information about the guess is returned"""
        # assert guess is not None
        if guess is not None:
            self.guesses.append(guess)
            return Information(goal = self.word, guess = guess)

    def is_word(self, guess):
        """Checks whether the guess is itself the word"""
        return guess == self.word

class Player():
    """Represents a human wordle player.

    Records a numeric count of the guesses and allows the human player to make
    guesses.
    """

    def __init__(self):
        """Initialize the player"""
        self.num_guesses = 0

    def make_guess(self):
        """returns a string guess

        For the human `Player`, the guess is read from the user's input. If the
        user's input is ill-formed (i.e.) not a sequence of 5 characters,
        `make_guess` prompts the user again and again until it is.
        """
        guess = ""
        while len(guess) != 5:
            guess = input("> ")
            guess = guess.strip()
        self.num_guesses += 1
        return guess

    def update_knowledge(self, info):
        """updates the knowledge state with `info`

        For the human `Player` the `info` is simply printed to the CLI to update
        the human about the quality of their guess
        """
        print(info)

class GameManager():
    """The GameManager runs the main control loop of the Wordle game """

    def __init__(self, player):
        """starts a game with one `player`"""
        self.wordle = Wordle()
        self.player = player

    def play_game(self):
        """starts the main game loop.

        The loop solicits guesses from self's player and passes them to self's
        wordle instance. It then conveys the success/fail info back to self's player.
        The loop continues until the player guesses the correct word.
        """
        guess = ""
        while not self.wordle.is_word(guess):
            guess = self.player.make_guess()
            info = self.wordle.guess(guess)
            self.player.update_knowledge(info)
        return self.player.num_guesses

def main():
    g = GameManager(Player())
    g.play_game()


if __name__ == "__main__": main()
