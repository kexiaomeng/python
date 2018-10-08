import _pickle as p

# f = open("sun.txt","wb",)
# f.write("ehee")
list = ["sun","meng"]

# p.dump(list,f)

# f.close()

# f = open("sun.txt","rb")
del list

# list = p.load(f)
#
import  itertools
with open("sun.txt") as f:
    for line in itertools.dropwhile(lambda li : li.startswith('#'),f):
        print(line)
# print(list)
# while(True):
#     line = f.readline()
#     if(line.__len__() != 0):
#         print(line)
#     else:
#         break

print("je")
with open("sun.txt") as f:
    line = f.readline()
    words = [lin.strip().upper() for lin in line.split()]
    print(words)
