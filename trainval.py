from collections import Counter
import numpy as np
import itertools
from markovorder import *
import random

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

# percent of data to be used in training set
SPLIT = 0.9

# how much of the test string is given to the generator
# must be >= ORDER
# not too long or else can't index question text
START = 8


data = [cs1110.data, cs4410.data, cs4820.data,
        cs4700.data, cs4620.data, cs2110.data]
for dataset in data:
    random.shuffle(dataset)

xTr = []
xTe = []
for dataset in data:
    split = round(len(dataset) * SPLIT)
    xTr += dataset[:split]
    xTe += dataset[split:]

train_text = ''
for text in xTr:
    train_text += ' ' + text

m = Markov(train_text.lower(), SMOOTH, CHAR, ORDER)

predictions = [m.generate(' '.join(text.split()[:START]))
               for text in xTe]

for index in range(len(xTe)):
    print("===========")
    print(index)
    print(xTe[index])
    print("-")
    print(predictions[index][0])
    print(predictions[index][1])

stats = []
for index in range(len(xTe)):
    same = 0
    pred = predictions[index][0].split()[START:]
    test = xTe[index].split()[START:]
    for word in pred:
        same += 1 if word in test else 0
    stats += [[index, same]]

print('')
print('===')
np.set_printoptions(threshold=np.inf)
print(np.array(stats))
print("mean = " + str(np.mean(stats, axis=0)[1]))
print("median = " + str(np.median(stats, axis=0)[1]))
print("max = " + str(np.amax(stats, axis=0)[1]))
