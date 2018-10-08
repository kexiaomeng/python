def fun():
    for i in range(20):
     x = yield i
     print('good', x)



def htest():
    i = 1
    while i < 4:
        n = yield i
        if i == 3:
            return 100
        i += 1


def itest():
    val = yield from htest()
    print("hello")
    print(val)

t = itest()
t.send(None)
j = 0
while j < 3:
    j += 1
    try:
        t.send(j)
    except StopIteration as e:
        print('异常了')
# if __name__ == '__main__':
#
#     a = fun()
#     for x in a:
#         print(x)


def g1(x):
    yield range(x)


def g2(x):
    yield from range(x)


it1 = g1(5)
it2 = g2(5)

print([x for x in it1])
# out [range(0, 5)]
print([x for x in it2])
# out [0, 1, 2, 3, 4]


import time


def func(n):
    yield from range(0, n)
    print('func:')
#
# def func(n):
#     for i in range(0, n):
#         arg = yield i
#         print("dddddddddddd")

f = func(10)
while True:
    try:
        print('main:', next(f))
        # print('main:', f.send(100))
        time.sleep(1)
    except StopIteration:
        exit()
        print("endddddddddddddd")
    finally:
        print("finally")
        #
