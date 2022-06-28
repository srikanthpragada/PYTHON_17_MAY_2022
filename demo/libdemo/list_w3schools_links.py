WEBSITE = "https://www.w3schools.com"

from bs4 import BeautifulSoup
import requests

resp = requests.get(WEBSITE)
if resp.status_code != 200:
    print(f"Sorry! Could not access website : {WEBSITE}")
    exit(1)

contents = resp.text
bs = BeautifulSoup(contents, 'html.parser')
links = bs.find_all("a")

for link in links:
    text = link.text.strip()
    url = link['href']
    if url == '#':
        continue

    if len(text) == 0:
        continue

    if 'javascript:void' in url:
        continue

    if not url.startswith('http'):
        url = WEBSITE + "//" + url  # Convert relative url to absolute


    print(text)
    print(url)
    print("-" * 80)
