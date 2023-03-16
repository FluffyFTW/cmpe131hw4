import time

def timestamp(func):
    def inner():
        print(time.ctime())
        func()
    return inner
