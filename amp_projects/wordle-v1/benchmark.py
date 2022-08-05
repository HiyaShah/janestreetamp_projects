#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

from multiprocessing import Pool

from wordle import GameManager
from solver import *

def experiment(idx):
    return GameManager(Solver()).play_game()

num_trials = 1000
guess_counts = []
#generates histogram of winners 
for winner in map(experiment, range(num_trials)):
    guess_counts.append(winner)

print("generating histogram")
plt.hist(guess_counts, bins=(sorted(list(set(guess_counts + [0,1,2,3,4,5,6])))), density=True)
plt.xlabel("Number of guesses")
plt.ylabel("Proportion of words solved")
fn = "solver_data.pdf"
plt.savefig(fn)
print("saved to", fn)
print("expected number of guesses:", float(sum(guess_counts)) / float(num_trials))
num_failures = sum([1 for num_guesses in guess_counts if num_guesses > 5])
print("number of failures (of {}):".format(num_trials), num_failures)
print("the maximum number of guesses to find any word was:", max(guess_counts))
