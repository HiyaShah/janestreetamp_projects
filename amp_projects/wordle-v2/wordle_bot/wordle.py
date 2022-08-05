from bot import *
import random

class Wordle:
    
    def __init__(self):
        self.actual_word = self.select_word()
        print("the word is", self.actual_word)

    def select_word(self):
        idx = random.randint(0,20)
        return Bot.list_wordlist()[idx]

    def check_guess(self,guess):
        print("bot guessed", guess)
        colors = []
        for i in range(len(guess)):
            if guess[i] == self.actual_word[i]:
                colors.append(2)
            elif guess[i] in self.actual_word:
                colors.append(1)
            else:
                colors.append(0)
        return(tuple(colors))

    

