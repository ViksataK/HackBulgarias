def count_words(arr):
    result = {x: 0 for x in arr}
    for x in arr:
        result[x] += 1
    return result


def nan_expand(times):
    result = []
    if times != 0:
        for i in range(times):
            result.append('Not a ')
        result.append('NaN')
    return ''.join(result)


def iterations_of_nan_expand(expanded):
    i = 0
    for i in range(len(expanded)):
        if expanded == nan_expand(i):
            return i
        else:
            i += 1
    return False


def group(items):
    result = [items[0]]
    al = []
    for i in range(1, len(items)):
        if items[i] in result:
            result.append(items[i])
        else:
            al.append(result)
            result = []
            result.append(items[i])
    al.append(result)
    return al


def max_consecutive(items):
    groups = group(items)
    maxim = 0
    for x in groups:
        if len(x) > maxim:
            maxim = len(x)
    return maxim


def gas_stations(distance, tank_size, stations):
    left_gas = tank_size
    result = [0]
    for i in range(len(stations) - 1):
        if stations[i + 1] - stations[i - 1] >= left_gas:
            result.append(stations[i])
            left_gas = tank_size
        else:
            left_gas = left_gas - (stations[i + 1] + stations[i - 1])
    if left_gas < distance - result[-1]:
        result.append(stations[-1])
    return result[1:]


def sum_of_numbers(st):
    suma = 0
    l = ''
    result = []
    for x in st:
        if x in "0123456789":
            l += x
        elif l != '':
            result.append(l)
            l = ''
    result.append(l)
    return suma

buttons = [
            [],
            [],
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i'],
            ['j', 'k', 'l'],
            ['m', 'n', 'o'],
            ['p', 'q', 'r', 's'],
            ['t', 'u', 'v'],
            ['w', 'x', 'y', 'z'],
        ]


def get_letter(key, lenght):
    result = ''
    if key == 0:
        for i in range(lenght + 1):
            result += " "
        return result
    return buttons[key][lenght]


def correct_index(i, value):
    if value == 7 or value == 9:
        return i % 4
    else:
        return i % 3


def numbers_to_message(sequence):
    grouped_numbers = group(sequence)
    result = ''
    cap = False
    for g in grouped_numbers:
        key = g[0]
        index = correct_index(len(g) - 1, key)

        if key == -1:
            continue
        elif key == 1:
            cap = True
        else:
            if not cap:
                result += get_letter(key, index)
            else:
                result += get_letter(key, index).upper()
                cap = False
    return result



def message_to_numbers(message):
    result = []
    for x in message:
        if x == ' ':
            result.append(0)
        else:
            for i in range(len(buttons)):
                if x in buttons[i]:
                    result.append(i)
                    
    return result
