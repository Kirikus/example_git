"""Fibonacci series module."""


fibonacci_array = [0, 1]

def fibonacci(n: int) -> int:
    """Fibonacci series.

    :param n: fibonacci number to return.
    :return: n-th fib. number.
    """
    if n < 0:
        print("Incorrect input")

    if n < len(fibonacci_array):
        return fibonacci_array[n]

    for _ in range(n - len(fibonacci_array) + 1):
        fibonacci_array.append(fibonacci_array[-1] + fibonacci_array[-2])
    print(fibonacci_array)
    return fibonacci_array[-1]


if __name__ == "__main__":
    print(fibonacci(9))
