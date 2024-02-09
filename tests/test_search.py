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

def test_search_words5():
    assert len(search_words("fallecio")) == 2

def test_search_words6():
    assert len(search_words("yema")) == 1

def test_search_words7():
    assert len(search_words("Escocia")) == 2

def test_search_words8():
    assert len(search_words("adiposo")) == 1

def test_search_words9():
    assert len(search_words("alhajas")) == 2
