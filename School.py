

class School:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("init school member %s %d" % (self.name , self.age))

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        raise Exception("can't delete")


    def tell(self):
        print("mymessage is %s %d " % (self.name, self.age))

    def __del__(self):
        print("exit from the programe")


class Student(School):

    def __init__(self, name, age, score):
        super.__init__(self,name, age)
        self.score = score

        print("initial student score %s %d, " % (self.name,self.score))

    def tell(self):
        print("my score is %s %d" % (self.name,self.score))

    def get_score(self):
        return self.score

    def set_socre(self, value):
        self.score = value

    name = property(get_score, set_socre)


class Teacher(School):
    def __init__(self,name, age, salary):
        super.__init__(self, name, age)
        self.salary = salary
        print("init teacher salary %d " % self.salary)

    def __str__(self):
        return "name ,%s age:%d " % (self.name, self.age)

    def __get__(self, instance, owner):

    def __len__(self):
        return  len(self.name)
    def  tell(self):
        print("my salary is %d" % self.salary)


t = Teacher("sunmeng", 20, 1000000)

s = Student("sunmengmeng", 10, 100)

t.tell()


s.tell()

print(t)





t.name = 'ssssssssss'

print(t.name)


print(s.score)

s.name = 111

print(s.score)