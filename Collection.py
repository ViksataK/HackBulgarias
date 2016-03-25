class Enumerable:
    def take(self, n):
        pass

    def drop(self, n):
        pass

    def take_while(self, predicate):
        pass

    def drop_while(self, predicate):
        pass

    def map(self, callable):
        pass

    def filter(self, predicate):
        pass

    def reduce(self, start_value, operator):
        pass

    # Returns True, if value is in self
    def search(self, value):
        return value in self.arg


class Collection(Enumerable):
    def __init__(self, *args):
        self.arg = args
        self.max = len(args)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.max:
            raise StopIteration
        else:
            self.index += 1
            return self.arg[self.index - 1]

    def __eq__(self, other):
        return self.arg == other.arg


c = Collection(1, 2, 7, 4, 5, 7, 2)
for s in c:
    print(s)
for s in c:
    print(s)
print(c.search(2))
