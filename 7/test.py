from typing import Any, Union


class Fraction:

    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __str__(self):
        return '{}/{}'.format(self.numer, self.denom)



    def __add__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.numer*other.denom + other.numer*self.denom, self.denom*other.denom)
        else:
            new_other = Fraction(other, 1)
            new_obj = self + new_other
        return new_obj

    def __sub__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.numer*other.denom - other.numer*self.denom, self.denom*other.denom)
        else:
            new_other = Fraction(other, 1)
            new_obj = self - new_other
        return new_obj

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.numer*other.numer, self.denom*other.denom)
        else:
            new_other = Fraction(other, 1)
            new_obj = self * new_other
        return new_obj

    def __int__(self):
        return int(self.numer/self.denom)

    def __float__(self):
        return float(self.numer/self.denom)

class OperationFraction(Fraction):
    def __init__(self, numer, denom):
        super().__init__(numer=numer, denom=denom)

    def getint(self):
        # super().__int__()
        return int(self.numer/self.denom)

    def getfloat(self):
        return float(self.numer/self.denom)


frac1 = Fraction(1, 4)
frac2 = Fraction(1, 4)

print(frac1 - frac2)
print(float(frac1))
print('-'*10)

frac3 = OperationFraction(8, 4)

print(frac3.getint())