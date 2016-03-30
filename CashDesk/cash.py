class Bill:
    def __init__(self, amount):
        if type(amount) != int:
            raise TypeError
        if amount < 0:
            raise ValueError
        self.amount = amount

    def __str__(self):
        return 'A {}$ bill'.format(self.amount)

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return self.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return hash(self.amount)

    def total(self):
        return self.__int__()

    def __len__(self):
        return 1


class BatchBill:
    def __init__(self, bills):
        self.bills = bills

    def __len__(self):
        return len(self.bills)

    def total(self):
        return sum(int(bill) for bill in self.bills)

    def __getitem__(self, index):
        return self.bills[index]




class CashDesk:
    def __init__(self):
        self.money = []

    def take_money(self, money):
        self.money.append(money)

    def total(self):
        return sum(mon.total() for mon in self.money)

    def inspect(self):
        a = {}
        for bill in self.money:
            print(len(bill))
            if len(bill) > 1:
                for b in bill:
                    print(b)
                    a[b] = 0
            elif len(bill) == 1:
                print(bill)
                a[bill] = 0

        for bill in self.money:
            if len(bill) > 1:
                for b in bill:
                    a[b] += 1
            else:
                a[bill] += 1
        return a
