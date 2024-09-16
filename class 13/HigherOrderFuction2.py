# function as an argument.That's another higherorderfunction
def square(num):
    return num **2


def cube(num):
    return num **3

def quad(num):
    return num ** 4

def helper(functionName,num):
    return functionName(num)
result = helper(functionName=cube, num=3)
print(result)
