def decorator(func):
    def wrapper(n):
        print("starting")
        func(n)
        print("Ending")
    return wrapper

def some(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    print("Sum is : ",sum)

myDecorator = decorator(some)

myDecorator(40)
myDecorator(100)
myDecorator(20)
myDecorator(42)
myDecorator(12)
    