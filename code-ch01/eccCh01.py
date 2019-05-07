from unittest import TestCase

class FieldElement:

    def __init__(self, num, prime):
        if num >= prime or num < 0:  # <1>
            error = 'Num {} not in field range 0 to {}'.format(
                num, prime - 1)
            raise ValueError(error)
        self.num = num  # <2>
        self.prime = prime

    def __repr__(self):
        return 'FieldElement_{}({})'.format(self.prime, self.num)

    def __eq__(self, other):
        #if other wasn't given (None), then the function should return false
        #if all elements of self and other are equal, return true
        raise NotImplementedError

    def __ne__(self, other):
        # this should be the inverse of the == operator
        raise NotImplementedError

    def __add__(self, other):
        #Should raise a TypeError() if two numbers are in different fields
        #Use finite field addition
        raise NotImplementedError

    def __sub__(self, other):
        #Should raise a TypeError() if two numbers are in different fields
        # self.num and other.num are the actual values
        # self.prime is what we need to mod against
        # We return an element of the same class
        raise NotImplementedError

    def __mul__(self, other):
        #Should raise a TypeError() if two numbers are in different fields
        # self.num and other.num are the actual values
        # self.prime is what we need to mod against
        # We return an element of the same class
        raise NotImplementedError

    def __pow__(self, exponent):
        # implement exponents
        return self.__class__(num, self.prime)

    def __truediv__(self, other):
        #Should raise a TypeError() if two numbers are in different fields
        # use fermat's little theorem:
        # self.num**(p-1) % p == 1
        # this means:
        # 1/n == pow(n, p-2, p)
        # We return an element of the same class
        raise NotImplementedError
