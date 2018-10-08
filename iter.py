import  itertools

items = [1, 2, 3]

it = iter(items)

# print(next(it))


class Node:
    def __init__(self, value):
        self.__value = value
        self.__children = []

    def __str__(self):
        return 'Node({!r})'.format(self.__value)

    def addChild(self, node):
        self.__children.append(node)

    def __iter__(self):
        return iter(self.__children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()

    def __reversed__(self):    #定义此函数可以实现反向迭代
        n = len(self.__children)
        while n >= 1:
            yield self.__children[n-1]
            n -= 1


def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


def count():
    n = 0

    while True:
        yield n
        n += 1


from collections import defaultdict


def iterate_index():
    my_list = ['a', 'b', 'c']
    for idx, val in enumerate(my_list):
        print(idx, val)
    # 索引从1开始
    for idx, val in enumerate(my_list, 1):
        print(idx, val)

    # 序列中含有元组的解压
    data = [ (1, 2), (3, 4), (5, 6), (7, 8) ]
    for n, (x, y) in enumerate(data):
        print(n)
        print(x, y)


def parse_data(filename):
        with open(filename, 'rt') as f:
            for lineno, line in enumerate(f, 1):
                fields = line.split()
                try:
                    count = int(fields[1])
                    # ...
                except ValueError as e:
                    print('Line {}: Parse error: {}'.format(lineno, e))


def word_lines():
    word_summary = defaultdict(list)
    with open('myfile.txt', 'r') as f:
        lines = f.readlines()
    for idx, line in enumerate(lines):
        # Create a list of words in current line
        words = [w.strip().lower() for w in line.split()]
        for word in words:
            word_summary[word].append(idx)


from itertools import zip_longest

def iterate_simul():
    xpts = [1, 5, 4, 2, 10, 7]
    ypts = [101, 78, 37, 15, 62, 99]
    t =  zip(xpts, ypts)
    print(t)
    for x,y in t:
        print(x,y)

    a = [1, 2, 3]
    b = ['w', 'x', 'y', 'z']
    for i in zip(a,b):
        print(i)  # 默认是按最短长度
    for i in zip_longest(a,b):
        print(i)
    for i in zip_longest(a, b, fillvalue=0):   #fillvalue 若不能匹配的填充值
        print(i)

    headers = ['name', 'shares', 'price']
    values = ['ACME', 100, 490.1]
    s = dict(zip(headers,values))

    for name, val in zip(headers, values):
        print(name, '=', val)

    for x in itertools.chain(headers, value):
        print(x)


import collections

def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, collections.Iterable) and not isinstance(x, ignore_types):   #isinstance 判断是否是一个对象的实例
            yield from flatten(x)
        else:
            yield x


def flatten_seq():
    items = [1, 2, [3, 4, [5, 6], 7], 8]
    # Produces 1 2 3 4 5 6 7 8
    for x in flatten(items):
        print(x)
    items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
    for x in flatten(items):
        print(x)


import sys


def process_data(data):
    print(data)


def reader(s, size):
    while True:
        data = s.recv(size)
        if data == b'':
            break
            # process_data(data)


def reader2(s, size):
    for data in iter(lambda: s.recv(size), b''):
        process_data(data)


def iterate_while():
    CHUNKSIZE = 8192
    with open('sun.txt') as f:
        for chunk in iter(lambda: f.read(100), ''):
            # print("heloloooo")
            n = sys.stdout.write(chunk)
            print(n)


if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)

    child1.addChild(Node(3))
    child1.addChild(Node(4))
    child2.addChild(Node(5))

    root.addChild(child1)
    root.addChild(child2)

    for ch in root.depth_first():
        print(ch)

    print("************")
    for rr in reversed(root):
        print(rr)
    # list1 = frange(0,5,1)
    #
    # print(list(list1))



    print("迭代器切片")
    list = itertools.islice(count(), 10, 20)

    for x in list:
        print(x)

    list = ['a', 'b']

    print("排列组合")
    for i in itertools.permutations(list):  #排列
        print(i)

    print("组合")
    for t in itertools.combinations(list,2):  #组合
        print(t)

    print("迭代时跟踪索引")

    for x, value  in enumerate(list,0):
        print(x,value)


    print("index")
    iterate_index()

    print('同时迭代多个序列')
    iterate_simul()
    print("展开嵌套的序列")
    flatten_seq()


    print("使用iter代替while循环")
    iterate_while()