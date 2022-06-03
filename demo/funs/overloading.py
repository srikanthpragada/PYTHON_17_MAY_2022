# Overloading

def add(a, b):
    return a + b


add2 = add
print(id(add))


def add(a, b, c):
    return a + b + c


print(id(add))

print(add2(10, 20))
print(add(10, 20, 30))
