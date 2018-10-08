

class Fib():
    def  __init__(self):
        self.__start = 0
        self.__cur = 1

    def __next__(self):
        self.value = self.__cur
        self.__cur += self.__start
        self.__start = self.value
        return self.value

    def __iter__(self):
        return self

from itertools import islice

f = Fib()


print()

print(list(islice(f, 0, 10)))