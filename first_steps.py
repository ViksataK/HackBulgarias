def sum_of_digits(digits):
    digits = to_digits(digits)
    result = 0
    for x in digits:
        result += int(x)
    return result


def to_digits(n):
    result = []
    n = abs(n)
    for a in str(n):
        result.append(int(a))
    return result


def to_number(digits):
    result = ''
    for a in digits:
        result += str(a)
    return int(result)


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def fact_digits(n):
    arr = to_digits(n)
    result = 0
    for a in arr:
        result += factorial(int(a))
    return result


def fibonacci_num(n):
    if n <= 2:
        return 1
    else:
        return fibonacci_num(n - 1) + fibonacci_num(n - 2)


def fibonacci(n):
    result = []
    for i in range(1, n+1):
        result.append(fibonacci_num(i))
    return result


def fib_number(n):
    result = ''
    for i in range(1, n + 1):
        result += str(fibonacci_num(i))
    return int(result)


def palindrome(st):
    st = str(st)
    return st == st[::-1]


def count_vowels(st):
    count = 0
    for x in st.lower():
        if x in "aeiouy":
            count += 1
    return count


def count_consonants(st):
    count = 0
    for x in st.lower():
        if x in "bcdfghjklmnpqrstvwxz":
            count += 1
    return count


def char_histogram(string):
    hist = {x: 0 for x in string}
    for x in string:
        hist[x] += 1
    return hist
