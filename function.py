
def multiple(*num):

    for nu in num:
        print(nu)


def keyWordParam(*arg, **args):
    print(arg)
    print(args)


def add(x:int, y:int) ->int :    #参数注释  参数名:注释   返回值注释  ：-> 注释
    print(x,y)


def recv(maxSize, *mes, block):
    print(block)

def manyNumber():
    return (1, 2, 3)


_no_value = object()

def defaultParam(a, b = _no_value):
    if b is _no_value:
        print("no param trans to this function")
    else:
        print('param has tran to this functio')


def particaltest(a, b, c, d, e):
    print(a,b,c,d,e)


class Proxy:
    def hello(self):
        print("hello proxy")


class ProxyTest:
    def __init__(self):
        self._a = Proxy()

    def __getattr__(self, item):
        return getattr(self._a, item)


if __name__ == '__main__':
    print("多个参数")
    multiple('hello','world')

    print("关键字参数")
    keyWordParam(1, 2, name = 'sun', age = 18)

    print("只接受关键字参数")
    recv(10, True, block=True)

    help(recv(10, True, block=True))

    print('t函数注解')

    add('helo', 'world')


    print(add.__annotations__)

    print('返回多个值')

    A,B,B = manyNumber()

    print(A)

    defaultParam('hello')
    defaultParam('hello', 'world')

    print('lambda 表达式')
    add = lambda x,y :x+y
    print(add(1,2))

    x = 10
    a = lambda y:x+y



    x = 20
    b = lambda y:x+y

    print(a(10))

    print(b(10))

    # partical()给某些参数预先赋值，减少调用函数的参数数量
    from functools import partial

    s = partial(particaltest,2)
    s(26,3,4,5)
    print(keyWordParam.__name__)

    print("代理测试")

    proxyTest = ProxyTest()

    proxyTest.hello()
