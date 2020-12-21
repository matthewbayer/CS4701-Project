from collections import Counter
from numpy.random import choice


class Markov:
    def __init__(self, text, smoothing_factor, char, order=1):
        """
        text: training data
        smoothing factor: must be > 0, should be very small or else would just randomly choose 
        char: True if character
        order: must be >= 1, larger than 5 would repeat corpus
        """
        self.char = char
        if self.char:
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

    def generate(self, text=None, length=None):
        self.fail = 0
        if text != None and self.char:
            text = text.lower()
        elif text != None and not self.char:
            text = text.lower().split()
        else:
            text = list(self.states[choice(len(self.states))])
        if length == None and self.char:
            length = 150
        elif length == None and not self.char:
            length = 30
        if self.char:
            # char level
            for i in range(len(text), length):
                state = tuple(text[i - self.order:])
                text += self.generate_text(state)
            text = "".join(text)
            return text, self.fail
        else:
            # word level
            for i in range(len(text), length):
                state = tuple(text[i - self.order:])
                result = self.generate_text(state)
                text.append(result)
            text = " ".join(text)
            return text, self.fail
