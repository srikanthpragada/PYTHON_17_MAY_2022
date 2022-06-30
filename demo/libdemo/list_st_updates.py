URL = "http://www.srikanthtechnologies.com/rss.xml"

from bs4 import BeautifulSoup
import requests

resp = requests.get(URL)
if resp.status_code != 200:
    print(f"Sorry! Could not access website : {URL}")
    exit(1)

contents = resp.text
bs = BeautifulSoup(contents, 'lxml-xml')
items = bs.find_all("item")

for item in items:
   title = item.find("title").text.strip()
   link = item.find("link").text.strip()
   pubdate = item.find("pubDate").text
   if '2022' in pubdate:
       print(title)
       print(link)
       print('-'  * 80)

