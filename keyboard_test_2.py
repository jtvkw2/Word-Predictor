# -*- coding: utf-8 -*-
"""
Date: Jan 14 2021

Authors: srinibadri, gsprint
"""
import random
import string
import timeit

from word_predictor import WordPredictor


def random_load_test(wp):
    print("random load test: ")
    valid = string.ascii_lowercase
    test_num = 10000
    hits = 0
    for i in range(test_num):
        prefix = ""
        for j in range(0, random.randint(1, 6), 1):
            prefix += valid[random.randrange(0, len(valid))]
        de = wp.get_best(prefix)
        if de is not None and de.get_word() != "null":
            hits += 1

    print("Hit = %.2f%%" % (hits / test_num * 100))


def main():
    # train a model on the first bit of Moby Dick
    wp = WordPredictor()
    print("bad1 = %s" % wp.get_best("the"))
    wp.train("moby_start.txt")
    print("training words = %d" % (wp.get_training_count()))

    # try and crash things on bad input
    print("bad2 = %s" % wp.get_best("the"))
    wp.train("thisfiledoesnotexist.txt")
    print("training words = %d\n" % (wp.get_training_count()))

    words = ["the", "me", "zebra", "ishmael", "savage"]
    for word in words:
        print("count, %s = %d" % (word, wp.get_word_count(word)))
    wp.train("moby_end.txt")
    print()
    # check the counts again after training on the end of the book
    for word in words:
        print("count, %s = %d" % (word, wp.get_word_count(word)))
    print()

    # Get the object ready to start looking things up
    wp.build()

    # do some prefix loopups
    test = ["a", "ab", "b", "be", "t", "th", "archang"]
    for prefix in test:
        if wp.get_best(prefix):
            print("%s -> %s\t\t\t%.6f" % (prefix, wp.get_best(prefix).get_word(), wp.get_best(prefix).get_prob()))
        else:
            print("%s -> %s\t\t\t%s" % (prefix, "None", "None"))
    print("training words = %d\n" % (wp.get_training_count()))

    # add two individual words to the training data
    wp.train_word("beefeater")
    wp.train_word("BEEFEATER!")
    wp.train_word("BEEFEATER")
    wp.train_word("Pneumonoultramicroscopicsilicovolcanoconiosis")
    print("added additional words")
    print("training words = %d\n" % (wp.get_training_count()))

    # The change should have no effect for prefix lookup until we build()
    test_2 = ['b', 'pn']
    for prefix in test_2:
        if wp.get_best(prefix):
            print("before, %s -> %s\t\t%.6f" % (prefix, wp.get_best(prefix).get_word(), wp.get_best(prefix).get_prob()))
        else:
            print("before, %s -> %s\t\t%s" % (prefix, "None", "None"))
    wp.build()
    for prefix in test_2:
        if wp.get_best(prefix):
            print("after, %s -> %s\t\t%.6f" % (prefix, wp.get_best(prefix).get_word(), wp.get_best(prefix).get_prob()))
        else:
            print("after, %s -> %s\t\t%s" % (prefix, "None", "None"))
    print("training words = %d\n" % (wp.get_training_count()))

    # test out training on a big file, timing the training as well
    start = timeit.default_timer()
    wp.train("mobydick.txt")
    wp.build()
    for prefix in test:
        if wp.get_best(prefix):
            print("%s -> %s\t\t\t%.6f" % (prefix, wp.get_best(prefix).get_word(), wp.get_best(prefix).get_prob()))
        else:
            print("%s -> %s\t\t\t%s" % (prefix, "None", "None"))
    print("training words = %d\n" % (wp.get_training_count()))
    stop = timeit.default_timer()
    elapsed = (stop - start)
    print("elapsed (s): %.6f" % elapsed)
    # test lookup using random prefixes between 1-6 characters
    start = timeit.default_timer()
    random_load_test(wp)
    stop = timeit.default_timer()
    elapsed = (stop - start)
    print("elapsed (s): %.6f" % elapsed)


main()
