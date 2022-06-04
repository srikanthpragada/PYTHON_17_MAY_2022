def math_op(a, b, operation):
    return operation(a, b)


def add(a, b):
    return a + b


def mul(a, b):
    return a * b


print(math_op(10, 20, add))
print(math_op(10, 10, mul))
print(math_op(10, 10, len))  # Throws error
