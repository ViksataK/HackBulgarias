class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def format_it(self):
        for x in range(abs(self.numerator), 1, -1):
            if self.numerator % x == 0 and self.denominator % x == 0:
                self.numerator = int(self.numerator / x)
                self.denominator = int(self.denominator / x)

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        return "{} / {}".format(self.numerator, self.denominator)

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        den = self.denominator * other.denominator
        num = other.denominator * self.numerator + \
            self.denominator * other.numerator
        neww = Fraction(num, den)
        neww.format_it()
        return neww

    def __sub__(self, other):
        den = self.denominator * other.denominator
        num = other.denominator * self.numerator - \
            self.denominator * other.numerator
        neww = Fraction(num, den)
        neww.format_it()
        return neww

    def __mul__(self, other):
        den = self.denominator * other.denominator
        num = self.numerator * other.numerator
        neww = Fraction(num, den)
        neww.format_it()
        return neww

    def __eq__(self, other):
        self.format_it()
        other.format_it()
        return self.numerator == other.numerator and self.denominator == other.denominator
