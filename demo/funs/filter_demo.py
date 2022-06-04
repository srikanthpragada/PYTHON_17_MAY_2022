def iseven(n) -> bool:
    return n % 2 == 0


l = [10, 11, 34, 45, 55]

for n in filter(iseven, l):
    print(n)

for c in filter(str.isupper, 'AbcXyz'):
    print(c)


def hasdigit(st : str) -> bool:
    for c in st:
        if c.isdigit():
            return True

    return False


for s in filter(hasdigit, ['abc', '392', 'ab12', 'def']):
    print(s)
