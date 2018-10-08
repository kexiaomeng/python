import importTest
import time

a = 1

importTest.sayHello()   #导入模块


print("version", importTest.version)

print("hello dir")

dir(importTest)  #列出属性

dir()


myList = [2,1,3,4,5,6]

print(' '.join('%s' % id for id in myList))
for i in myList:
    print(i)

print("len of list is ", len(myList))

myList.append(9)

print(myList)
myList.append("hello")
myList.append(3)
#myList.sort()
print(myList)
del  myList[0]

name = "sun"
age  = 18

print(time.localtime())

print("my name is %s age is %d" %(name,age))
print(time.strftime("%Y-%m-%d %X", time.localtime()))


ab = {
    "name": "sun",
    "age": 18
}

delimiter="_*_"

print(delimiter.join(myList))

print("sunmeng")
print(sun.say("hello"))
class sun :
    var =1

    def say(self):
        print("hello")
