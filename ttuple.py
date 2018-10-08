
record = [
    ("foo", 1, 2),
    ("bar", "hello"),
    ("foo", 3,4)
]


def do_foo(x, y):
    print("foo", x, y)


def do_bar(x):
    print("bar", x)


for tag, *arg in record:
    if tag == "foo":
        do_foo(*arg)
    elif tag == "bar":
        do_bar(*arg)

import collections   #队列

q = collections.deque(maxlen=3)

q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)

print(q.pop())
print(q.popleft())

q.appendleft(5)

print(q)

#################################
#查找最大或最小的值
import heapq

nums = [1,3,6,8,2,3,4]

print(heapq.nlargest(2,nums))
print(heapq.nsmallest(2,nums))
print(heapq.heappop(nums))


############################



items = [1,2,3,4,5,6,7,8,9,10]

def sum(item):   #递归
    head, *tail = item

    # if(len(tail)>0):
    #      return head + sum(tail)
    # else:
    #     return  head
    return head + sum(tail) if tail else head

print(sum(items))



li = [11, 22, 33]

new_list = map(lambda a: a + 100, li)

new_list1=[]
if new_list1:
    print("null")
else:
    print('not null')


from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            yield li, previous_lines
        previous_lines.append(li)

# Example use on a file
if __name__ == '__main__':
    with open(r'sun.txt') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)

    for i in range(1000):
        pass
###################################

import collections

# d = collections.defaultdict(set)
# print("##############")
# d['a'].add('1')
# d['b'].add('2')
# d['a'].add('3')
# d['a'].add('3')

d = collections.defaultdict(list)
print("##############")
d['a'].append('1')
d['b'].append('2')
d['a'].append('3')
d['a'].append('3')

print(d)