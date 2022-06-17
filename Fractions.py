"""
A python module that allows for the creation and application of a new datatype called Fractions, developed by yours truly Ian Patrick M. Tan
"""

def fraction(x:'Takes in any number (can be a string as well)') -> 'Returns a fraction equivalent of input value':
    """
    Converts most other data types (e.g. int, str, float) into a Fraction datatype
    """
    try:
        x = eval(x)
    except:
        pass
    denominator, numerator, a = 0, 0, type(x)
    if a == int:
        denominator, numerator = x, 1
    if a == float:
        b = str(x)
        c = len(b) - b.index('.') - 1
        d = 10 ** c
        denominator, numerator = x * d, d
    if a == str:
        b = x.replace(' ', '').split('/')
        denominator, numerator = int(b[0]), int(b[1])
    if a == Fraction:
        denominator, numerator = x.denominator, x.numerator
    return simplify(Fraction(denominator, numerator))

def simplify(x:'Takes in any fraction') -> 'Returns simplified Fraction':
    """
    Simplifies a Fraction datatype
    """
    a, b = x.denominator, x.numerator
    while b:
        a, b = b, a % b
    return Fraction(x.denominator / a, x.numerator / a)

class Fraction:
    """
    It's a fraction.
    You can use it like this:
        Fraction(10)
        Fraction(0.5)
        Fraction('10 / 2')
        Fraction('420       /69')
        Fraction(10, 21)
        Fraction(2 / 5)

    Bruh
    """
    def __init__(self, a, b = None):
        if b == None:
            f = fraction(a)
            self.denominator, self.numerator = f.denominator, f.numerator
        else:
            self.denominator, self.numerator = a, b
        a, b = self.denominator, self.numerator
        while b:
            a, b = b, a % b
        self.denominator, self.numerator = self.denominator / a, self.numerator / a
        
    
    def __repr__(self):
        return f'{int(self.denominator)} / {int(self.numerator)}'
    
    def __int__(self):
        return int(self.denominator / self.numerator)
    
    def __float__(self):
        return self.denominator / self.numerator
    
    def __str__(self):
        return f'{int(self.denominator)} / {int(self.numerator)}'

    def __add__(self, value):
        a, b = self, fraction(value)
        return simplify(Fraction(a.denominator * b.numerator + b.denominator * a.numerator, a.numerator * b.numerator))
    
    def __sub__(self, value):
        a, b = self, fraction(value)
        return simplify(Fraction(a.denominator * b.numerator - b.denominator * a.numerator, a.numerator * b.numerator))
    
    def __mul__(self, value):
        a, b = self, fraction(value)
        return simplify(Fraction(a.denominator * b.denominator, a.numerator * b.numerator))

    def __truediv__(self, value):
        a, b = self, fraction(value)
        return simplify(Fraction(a.denominator * b.numerator, a.numerator * b.denominator))
    
    def __pow__(self, value):
        a, b = self, fraction(value)
        return Fraction((a.denominator ** b.denominator) ** (1 / b.numerator)) / Fraction((a.numerator ** b.denominator) ** (1 / b.numerator))