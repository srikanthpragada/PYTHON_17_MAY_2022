WEBSITE = "http://www.srikanthtechnologies.com"

from bs4 import BeautifulSoup
import requests
from datetime import datetime

resp = requests.get(WEBSITE)
if resp.status_code != 200:
    print(f"Sorry! Could not access website : {WEBSITE}")
    exit(1)

contents = resp.text
bs = BeautifulSoup(contents, 'html.parser')
table = bs.find(id="ctl00_ContentPlaceHolder1_GridView2")

rows = table.find_all("tr")[1:]

for row in rows:
    cols = row.find_all("td")
    name = cols[0].text
    timings = cols[1].text
    today = datetime.now()
    try:
        stdate = cols[2].text + "-" + str(today.year)
        startdate = datetime.strptime(stdate, "%d-%b-%Y")
        days = (startdate.date() - today.date()).days
        if days >= 0:
            msg = "day(s) to go"
        else:
            msg = "day(s) old"
        print(f"{name:50} {timings:20} {abs(days):2} {msg}")
    except:
        print(f"{name:50} {timings:20}")
