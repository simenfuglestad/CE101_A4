import urllib2
from bs4 import BeautifulSoup


def format_web_string(string):
    cache = ""
    found_tag = False
    for c in string:
        if c == '<':
            found_tag = True

        if c == '>':
            found_tag = False
            cache = cache + c

        if found_tag:
            cache = cache + c

        if not found_tag and len(cache) > 0:
            string = string.replace(cache, "")
            cache = ""
    return string


def eliminate_single_word_lines(string):
    for c in string:
        pass


def get_string_from_url(url):
    website = urllib2.urlopen(url).read()
    soup = BeautifulSoup(website, "lxml")
    string = ""
    for p in soup.findAll('p'):
        string = string + str(p) + '\n'
    string = str(soup.findAll('title')) + string
    return string

print format_web_string(get_string_from_url(
        "http://www.bbc.co.uk/news/uk-england-leeds-38767596"))
