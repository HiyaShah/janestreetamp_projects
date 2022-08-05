# Wordle

Your task is to implement a [Wordle](https://www.nytimes.com/games/wordle/index.html) player by writing code in `solver.py`. Feel free to try out your ideas and experiment, but remember to do so robustly and measure the effects of your changes. Using [`benchmark.py`](./benchmark.py)

## Basic structure.

There are three key files you can run, `wordle.py`, `solver.py` and `benchmark.py`.

### `wordle.py`

Running `python3 wordle.py` starts a game instance of wordle and allows you to play against the computer.


### `solver.py`

Running `python3 solver.py` runs your solver against the code. At first it will simply guess `salty` over and over again and never finish.

**WARNING**. At the start this will never terminate because solver always makes the same guess.

### `benchmark.py`

Running `python3 benchmark.py` generates 1000 random wordle games and uses your solver implementation to play the game. After running the 1000 simulations, it produces a PDF file `solver_data.pdf`, which depicts a histogram of your solver's performance. The horizontal axis is the number of guesses and the vertical axis is the proportion of wordle games that were solved in that number of guesses.

**WARNING**. At the start this will never terminate because solver always makes the same guess.

## Running test

I've included some tests for the `information.py` and `wordlist.py`. To run these tests, run `pytest`.

## Repository Contents

In this repository you will find the following files

1. [`wordle.py`](./wordle.py) contains the main game driver and logic for the class. If you run `python wordle.py` you can play wordle against the computer!

2. [`solver.py`](./solver.py) contains the starter code for your solution. You should write most of your code here.

3. [`benchmark.py`](./benchmark.py) runs the benchmarking script and produces a pdf file `solver_data.pdf` that shows a histogram of the number of guesses it took over a random sample (with replacement) of words taken from `possible_words.txt`. To run this script and measure the correctness of your solution, type `python3 benchmark.py` in the command line

4. [`information.py`](./information.py) contains some auxiliary classes for representing the outcomes of a guess (i.e. was each word correct, incorrect, or misplaced)

5. [`wordlist.py`](./wordlist.py) contains some auxiliary classes for representing and manipulating the list of words.

6. [`test_information.py`](./test_information.py) and [`test_wordlist.py`](./test_wordlist.py) contain testcases for the `information.py` and `wordlist.py` files respectively.


7. [`words.txt`](./words.txt) contains all allowed guesses in Wordle. This is scraped from the javascript implementation of the wordle game. 

8. [`possible_words.txt`](./possible_words.txt) contains the words that can occur as answers to the wordle game. these are scraped directly from the javascript implementation of wordle.

