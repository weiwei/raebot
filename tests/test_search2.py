from pprint import pprint
from raebot import search_words
from time import sleep

def test_this():
    words = open("tests/exceptions.txt").read().splitlines()
    for wd in words:
        sleep(2)
        try:
            word = search_words(wd)
            if len(word) == 0:
                print("not found", wd)
        except:
            print("exception", wd)
