
def double(func):
    def repeat():   
        func()
        print("Let's try that again!")
        func()
    return repeat
