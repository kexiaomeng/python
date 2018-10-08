import time
from functools import  wraps

def logged(level, name = None, message = None):
    """

    :param level:
    :param name:
    :param message:
    :return:
    """
def timethis(func):


    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(func.__name__, end-start)
        return result

    return wrapper

# @timethis

def decorator(x, y, z):
    print(x,y,z)
    return timethis

@decorator(10, 1, 1)
def countdown(n:int):
    '''
        helloworld
    :param n:
    :return:
    '''

    while n>0 :
        n = n-1

print(countdown(10000000))

print(countdown.__name__)

print(countdown.__doc__)

print(countdown.__annotations__)

countdown.__wrapped__(10000)

print(countdown(222))