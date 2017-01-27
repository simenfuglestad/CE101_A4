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


def get_string_from_url(url):
    website = urllib2.urlopen(url).read()
    soup = BeautifulSoup(website, "lxml")
    string = ""
    for p in soup.findAll('p'):
        if "twite" not in str(p) and "promo" not in str(p):
            string = string + str(p) + '\n'
    title = str(soup.findAll("title"))
    title = title[1:len(title) - 1]
    string = title + string
    return string

print format_web_string(get_string_from_url(
        "http://www.bbc.co.uk/news/uk-england-leeds-38767596"))
