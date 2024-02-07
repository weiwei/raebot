from pprint import pprint
from raebot import search_words

def test_search_words():
    assert len(search_words("linda")) == 1
    assert len(search_words("gafas")) == 4
