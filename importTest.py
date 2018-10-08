import sys

print('this command line arguments are:')

for i in sys.argv:
    print(i)

print('\n\n The PYTHONPATH is ', sys.path, '\n')


def sayHello():
    """
      dir([object]) -> list of strings

      If called without an argument, return the names in the current scope.
      Else, return an alphabetized list of names comprising (some of) the attributes
      of the given object, and of attributes reachable from it.
      If the object supplies a method named __dir__, it will be used; otherwise
      the default dir() logic is used and returns:
        for a module object: the module's attributes.
        for a class object:  its attributes, and recursively the attributes
          of its bases.
        for any other object: its attributes, its class's attributes, and
          recursively the attributes of its class's base classes.
      """
    print("hello man i am import")


version = 1.0


if __name__ == '__main__':
    print("i am the main function")
else:
    print("i am not main func")