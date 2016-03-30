class BankAccount:
    def __init__(self, name, balance, currency):
        if balance < 0:
            raise ValueError
        self._name = name
        self._balance = balance
        self._currency = currency
        self._history = ['Account was created']

    def __eq__(self, other):
        return self._currency == other._currency

    def get_name(self):
        return self._name

    def deposit(self, amount, froms=None):
        if amount <= 0:
            raise ValueError
        if froms is None:
            hist_dep = 'Deposited {}{}'
            self._history.append(hist_dep.format(amount, self._currency))
        else:
            hist_dep = 'Transfer from {} for {}{}'
            self._history.append(hist_dep.format(froms.get_name(), amount, self._currency))

        self._balance += amount

    def balance(self):
        hist_bal = 'Balance check -> {}{}'
        self._history.append(hist_bal.format(self._balance, self._currency))
        return self._balance

    def withdraw(self, amount, to=None):
        if amount <= self._balance:
            if to is None:
                hist_withraw = '{}{} withrawed'
                self._history.append(hist_withraw.format(amount, self._currency))
            else:
                hist_withraw = 'Transfer to {} for {}{}'
                self._history.append(hist_withraw.format(to.get_name(), amount, self._currency))
            self._balance -= amount
            return True
        return False

    def __str__(self):
        hist_str = 'Balance check -> {}{}'
        self._history.append(hist_str.format(self._balance, self._currency))
        return 'Bank account for {} with balance of {}{}'.format(self._name, self._balance, self._currency)

    def __int__(self):
        hist_int = '__int__ check -> {}{}'
        self._history.append(hist_int.format(self._balance, self._currency))
        return self._balance

    def transfer_to(self, other, amount):
        if self == other and self.withdraw(amount, other):
            other.deposit(amount, self)
            return True
        return False

    def history(self):
        return self._history
