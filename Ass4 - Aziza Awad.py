'''
Natural Language Processing (NLP)
ECOM6355
ASSIGNEMENT # 4
AZIZA AWAD HASSAN
220182085
'''

################# Q. 3.8 & Q. 3.9 ##################
import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter
import random


text1 = "I need to write a program in NLTK that breaks a corpus (a large collection of \
txt files) into unigrams, bigrams, trigrams, fourgrams and fivegrams.\
I need to write a program in NLTK that breaks a corpus"

file = open(r"C:\Users\aawad\PycharmProjects\NLP\wizard_of_oz.txt","r")
text2 = file.read()


tokens1 = nltk.word_tokenize(text1)
tokens2 = nltk.word_tokenize(text2)


print('tokens1 = ', tokens1)
print('tokens2 = ', tokens2)

print(Counter(tokens1))
print(Counter(tokens2))


################# Q. 3.10 ##################

from random import choice

def generate_sentence(tokens, min, max):
    s = []
    length =0
    for x in range(random.randint(min, max)):
        word = random.choice(tokens)
        s.append(word)
        length += 1
    sentence = " ".join(s)
    return sentence, length

sentence1, len1 = generate_sentence(tokens1, 3, 6)
sentence2, len2 = generate_sentence(tokens2, 4, 10)
print('sentence1 length = ', len1)
print('sentence1 = ', sentence1)
print('sentence2 length = ', len2)
print('sentence2 = ', sentence2)

tokens1 = nltk.word_tokenize(sentence1)
tokens2 = nltk.word_tokenize(sentence2)
bigrams1 = ngrams(tokens1,2)
bigrams2 = ngrams(tokens2,2)
print (Counter(bigrams1))
print (Counter(bigrams2))



################# Q. 3.11 ##################

def word_freq_unigram(string):
    text = word_tokenize(string.lower())
    c = Counter(text)           # count the words
    d = Counter(''.join(text))  # count all letters
    return (dict(c),dict(d))    # return a tuple of counted words and letters

data = "This is a text, it contains  dupes and more dupes and dupes of dupes and lkkk."
words, letters = word_freq_unigram(data) # count and get dicts with counts

sumWords = sum(words.values())       # sum total words
sumLetters = sum(letters.values())   # sum total letters

# calc / print probability of word
for w in words:
    print("Probability of '{}': {}".format(w,words[w]/sumWords))

# calc / print probability of letter
for l in letters:
    print("Probability of '{}': {}".format(l,letters[l]/sumLetters))

# update the counts to propabilities:
for w in words:
    words[w] = words[w]/sumWords

print (words)



import math
Pro_sum = 0
for w in words:
    Pro_sum += math.log(words[w])
Pro_sum = math.exp(Pro_sum)
print('probability(log) = ', Pro_sum)
perplexity = math.pow(Pro_sum, (-1/sumWords))
print ('perplexity = ', perplexity)




def word_freq_bigram(string):
    text = word_tokenize(string.lower())
    c = Counter(ngrams(text,2))
    return dict(c)


data = "This is a text, it contains  dupes and more dupes and dupes of dupes and lkkk."
words = word_freq_bigram(data)
print('all_words = ', words)
sumWords1 = sum(words.values())       # sum total words

# calc / print probability of word
for w in words:
    print("Probability of '{}': {}".format(w,words[w]/sumWords1))

import math
Pro_sum = 0
for w in words:
    Pro_sum += math.log(words[w])
Pro_sum = math.exp(Pro_sum)
print('probability(log) = ', Pro_sum)
perplexity = math.pow(Pro_sum, (-1/sumWords))
print ('perplexity = ', perplexity)







