class Rational:
    def __init__(self, numer=1, denom=1):
        self.numer = numer
        self.denom = denom
        self.simplify()

    @property
    def numer(self):
        return self.__numer

    @property
    def denom(self):
        return self.__denom

    @numer.setter
    def numer(self, value):
        if isinstance(value, (int, float)):
            self.__numer = value
        else:
            raise TypeError

    @denom.setter
    def denom(self, value):
        if isinstance(value, (int, float)) and value != 0:
            self.__denom = value
        elif not isinstance(value, (int, float)):
            raise TypeError
        elif value == 0:
            raise ZeroDivisionError
        else:
            raise Exception("An error occurred, that is not ZeroDivisionError or TypeError")

    def __level_fractions(self, other) -> None:  # level fractions to the same denominator
        x = self.denom
        y = other.denom
        self.numer *= y  # adjust to the same denominator
        self.denom *= y
        other.numer *= x
        other.denom *= x

    def __add__(self, other):
        if isinstance(other, Rational):
            self.__level_fractions(other)
            self.numer += other.numer
            self.simplify()  # make it clean and good-looking
            return self
        elif isinstance(other, (int, float)):
            self.numer += (other * self.denom)
            self.simplify()
            return self
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, Rational):
            self.__level_fractions(other)
            self.numer -= other.numer
            self.simplify()  # make it clean and good-looking
            return self
        elif isinstance(other, (int, float)):
            self.numer -= (other * self.denom)
            self.simplify()
            return self
        else:
            raise TypeError

    def __mul__(self, other):
        if isinstance(other, Rational):
            self.numer *= other.numer
            self.denom *= other.denom
            self.simplify()
            return self
        elif isinstance(other, (int, float)):
            self.numer *= other
            self.simplify()
            return self
        else:
            raise TypeError

    def __truediv__(self, other):
        if isinstance(other, Rational):
            other.numer, other.denom = other.denom, other.numer
            return self.__mul__(other)
        elif isinstance(other, (int, float)):
            self.denom *= other
            self.simplify()
            return self
        else:
            raise TypeError

    def __gt__(self, other):
        copy_self, copy_other = Rational.__copy_rational_instance(self, other)
        copy_self.__level_fractions(copy_other)
        return copy_self.numer > copy_other.numer

    def __ge__(self, other):
        copy_self, copy_other = Rational.__copy_rational_instance(self, other)
        copy_self.__level_fractions(copy_other)
        return copy_self.numer >= copy_other.numer

    def __lt__(self, other):
        copy_self, copy_other = Rational.__copy_rational_instance(self, other)
        copy_self.__level_fractions(copy_other)
        return copy_self.numer < copy_other.numer

    def __le__(self, other):
        copy_self, copy_other = Rational.__copy_rational_instance(self, other)
        copy_self.__level_fractions(copy_other)
        return copy_self.numer <= copy_other.numer

    @staticmethod
    def __copy_rational_instance(one, another):  # only used at comparing to make less of demanding simplify() calls
        if isinstance(one, Rational) and isinstance(another, Rational):
            copy_one = Rational(one.numer, one.denom)
            copy_another = Rational(another.numer, another.denom)
            return copy_one, copy_another
        else:
            raise TypeError

    def simplify(self):
        if not Rational.is_flat(self.numer) or not Rational.is_flat(self.denom):  # because you don't need more than
            # 3 digits of precision, float support for this class is a nuisance anyway
            self.numer *= 1000
            self.numer = int(self.numer)
            self.denom *= 1000
            self.denom = int(self.denom)
        gcd = self.euclidean()
        self.numer //= gcd
        self.denom //= gcd

    def euclidean(self):  # find the greatest common divisor using euclidean algorithm
        a = max(self.numer, self.denom)
        b = min(self.numer, self.denom)
        while a != 0 and b != 0:
            (a, b) = (b, a % b)
        return max(a, b)

    @staticmethod
    def is_flat(number):  # checks if number is an integer (even if float-type)
        if isinstance(number, int):
            return True
        elif isinstance(number, float):
            return number.is_integer()
        elif not isinstance(number, (int, float)):  # yes it does support an str-type number
            return Rational.is_flat(float(number))
        else:
            return False

    def trad(self):  # traditional form printout
        return str(int(self.numer)) + "/" + str(int(self.denom))

    def floating(self):  # floating-point form printout
        return self.numer / self.denom

