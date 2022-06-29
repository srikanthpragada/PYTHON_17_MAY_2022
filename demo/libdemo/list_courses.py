from bs4 import BeautifulSoup

with open("courses.xml", "rt") as f:
    contents = f.read()

bs = BeautifulSoup(contents, 'lxml-xml')
courses = bs.find_all("course")

for course in courses:
    title = course.find("title").text

    duration_tag = course.find("duration")
    duration = int(duration_tag.text)
    dur_kind = duration_tag["kind"]

    fee_tag = course.find("fee")
    fee = int(fee_tag.text)
    if 'currency' in fee_tag.attrs:
        fee_currency = fee_tag["currency"]
    else:
        fee_currency = "INR"

    print(f"{title:50} {duration:3} {dur_kind.upper():5} {fee:6} {fee_currency.upper()}")
