"""
Identify a named entity in the text, example from http://www.nltk.org/ homepage.
"""

import nltk

sentence = "At eight o'clock on Thursday morning Arthur didn't feel very good."

tokens = nltk.word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)
entities = nltk.chunk.ne_chunk(tagged)

print entities

