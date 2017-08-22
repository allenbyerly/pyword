import sys
import datetime
import nltk
from nltk.corpus import treebank
from nltk.sem import Valuation, Model
#import spacy
from collections import deque
from functools import reduce
import re
from itertools import product
from string import whitespace
path = 'adventures-of-sherlock-holmes.txt'



file = open(path, 'r')
counter = 0;

token_index = 0
token_lines = [1000]

for line in file.readlines():
#sentence = """At eight o'clock on Thursday morning Arthur didn't feel very good."""

    print token_index
    tokens = nltk.word_tokenize(line)
    token_lines[0] = tokens
    print tokens
    token_index = token_index + 1
    if token_index >= 100:
        break
       # break


tagged = nltk.pos_tag(tokens)
print tagged
print tagged[0:1000]

#entities
entities = nltk.chunk.ne_chunk(tagged)
print entities

t = treebank.parsed_sents('wsj_0001.mrg')[0]
print t
t.draw()


print datetime.date.today()
