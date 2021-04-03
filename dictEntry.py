class DictEntry:
    # create a new entry given a word and probability
    def __init__(self, word, prob):
        self.word = word
        self.prob = prob

    # getter for the word
    def get_word(self):
        # returns string
        return self.word

    # getter for the probability
    def get_prob(self):
        # returns float
        return self.prob
