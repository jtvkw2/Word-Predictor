from dictEntry import DictEntry
from map import Map
import re


class WordPredictor:
    def __init__(self):
        self.totalCount = 0
        self.built = False
        self.word_to_count = Map()
        self.prefix_to_entry = Map()

    def get_best(self, word):
        if self.built is False:
            return 'null'
        highest = 0
        highest_entry = None
        if type(self.prefix_to_entry.get(word)) == int:
            return
        for entry in self.prefix_to_entry.get(word):
            if entry.get_prob() > highest:
                highest = entry.get_prob()
                highest_entry = entry
        return highest_entry

    def train(self, filename):
        try:
            file = open("texts/" + filename).read()
            for word in file.split():
                word = re.sub(r'[^\w\s]', '', word)
                self.word_to_count.insert(word.lower(), 1)
                self.totalCount += 1
        except FileNotFoundError:
            print("Could not open training file: " + filename)

    def get_training_count(self):
        return self.totalCount

    def get_word_count(self, word):
        return self.word_to_count.get(word)

    def build(self):
        self.prefix_to_entry = Map()
        for i in range(10):
            for key, value in self.word_to_count.hash_table[i]:
                for s in range(1, len(key)+1):
                    chars = key[0:s]
                    if self.totalCount == 0:
                        percent = 0
                    else:
                        percent = self.word_to_count.get(key) / self.word_to_count.count
                    self.prefix_to_entry.insert(chars, [DictEntry(key, percent)])
            self.built = True

    def train_word(self, word):
        self.word_to_count.insert(word.lower(), 1)
        self.totalCount += 1
