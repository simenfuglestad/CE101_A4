import urllib.request
from bs4 import BeautifulSoup

def format_web_string(string):
	cache =""
	found_tag = False
	for c in string:
		if c == '<':
			found_tag = True

		if c == '>':
			found_tag = False
			cache = cache + c

		if found_tag:
			cache = cache +c

		if not found_tag and len(cache) > 0:
			string = string.replace(cache, "")
			cache = ""
	return string

def get_string_from_url(url):
	website = urllib.request.urlopen(url).read()
	soup = BeautifulSoup(website, "lxml")
	string = ""
	for p in soup.findAll('p'):
		string = string + str(p) + '\n'
	return string

print(format_web_string(get_string_from_url("http://www.bbc.co.uk/news/uk-politics-38286794")))
