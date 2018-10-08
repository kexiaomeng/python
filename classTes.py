class Person:
    number = 0  ##类的变量 相当于java中的static#

    def __init__(self, name):  #相当于java中的构造函数
        self.x = 1
        self.y = 2
        self.__name = name
        Person.number += 1
        print('my name is %s' % self.__name + " number is %d" % Person.number)
        self.hello = ['name', 'age', 'sex', '111', '222', '333']

    def __enter__(self):   #上下文管理器  执行with方法时候触发
       return 2

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')
    #
    # def __del__(self):
    #     Person.number -= 1
    #     print('im being deleted by you,name is %s' % self.name)

    def set__name(self, name):
        self.__name = name

    def get__name(self):
        return self.__name

    # def __repr__(self):
    #     return 'Pair({0.x!r},{0.y!r})'.format(self)


    def __repr__(self):
        return 'Pair(%r,%r)' % (self.x, self.y)

    def say(self):
        print("hello world"+ " "+ self.__name)



"""
Topic: 对象自定义格式化
Desc : 
"""
_formats = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}'
}


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):  #可以自定义类的输出格式
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)


d = Date(2012, 12, 21)
print(d)
print(format(d, 'mdy'))
print('The date is {:ymd}'.format(d))
print('The date is {:mdy}'.format(d))

if __name__ == "__main__":

    p = Person("sun")
    p.say()
    name, age, sex, *num = p.hello


    print("name %s, age %s,sex %s" % (name, age, sex))
    print(num)
    # p1 = Person("meng")
    # p1.say()
    #
    # p2 = Person("meng  2")
    # p2.say()
    print("************")
    print(p)


    print('上下文管理器')

    with Person('meng') as sun:
        print(sun)



