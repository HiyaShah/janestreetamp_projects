from bot import *
from wordle import *
import random
class PerformanceTracker:

    def __init__(self):
        self.shuffle_wordlist_trimmed()
        self.w = Wordle()
        self.bot = Bot()
        print("the word is",self.w.actual_word)
        self.run_game()
    def update_scores(self):
        self.guesses.append(self.player.num_guesses)

    def run_game(self):
        self.bot.calc_ent_write_to_csv()
        guess = self.bot.max_entropy_word()
        self.bot.refine(self.w.check_guess(guess))
        print("the lst is", Bot.list_wordlist())

    
    def shuffle_wordlist_trimmed(self):
        with open("wordlist_full.csv") as file:
            csv_reader = reader(file)
            words = list(csv_reader)
            twenty_words = [random.choice(words) for i in range(20)]
        with open('wordlist.csv','w') as file:
            csv_writer = writer(file)
            for word in twenty_words:
                csv_writer.writerow(word)
p = PerformanceTracker()
p.shuffle_wordlist_trimmed()