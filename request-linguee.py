#!/usr/bin/env python3
# linguee definition && examples scraper
import sys
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote_plus
from urllib.request import Request
import urllib
import ssl

whatWord = quote_plus(sys.argv[1])
lingueeLink = "https://www.linguee.de/deutsch-englisch/search?source=auto&query={}".format(whatWord)

# without proxy
#print(lingueeLink)
page = urlopen(lingueeLink)

# with proxy
#req = Request(lingueeLink)
#proxy_host = '<host>:<port>'
#req.set_proxy(proxy_host, 'http')
#context = ssl._create_unverified_context()
#page = urlopen(req, context=context)

initial = BeautifulSoup(page, "html.parser")

def define():
	definition = initial.find('a', class_="dictLink featured")
	if definition is not None:
		definition = initial.find('a', class_="dictLink featured").get_text()
	else:
		definition = "Word not found"
	return definition

example = initial.find('table', class_="result_table")
#print(example)
# left[0] in german ~ right[0] in english
left = [] # the german sentence array
right = [] # the corresponding english sentence array
rows = example.findAll("tr")
for row in rows:
	lefty = row.find('td', class_="sentence left")
	if lefty is None:
		lefty = row.find('td', class_="sentence left warn")
	link1 = (lefty.find('div', class_="source_url_spacer")).get_text()
	righty = row.find('td', class_="sentence right2")
	if righty is None:
		righty = row.find('td', class_="sentence right2 warn")
	link2 = (righty.find('div', class_="source_url_spacer")).get_text()
	left.append((lefty.get_text()).replace("\n", " ").replace(link1,"").replace("\r", ""))
	right.append((righty.get_text()).replace("\n", " ").replace(link2,"").replace("\r", ""))

lst = []
lst_insecure = []
for ex in left:
	if ex.find(whatWord) != -1:
		ex = ex.replace("[...]", "")
		for i in range(2):
			ex = ex.replace("  ", " ")
		lst.append(ex)
	else:
		ex = ex.replace("[...]", "")
		for i in range(2):
			ex = ex.replace("  ", " ")
		lst_insecure.append(ex)

if len(lst) != 0:
	sorted_lst = sorted(lst, key=len)
	print(sorted_lst[0])
elif len(lst_insecure) != 0:
	sorted_lst = sorted(lst_insecure, key=len)
	print(sorted_lst[0])
