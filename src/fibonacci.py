"""Fibonacci series module."""



def fibonacci(n: int) -> int:
    """Fibonacci series.

    :param n: fibonacci number to return.
    :return: n-th fib. number.
    """
    a = 0
    b = 1

    if n < 0:
        raise ValueError('Fibonacci series can not be negative.')

    elif n == 0:
        return 0

    elif n == 1:
        return b
    for _ in range(1, n):
        c = a + b
        a = b
        b = c
    return b


if __name__ == "__main__":
    print(fibonacci(9))
