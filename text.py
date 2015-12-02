import cPickle as pickle
import bisect
import collections
import random

path = "/Users/abatian/Downloads/corpus/"

first_input = open('first_C.pkl', 'rb') 
first = pickle.load(first_input) 
first_input.close()

words_input = open('words_C.pkl', 'rb') 
words = pickle.load(words_input) 
words_input.close()

pairs_input = open('pairs_C.pkl', 'rb') 
pairs = pickle.load(pairs_input) 
pairs_input.close()

class WeightedChoice(collections.Sequence):
    def __init__(self, counter):
        self.values = counter.keys()
        self.cumweights = []
        cumsum = 0
        for (key, count) in counter.items():
            cumsum += count  
            self.cumweights.append(cumsum)  
    def __len__(self):
        return self.cumweights[-1]
    def __getitem__(self, i):
        if not 0 <= i < len(self):
            raise IndexError(i)
        return self.values[bisect.bisect(self.cumweights, i)]

def make_sentence():
	sentence = ""
	first_word = random.choice(WeightedChoice(first))
	sentence += first_word
	filtered_dict = words[first_word]
	second_word = random.choice(WeightedChoice(filtered_dict))
	if second_word not in ".?!":
			sentence += " "
	sentence += second_word
	third_word = second_word[:]
	num = 1
	while third_word not in ".?!":
		num += 1
		filtered_dict = pairs[(first_word, second_word)]
		third_word = random.choice(WeightedChoice(filtered_dict))
		first_word = second_word[:]
		second_word = third_word[:]
		if third_word not in ".?!":
			sentence += " "
		sentence += third_word
	return sentence, num


def make_text(words_num):
	text = ""
	cur_num = 0
	f = open("my_book.txt", "w")
	while cur_num < words_num:
		sentence, num = make_sentence()
		cur_num += num
		print sentence
		print cur_num
		f.write(sentence)
		f.write(" ")
	f.close()

make_text(10010)