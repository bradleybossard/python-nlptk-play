"""
  Plot the cumulative frequency of the first 50 words in Moby Dick.
"""

from nltk import FreqDist
from nltk.corpus import gutenberg
moby = gutenberg.words('melville-moby_dick.txt')

fdist = FreqDist(moby)
vocab = fdist.keys()
fdist.plot(50, cumulative=True)
