from pprint import pprint
from raebot import by_words

def test_search_words():
    assert len(by_words("linda")) == 1

def test_search_words2():
    # gafa, gafar1, gafar2, gafo
    assert len(by_words("gafas")) == 4

def test_search_words3():
    assert len(by_words("Allen")) == 1

def test_search_words4():
    assert len(by_words("disparajuste")) == 0

def test_search_words5():
    assert len(by_words("fallecio")) == 2

def test_search_words6():
    assert len(by_words("yema")) == 1

def test_search_words7():
    assert len(by_words("Escocia")) == 2

def test_search_words8():
    assert len(by_words("adiposo")) == 1

def test_search_words9():
    assert len(by_words("alhajas")) == 2
