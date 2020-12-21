from collections import Counter
import numpy as np
import itertools
from markovorder import *

import dataset.cs1110fa18 as cs1110
import dataset.cs4410sp20 as cs4410
import dataset.cs4820fa20 as cs4820
import dataset.cs4700sp20 as cs4700
import dataset.cs4620fa20 as cs4620
import dataset.cs2110sp19 as cs2110

# switch for either character (True) or word level (False)
CHAR = False

# markov chain of order ORDER
# how many past words/chars are in the state
# should be greater than or equal to 1
# shouldn't be larger than 5 or else would always choose transition randomly or
# repeat dataset
ORDER = 3

# smoothing for markov chain
# must be > 0
# should be less than 0.00001 for order 2
SMOOTH = 0.00000018

# input text to override random state
# order needs to be less than or equal to length of TEXT
# set to None for random state
TEXT = None

sample_text = "\n".join(cs4410.data) + "\n".join(cs1110.data) + \
    "\n".join(cs4820.data) + "\n".join(cs4700.data) + \
    "\n".join(cs4620.data) + "\n".join(cs2110.data)
sample_text = sample_text.lower()
m = Markov(sample_text, SMOOTH, CHAR, ORDER)

result = m.generate(TEXT)
print(result[0])
print(result[1])
