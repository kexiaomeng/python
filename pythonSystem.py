import sys


def readFile(fileName):
    '''print a file to the standard output.
    '''

    try:
        f = open(fileName)

        while True:
            line = f.readline()
            if len(line) == 0:
                break
            print(line)
        f.close()
    except FileNotFoundError:
        print("exception file not fount ")






if len(sys.argv) <2:
    print("No Action specified")
    sys.exit()
if sys.argv[1].startswith('-'):
    option = sys.argv[1][1:]
    if option == 'version':
        print(sys.version)
    elif option == 'hello':
        print("hello world")
else:
    readFile(sys.argv[1])


