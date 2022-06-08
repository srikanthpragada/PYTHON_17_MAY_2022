# Math functions

def iseven(n):
    """
    Checks whether the given number is even!
    :param n: number to check
    :return: True if number is even otherwise false
    """
    return n % 2 == 0


def ispositive(n):
    return n > 0


def isprime(n):
    pass


# Do not execute this code when imported
if __name__ == '__main__':
    print(iseven(11), iseven(10))
    print(ispositive(11), ispositive(-10))
