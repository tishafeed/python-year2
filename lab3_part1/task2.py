class Calendar:
    def __init__(self, dd, mm, year):
        self.year = year
        self.mm = mm
        self.dd = dd
        self.max_day = self.__get_max_day()

    def __get_max_day(self):  # find the maximum allowed day value of a Calendar object by its month value
        months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        months_leap = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        if self.year % 400 == 0:  # leap end of century years must be divisible by 400
            maximum_day = months_leap[self.mm]
        elif self.year % 4 == 0 and self.year % 100 != 0:  # if divisible by 4 and not end-of-century year
            maximum_day = months_leap[self.mm]
        else:  # for non-leap years
            maximum_day = months[self.mm]
        return maximum_day

    @property
    def dd(self):
        return self.__dd

    @dd.setter
    def dd(self, val):
        if isinstance(val, int):
            self.__dd = val
            if val not in range(1, self.max_day+1):
                Calendar.__correct_day(self)
        else:
            raise TypeError

    @property
    def mm(self):
        return self.__mm

    @mm.setter
    def mm(self, val):
        if isinstance(val, int):
            self.__mm = val
            if self.mm in range(1, 13):
                self.max_day = self.__get_max_day()  # every time month changes we will keep record of its maximum day
            else:
                Calendar.__correct_month(self)
        else:
            raise TypeError

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, val):
        if isinstance(val, int):
            if val > 0:
                self.__year = val
            else:
                raise ValueError("Year value cannot be negative or zero")
        else:
            raise TypeError

    @staticmethod
    def __correct_month(obj):
        if obj.mm > 12:
            obj.year += 1
            obj.mm -= 12
        elif obj.mm < 1:
            obj.year -= 1
            obj.mm += 12

    @staticmethod
    def __correct_day(obj):
        if obj.dd > obj.max_day:
            obj.dd -= obj.max_day
            obj.mm += 1
        elif obj.dd < 1:
            obj.mm -= 1
            obj.dd += obj.max_day

    def __add__(self, other):
        if isinstance(other, Calendar):
            self.year += other.year
            self.mm += other.mm
            self.dd += other.dd
            return self
        elif isinstance(other, tuple):
            self.year += other[2]
            self.mm += other[1]
            self.dd += other[0]
            return self
        else:
            raise TypeError('\'other\' was not of Calendar or tuple type')

    def __sub__(self, other):
        if isinstance(other, Calendar):
            self.year -= other.year
            self.mm -= other.mm
            self.dd -= other.dd
            return self
        elif isinstance(other, tuple):
            self.year -= other[2]
            self.mm -= other[1]
            self.dd -= other[0]
            return self
        else:
            raise TypeError('\'other\' was not of Calendar or tuple type')

    def __eq__(self, other):
        if not isinstance(other, Calendar):
            raise TypeError('\'other\' is not of Calendar type')
        elif isinstance(other, Calendar) and self.__dict__ == other.__dict__:
            return True
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        if not isinstance(other, Calendar):
            raise TypeError('\'other\' is not of Calendar type')
        else:
            if self.year > other.year:
                return True
            elif self.year == other.year and self.mm > other.mm:
                return True
            elif self.year == other.year and self.mm == other.mm and self.dd > other.dd:
                return True
            else:
                return False

    def __lt__(self, other):
        if not isinstance(other, Calendar):
            raise TypeError('\'other\' is not of Calendar type')
        else:
            if self.year < other.year:
                return True
            elif self.year == other.year and self.mm < other.mm:
                return True
            elif self.year == other.year and self.mm == other.mm and self.dd < other.dd:
                return True
            else:
                return False

    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def __str__(self):
        return f"{self.dd}/{self.mm}/{self.year}"
