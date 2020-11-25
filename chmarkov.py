from collections import Counter
from numpy.random import choice

import dataset.cs1110fa18 as cs1110
import dataset.cs4410sp20 as cs4410


CHAR = False


class Markov:
    def __init__(self, text, smoothing_factor):
        if CHAR:
            # Char level
            self.vocab = set(text)
            self.smoothing_factor = smoothing_factor
            self.counts = {c: Counter() for c in self.vocab}
            self.process(text)
        else:
            # Word level
            self.vocab = set(text.split())
            self.counts = {c: Counter() for c in self.vocab}
            self.smoothing_factor = smoothing_factor
            self.process(text)

    def process(self, text):
        if CHAR:
            # Char level
            for idx in range(len(text) - 1):
                prev_char = text[idx]
                next_char = text[idx + 1]
                self.counts[prev_char][next_char] += 1
        else:
            # Word level
            words = text.split()
            for idx in range(len(words) - 1):
                prev_word = words[idx]
                next_word = words[idx + 1]
                self.counts[prev_word][next_word] += 1

    def generate_next(self, char):
        smoothing = Counter({c: self.smoothing_factor for c in self.vocab})
        total_weights = dict(smoothing + self.counts[char])

        chars = list(self.vocab)
        total_mass = sum(total_weights.values())
        probs = [0] * len(chars)
        for i, char in enumerate(chars):
            probs[i] = total_weights[char] / total_mass

        next_char = choice(chars, p=probs)
        return next_char


data = cs4410.data
sample_text = "\n".join(data)
sample_text += "\n" + "\n".join(cs1110.data)
sample_text = sample_text.lower()
# m = Markov(sample_text, 0.0002)
m = Markov(sample_text, 0.0000002)

if CHAR:
    # char level
    text = "a"
    for i in range(100):
        text += m.generate_next(text[-1])
    print(text)
else:
    # word level
    word = "the"
    word = "we"
    text = ''
    for i in range(30):
        text += word + ' '
        word = m.generate_next(word)
    print(text)
