import requests
from bs4 import BeautifulSoup
from .model import Definition, Phrase, Word

BASE_URL = "https://dle.rae.es"
session = requests.session()
session.headers.update({'User-Agent': 'Mozilla/5.0'})


def search_words(word: str):
    resp = session.get(f"{BASE_URL}/{word}?m=form")
    soup = BeautifulSoup(resp.text, 'html.parser')
    entries = soup.select('#resultados > article')
    if entries:
        words = []
        for entry in entries:
            linked_entries = entry.find_all('p', {'class': ['l', 'l3']})
            if linked_entries:
                for linked in linked_entries:
                    path = linked.find('a').attrs['href']
                    id = path.split('#')[1]
                    url = f"{BASE_URL}{path}"
                    resp = session.get(url)
                    soup = BeautifulSoup(resp.text, 'html.parser')
                    entry = soup.select(f'#{id}')
                    if entry:
                        if entry[0].attrs['class'] == ['k5'] or entry[0].attrs['class'] == ['k6']:
                            # Entry is a phrase
                            ph = entry[0].text
                            defi = Definition(entry[0].find_next_sibling('p', {'class': 'm'}))
                            wd = Phrase(ph, defi)
                        else:
                            wd = Word(entry[0])
                        words.append(wd)
            else:
                wd = Word(entry)
                words.append(wd)
        return words
    else:
        others = soup.select('#resultados > .otras > .n1 > a')
        words = []
        for o in others:
            path = o.attrs['href']
            id = path.split('#')[1]
            url = f"{BASE_URL}{path}"
            resp = session.get(url)
            soup = BeautifulSoup(resp.text, 'html.parser')
            entry = soup.select(f'article#{id}')
            wd = Word(entry[0])
            words.append(wd)
        return words


def search_expressions(expr: str):
    resp = session.get(f"{BASE_URL}/{word}?m=form2")
    soup = BeautifulSoup(resp.text, 'html.parser')
    entries = soup.select('#resultados > article')
    words = []
    for entry in entries:
        wd = Word(entry)
        words.append(wd)
    return words

def exact_match():
    pass

def start_with():
    pass

def end_with():
    pass

def contains():
    pass

def anagrams():
    pass

def random():
    pass



