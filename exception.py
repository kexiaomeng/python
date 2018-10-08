

class MyException(Exception):
    def __init__(self, length, atleast):
        self.length = length
        self.atleast = atleast

string = input("enter your string")

try:
    if (len(string) < 3):
        raise MyException(len(string), 3)
except MyException as x:
    print("my exception %d %d " % (x.length, x.atleast))
except:
    print("hello")
finally:
    print("this is the final yuju")