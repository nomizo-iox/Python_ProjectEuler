"""Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2,
the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ... By considering the terms in the Fibonacci sequence
whose values do not exceed four million, find the sum of the even-valued terms. """


def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def solution():
    ans = 0
    i = 1
    while fibonacci(i) <= 6000000:
        if fibonacci(i) % 2 == 0:
            ans += fibonacci(i)
        i += 1
    print(ans)


if __name__ == '__main__':
    solution()