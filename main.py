import datetime
from nltk import word_tokenize
import nltk
import collections
import io
import operator
import json

#map function that maps each occurrence pf a word to a map  that only adds words that are not alpha-numeric (punctuation)
def map_it(lines):
    """ Returns a list of lists of the form [word,1]
        for each element in the list that was passed.
    """
    return [[word, 1] for word in lines if word.isalpha()]

#resuce function reduces the map of words ato unique words and their counts
def reduce_it(wlist):
    """ Returns a list of list of the form [word,[partialcounts]] """
    res = collections.defaultdict(list)
    map(lambda w: res[w[0]].append(w[1]), wlist)
    return res.items()

#function that kicks off the map reduce process and returns a dictionary. where the vaue of each word is the sum of
#the occurances in the file
def map_reduce(wlist):
    """ Returns a dict with word : count mapping """
    results = {}
    for res in reduce_it(map_it(wlist)):
        results[res[0]] = sum(res[1])
    return results
#open the file
path = 'adventures-of-sherlock-holmes.txt'
file = io.open(path, 'r', encoding='utf8')
print '\nOPENING DOCUMENT: ' + '\n' + path
#convert the file data into tokens
tokens = word_tokenize(file.read())
#print tokens
print '\nTOKENIZING'
#the resulting word map maps each token to a list with each word having a count of 1 and then reduces that list
#to a map of only unique words and their occurrences. Furthermore, the functions used to do this have also made sure
#that only actual words and not punctuation are added to the map.
wordmap = map_reduce(tokens)
print '\nMAPPING & REDUCING'
print '\nCOUNTING WORD FREQUENCY'

#W

#SORT THE MAP SO THAT THE WORDS WITH THE MOST FREQUENCY ARE SORTED FIRST
sortedwordcounts = sorted(wordmap.items(), key=operator.itemgetter(1), reverse=True)
print '\nGENERATING SORTED LIST OF UNIQUE WORDS BY WORD COUNT'

#GENERATE A LIST AND THEIR OCCURRENCE FREQUENCY FROM THE SORTED MAP.
top10list = [v for v in sortedwordcounts[:10]]

print '\nFINALIZING TOP 10 WORDS BY WORD COUNT\n'


print '\nSUMMARY\n'
print 'THE TOTAL WORD COUNT IS: ' + str(len(tokens))

#formatted list of top 10 word used in the file
print '\n'
print 'THE TOP TEN LIST IS:\n'
print json.dumps(top10list)
print '\nPROCESS COMPLETED ON: ' + str(datetime.date.today())



#TEST CODE TO CLEANUP LATER
#for line in file.readlines():
#items = line.split(" ")
#Understand the architecture
#bring existing  skills
#keep team growing at the right pace
#network and social graph  and real time busines processing
#


#TEST CODE TO CLEANUP LATER
'''
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

#Word Count

44764




tagged = nltk.pos_tag(tokens)
print tagged
print tagged[0:1000]

#entities
entities = nltk.chunk.ne_chunk(tagged)
print entities

t = treebank.parsed_sents('wsj_0001.mrg')[0]
print t
t.draw()

wordcount = len(text10)


'''

