l = [10, -20, 30, -33, 44]

for n in map(abs, l):
    print(n)

marks = ['98', '37', '88', '67']

# print(sum(marks))
print(sum(map(int, marks)))


def hasdigit(st: str) -> bool:
    for c in st:
        if c.isdigit():
            return True

    return False


def getnumber(st):
    n = ""
    for c in st:
        if c.isdigit():
            n += c

    return int(n)


codes = ['AB93', 'X373', 'V393', 'XY']
valid_codes = filter(hasdigit, codes)
for n in map(getnumber, valid_codes):
    print(n)
