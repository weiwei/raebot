from pprint import pprint
from raebot import search_words

def test_search_words():
    assert len(search_words("linda")) == 1

def test_search_words2():
    # gafa, gafar1, gafar2, gafo
    assert len(search_words("gafas")) == 4

def test_search_words3():
    assert len(search_words("Allen")) == 1


def test_search_words4():
    assert len(search_words("disparajuste")) == 0
