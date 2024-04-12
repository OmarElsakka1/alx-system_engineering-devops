#!/usr/bin/python3
"""
100-main
"""
import sys

if __name__ == '__main__':
    count_words = __import__('100-count').count_words
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        string = "python java javascript"
        print("Ex: {} programming '{}'".format(sys.argv[0], string))
    else:
        result = count_words(sys.argv[1], [x for x in sys.argv[2].split()])
