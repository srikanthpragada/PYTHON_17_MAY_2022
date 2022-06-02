def iseven(n: int) -> bool:
    return n % 2 == 0


def count_digits(s):
    count = 0
    for c in s:
        if c.isdigit():
            count += 1

    return count


print(iseven(10))
print(iseven(11))
print(count_digits('Abc123Xyz789'))
