from datetime import datetime
import time


def accepts(*args):
    def accepter(func):
        def decorated(*args2):
            if type(args2[0]) != args[0]:
                raise TypeError
            if len(args2) > 1:
                a = [(x, y) for x in args for y in args2]
                for x in a:
                    if type(x[1]) != args[0]:
                        raise TypeError
            return func(*args2)
        return decorated
    return accepter


def log(filename):
    def accepter(func):
        def decorated():
            with open(filename, 'a') as f:
                f.write('{} was called at {}\n'.format(func.__name__, datetime.now()))
            return func()
        return decorated
    return accepter


def encrypt(key):
    def accepter(func):
        def decorated():
            asd = [chr(ord(ch) + key) if ch is not ' ' else ch for ch in func()]
            return ''.join(asd)
        return decorated
    return accepter


def performance(filename):
    def accepter(func):
        def decorated():
            ts = time.time()
            result = func()
            te = time.time()
            with open(filename, 'a') as f:
                f.write('{} was called and took {} seconds to complete\n'.format(func.__name__,
                                                                                 te - ts))
            return result
        return decorated
    return accepter

