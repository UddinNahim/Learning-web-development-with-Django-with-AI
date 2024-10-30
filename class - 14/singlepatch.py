from functools import singledispatch
from functools import wraps

@singledispatch
def greet(value):
    return "your type doenot support"


@greet.register(int)
def handle_int(value):
    value = value + 10
    return value


@wraps
@greet.register(str)
def handle_str(value):
    value = "hi"
    return value


print(handle_int. __name__)
print(handle_str.__doc__)

print(greet(10))
print(greet("nahim"))
print(greet(1000))
