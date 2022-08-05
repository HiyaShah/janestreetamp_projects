
import itertools
import re
import math
from csv import reader, writer

class Bot:
    def __init__(self):
        self.num_guesses = 0
        self.TOTAL_WORDS = len(Bot.list_wordlist())
        self.current_guess = None


    def calc_ent_write_to_csv(self):
        

        with open("wordlist.csv") as file:
            csv_reader = reader(file)
            words = list(csv_reader)
        with open('wordlist_writable.csv','w') as file:
            csv_writer = writer(file)
            for word in words:
                entropy = self.get_entropy(word[0])
                word.append(entropy)
                print(word)
                csv_writer.writerow(word)
    
    def update_wordlist_csv(self,new_list):
        print("newlist is",new_list)
        with open('wordlist.csv','w') as file:
            csv_writer = writer(file)
            for word in new_list:
                print("adding",word)
                csv_writer.writerow(word)
    
    @staticmethod
    def list_wordlist():
        with open("wordlist.csv") as file:
                    csv_reader = reader(file)
                    lst= [item[0] for item in list(csv_reader)]
                    return lst
    @staticmethod
    def str_wordlist():
        return " ".join(Bot.list_wordlist())

    def get_all_possible_patterns(self):
        patterns = (list(itertools.product("012", repeat=5)))
        return [[int(color) for color in lst_colors] for lst_colors in patterns]
    
    def count_yellows(self, letter):
        regex_code = rf"{letter}\w"+r'{'+r'4'+r'}' + rf"|\w{letter}\w"+r'{'+r'3'+r'}' + rf"|\w\w{letter}\w"+r'{'+r'2'+r'}' + rf"|\w\w\w{letter}\w" + rf"|\w\w\w\w{letter}"
        regex = re.compile(regex_code) 
        return(len(regex.findall(Bot.str_wordlist())))

    def count_greens(self, letter, index):
        regex_code = [r"\w",r"\w",r"\w",r"\w"]
        regex_code = list(regex_code)
        regex_code.insert(letter,index)
        regex_code="".join(regex_code)
        regex = re.compile(regex_code) 
        return(len(regex.findall(Bot.str_wordlist()))) 
    
    def count_grays(self,letter):
        return self.TOTAL_WORDS - self.count_yellows(letter)

    def get_entropy(self,word):
        all_patterns = self.get_all_possible_patterns()
        expected_info = 0
        for pattern in all_patterns:
            probability = 1.0
            for i in range(5):
                if pattern[i] == 0:
                    probability*= self.count_grays(word[i])/self.TOTAL_WORDS
                    
                if pattern[i] == 1:
                    
                    probability*=self.count_yellows(word[i])/self.TOTAL_WORDS
                    
                if pattern[i] == 2:
                    probability*=self.count_greens(i,word[i])/self.TOTAL_WORDS
                    
            expected_info+=probability*math.log(1.0/probability,2)
        return expected_info
    
    def get_entropy_one_pattern(self,word,pattern):
        expected_info = 0

        probability = 1.0
        for i in range(5):
            if pattern[i] == 0:
                probability*= self.count_grays(word[i])/self.TOTAL_WORDS

                print(f"the grays for {word[i]} are {self.count_grays(word[i])}")
                print(f"the probability for gray {word[i]} is {probability}") 
            if pattern[i] == 1:
                probability*=self.count_yellows(word[i])/self.TOTAL_WORDS
                print(f"the yellows for {word[i]} are {self.count_yellows(word[i])}")
                print(f"the probability for yellow {word[i]} is {probability}")
            if pattern[i] == 2:
                probability*=self.count_greens(i,word[i])/self.TOTAL_WORDS
                print(f"the greens for {word[i]} are {self.count_greens(i,word[i])}")
                print(f"the probability for green {word[i]} is {probability}")
            print(probability) 
        expected_info+=probability*math.log(1.0/probability,2)
        return expected_info
    
    def max_entropy_word(self):
        with open("wordlist_writable.csv") as file:
            csv_reader = reader(file)
            lst_wordlist_entropies = list(csv_reader)
            max_entropy = max(row[1] for row in lst_wordlist_entropies)
            guess = [row[0] for row in lst_wordlist_entropies if row[1]==max_entropy][0]
            print("my guess is", guess, "with an entropy of", max_entropy)
            self.current_guess = guess
            self.num_guesses+=1
            return guess
    
    def refine(self,current_pattern):
        print(current_pattern)
        new_list = Bot.list_wordlist()
        for i in range(5):
            for word in Bot.list_wordlist():
                if self.current_guess[i] in word and current_pattern[i]==0:
                    print("removing gray", word)
                    if word in new_list: new_list.remove(word)
                if (self.current_guess[i] == word[i] or self.current_guess[i] not in word) and current_pattern[i]==1:
                    if word in new_list: new_list.remove(word)
                    print("removing yellow", word)
                if self.current_guess[i] != word[i] and current_pattern[i]==2:
                    if word in new_list: new_list.remove(word)
                    print("removing green", word)
        self.update_wordlist_csv(new_list)

    # def calculate_all_entropies(self):
    #     entropy_values = []
    #     for word in self.list_wordlist():
    #         entropy = self.get_entropy(word)
    #         entropy_values.append(entropy)
    #         print(entropy)
    #     self.write_to_csv(entropy_values)
b = Bot()
# print(b.calc_ent_write_to_csv())
# print(b.max_entropy_word())
        
