"Run this with pytest -s tests/test_search2.py"

from raebot import by_words
from time import sleep

import pytest

@pytest.mark.skip
def test_this():
    words = open("tests/exceptions.txt").read().splitlines()
    for wd in words:
        sleep(2)
        try:
            word = by_words(wd)
            if len(word) == 0:
                print("not found", wd)
        except:
            print("exception", wd)
