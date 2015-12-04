# -*- coding: utf-8 -*-
import os
import re
import collections
import cPickle as pickle
import sys


path = "/Users/abatian/Downloads/corpus/"

def make_stats():
    first_counter = collections.Counter()
    words_counter = {}
    pairs_counter = {}

    for (dirpath, dirnames, filenames) in os.walk(path):
        for filename in filenames:
            if filename.endswith(".txt"):
                f = open(dirpath + "/" + filename, 'r')
                book = f.read()
                book = book.replace('’', "'")
                rgx = re.compile("([\w]+['-]?[\w]*[,]?|\.|\?|!)")
                words = rgx.findall(book)
                for idx in range(len(words)-2):
                    if words[idx] not in ".?!":
                        if words[idx+1] not in ".?!":
                            if pairs_counter.has_key((words[idx], words[idx+1])):
                                if pairs_counter[(words[idx], words[idx+1])].has_key(words[idx+2]):
                                    pairs_counter[ (words[idx], words[idx+1]) ][ words[idx+2] ] += 1
                                else:
                                    pairs_counter[ (words[idx], words[idx+1]) ][ words[idx+2] ] = 1
                            else:
                                pairs_counter[ (words[idx], words[idx+1]) ] = {words[idx+2]:1}
                    elif words[idx+1] not in ".?!":
                        if (len(words[idx+1]) > 1 or words[idx+1] == "I" or words[idx+1] == "A") and words[idx+1][0].isupper():
                            first_counter[ words[idx+1] ] += 1
                            if words_counter.has_key(words[idx+1]):
                                if words_counter[words[idx+1]].has_key(words[idx+2]):
                                    words_counter[ words[idx+1] ][ words[idx+2] ] += 1
                                else:
                                    words_counter[ words[idx+1] ][ words[idx+2] ] = 1
                            else:
                                words_counter[ words[idx+1] ] = {words[idx+2]:1}
                f.close()

    
    f = open(path + "first_C.pkl", 'wb')
    pickle.dump(first_counter, f, 2)
    f.close()

    f = open(path + "words_C.pkl", 'wb')
    pickle.dump(words_counter, f, 2)
    f.close()

    f = open(path + "pairs_C.pkl", 'wb')
    pickle.dump(pairs_counter, f, 2)
    f.close()

if __name__ == '__main__':
    make_stats()





