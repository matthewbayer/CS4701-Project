from collections import Counter
from numpy.random import choice
import itertools

import dataset.cs1110fa18 as cs1110
import dataset.cs4410sp20 as cs4410
import dataset.cs4820fa20 as cs4820

# switch for either character (True) or word level (False)
CHAR = False

# markov chain of order ORDER
# how many past words/chars are in the state
# should be greater than or equal to 1
# shouldn't be larger than 5 or else would always choose transition randomly or
# repeat dataset
ORDER = 1

# smoothing for markov chain
# must be > 0
# should be less than 0.00001 for order 2
SMOOTH = 0.00001


class Markov:
    def __init__(self, text, smoothing_factor, order=1):
        """
        text: training data
        smoothing factor: must be > 0, should be very small or else would just randomly choose 
        order: must be >= 1, larger than 5 would repeat corpus
        """
        if CHAR:
            self.vocab = set(text)
        else:
            text = text.split()
            self.vocab = set(text)
        self.order = order
        self.smoothing_factor = smoothing_factor
        self.states = []
        self.counts = self.process(text)
        self.fail = 0

    def process(self, text):
        counts = {}
        for index in range(self.order, len(text)):
            state = tuple(text[(index - self.order):index])
            next_char = text[index]
            if state not in counts:
                self.states += [state]
                counts[state] = Counter()
                counts[state][next_char] = 1
            else:
                counts[state][next_char] += 1
        return counts

    def generate_text(self, state):
        smoothing = Counter({c: self.smoothing_factor for c in self.vocab})
        if state in self.counts:
            total_weights = dict(smoothing + self.counts[state])
        else:
            self.fail += 1
            return choice(list(self.vocab))

        chars = list(self.vocab)
        total_mass = sum(total_weights.values())
        probs = [0] * len(chars)
        for i, char in enumerate(chars):
            probs[i] = total_weights[char] / total_mass
        next_char = choice(chars, p=probs)
        return next_char


sample_text = "\n".join(cs4410.data) + \
    "\n".join(cs1110.data) + "\n".join(cs4820.data)
sample_text = sample_text.lower()
m = Markov(sample_text, SMOOTH, ORDER)

if CHAR:
    # char level
    text = list(m.states[choice(len(m.states))])
    for i in range(ORDER, ORDER * 100):
        state = tuple(text[i - ORDER:])
        text += m.generate_text(state)
    text = "".join(text)
    print(text)
    print(m.fail)
else:
    # word level
    text = list(m.states[choice(len(m.states))])
    for i in range(ORDER, ORDER * 30):
        state = tuple(text[i - ORDER:])
        text.append(m.generate_text(state))
    text = " ".join(text)
    print(text)
    print(m.fail)
