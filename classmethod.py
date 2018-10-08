import time


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


a = Date(2012, 12, 12)
b = Date.today()
c = Date.__new__(Date)

print(a.__dict__)
print(b.__dict__)
print(c.__dict__)

d = {'year':2015, 'month':10, 'day':29}

for key, value in d.items():
    setattr(c, key, value)

print(c.__dict__)