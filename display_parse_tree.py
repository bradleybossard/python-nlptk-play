"""
Displays a parse tree from an example sentence from the WSJ corpus, example from http://www.nltk.org homepage
"""

from nltk.corpus import treebank
t = treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()
