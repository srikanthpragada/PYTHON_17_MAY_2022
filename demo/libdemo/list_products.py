from bs4 import BeautifulSoup

f = open("products.html", "rt")
contents = f.read()
f.close()

bs = BeautifulSoup(contents, "html.parser")
print(bs.h1.text)
products = bs.find_all("li")
for prod in products:
    name, price = prod.text.split(",")
    print(f"{name:20} {float(price):10.2f}")
