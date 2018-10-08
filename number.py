
#简单的舍入运算

num1 = round(1.23,1) #保留1位小数  当一个数处于中间的时候round函数返回离它最近的偶数  例如1.5  和2.5都返回2
num2 = round(1.27,1)
num3 = round(1.345,1)

print(num1)
print(num2)
print(num3)

x = 1.23456

print(format(x, '0.2f'))

print('values is {:0.3f} 0.3f'.format(x))


from decimal import Decimal

a= 4.2
b = 2.1
print(a+b)

a = Decimal('4.2')

b = Decimal('2.1')

c = a+b
print(c)


class Test:
    def __enter__(self):
        return "hello world"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type, exc_val, exc_tb)
        return True


def getTest():
    return Test()

with getTest() as test:     #with as  相当于try finally语句块
    print(test)
    raise  Exception("eeeeeeeeeeee")


import datetime

now  = datetime.datetime.today()

print(now)


text = "2012-3-6"

print(datetime.datetime.strptime(text, '%Y-%m-%d'))

print(datetime.datetime.strftime(now, '%Y-%m-%d'))