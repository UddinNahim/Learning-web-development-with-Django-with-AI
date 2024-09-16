def decorator(func):
    def wrapper():
        print("this is wrapper")
        func()
        print("finish")
    return wrapper

def some():
    print("This is function for decorator")
myDecorator = decorator(some)
# print(myDecorator)
myDecorator()
myDecorator()
myDecorator()
myDecorator()

