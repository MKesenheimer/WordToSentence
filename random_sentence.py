#!/usr/bin/env python3
# -*- conding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import urllib

url = "https://www.csgenerator.com:443/de"
cookies = {"_ga": "GA1.2.1284025350.1602148485", "_gid": "GA1.2.1339863284.1602148485"}
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded", "Origin": "https://www.csgenerator.com", "Connection": "close", "Referer": "https://www.csgenerator.com/de", "Upgrade-Insecure-Requests": "1"}
data = {"randomButton": "Zufallss\xc3\xa4tze", "s": ''}
response = requests.post(url, headers=headers, cookies=cookies, data=data)
page = response.text

initial = BeautifulSoup(page, "html.parser")
text = initial.find('originalText', class_="content")
print(text)