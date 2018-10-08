# from abc import ABCMeta, abstractmethod
#
# class ISsstream(metaclass=ABCMeta):    #声明为抽象类
#     @abstractmethod
#     def read(self, maxBytes=-1):
#         pass
#
#     @abstractmethod
#     def write(self, data):
#         pass
#
#
# class SocketStream(IStream):    #inherit from parent class
#     version = 0.01
#     def __init__(self):
#         self.name = 'sun'
#
#
#     def read(self, maxBytes=-1):
#         print('inherit from parent class ')
#
#
#     def write(self, data):
#         pass
#
#
#
#
# class Descriptor:
#
#     sex = 'man'
#     def __init__(self, name=None, **opts):  #相当于java中的构造函数
#         self.name = name
#         for key, value in opts.items():
#             setattr(self, key, value)
#
#     def __set__(self, instance, value):
#         instance.__dict__[self.sex] = value
#
#     def set(self, value):
#         setattr(self, self.sex, value)
#
#
#     def __enter__(self):   #上下文管理器  执行with方法时候触发
#        return 2
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('exit')
#     #
#     # def __del__(self):
#     #     Person.number -= 1
#     #     print('im being deleted by you,name is %s' % self.name)
#
#     def set__name(self, name):
#         self.__name = name
#
#     def get__name(self):
#         return self.__name
#
#     # def __repr__(self):
#     #     return 'Pair({0.x!r},{0.y!r})'.format(self)
#
#
#     def __repr__(self):
#         return 'Pair(%r,%r)' % (self.x, self.y)
#
#     def say(self):
#         print("hello world"+ " "+ self.__name)
#
#
#
#
# a = SocketStream()
# b = SocketStream()
#
# a.version = 0.02
# b.version = 111111
# SocketStream.version = 'hello'
# print(a.__dict__)
# print(b.version)
# print("**************88")
#
# print(SocketStream.__dict__)
