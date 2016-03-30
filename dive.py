import copy


def is_number_balanced(n):
    middle = len(str(n)) // 2
    sum1 = 0
    sum2 = 0
    if len(str(n)) % 2 != 0:
        for i in range(0, middle):
            sum1 += int(str(n)[i])
        for i in range(middle + 1, len(str(n))):
            sum2 += int(str(n)[i])
    else:
        for i in range(0, middle):
            sum1 += int(str(n)[i])
        for i in range(middle, len(str(n))):
            sum2 += int(str(n)[i])

    return sum1 == sum2


def is_increasing(seq):
    for i in range(0, len(seq) - 1):
        if seq[i] >= seq[i + 1]:
            return False
    return True


def is_decreasing(seq):
    for i in range(0, len(seq) - 1):
        if seq[i] <= seq[i + 1]:
            return False
    return True


def is_palindrome(obj):
    return str(obj) == str(obj)[::-1]


def get_largest_palindrome(n):
    for i in range(n - 1, 0, -1):
        if is_palindrome(i) is True:
            return i


def prime_numbers(n):
    prime = []
    not_prime = []
    for i in range(2, n + 1):
        if i not in not_prime:
            prime.append(i)
            for j in range(i * i, n + 1, i):
                not_prime.append(j)
    return prime


def prime_sieve(n):
    all_num = [x for x in range(2, n + 1)]
    for i in range(2, n + 1):
        not_prime = [x for x in range(i * 2, n + 1, i)]
        all_num = set(all_num) - set(not_prime)

    return sorted(list(all_num))


def remove_first(x, string):
    chars = [ch for ch in string]
    if x in chars:
        chars.remove(x)

    return "".join(chars)


def is_anagram(a, b):
    if len(a) != len(b):
        return False
    for i in a.lower():
        if i not in b.lower():
            return False
        if i in b.lower():
            b = remove_first(i, b)
    return True


def birthday_ranges(birthdays, ranges):
    result = []
    for range in ranges:
        sum = 0
        for day in birthdays:
            if day >= range[0] and day <= range[1]:
                sum += 1
        result.append(sum)
    return result


def sum_matrix(m):
    sum = 0
    for x in m:
        for y in x:
            sum += y
    return sum


AROUND = [
            (-1, -1), (-1, -1), (0, -1), (1, -1),
            (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)
        ]


def get_around(row, col):
    ar = [
        (row - 1, col - 1), (row, col - 1), (row + 1, col - 1),
        (row - 1, col), (row + 1, col),
        (row - 1, col + 1), (row, col + 1), (row + 1, col + 1)
    ]
    return ar


def within_bounds(m, at):
    if at[0] < 0 or at[0] >= len(m) or at[1] < 0 or at[1] >= len(m[0]):
        return False
    return True


def matrix_bombing_plan(m):
    d = {}
    for i in range(len(m)):
        for j in range(len(m[0])):
            temp = copy.deepcopy(m)
            indexes = (i, j)
            dmg = m[i][j]
            neighbours = get_around(i, j)
            for x in neighbours:
                if within_bounds(temp, x):
                    if temp[x[0]][x[1]] <= dmg:
                        temp[x[0]][x[1]] = 0
                    else:
                        temp[x[0]][x[1]] -= dmg
            d[indexes] = sum_matrix(temp)
    return d


def is_transversal(transversal, family):
    for group in family:
        it = [x for x in group if x in transversal]
        if len(it) == 0 or len(it) > 1:
            return False
    return True
