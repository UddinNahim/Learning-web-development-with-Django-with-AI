def greet (value):
    if isinstance(value, int):
        value = value + 10
        return value
    if isinstance (value,str):
        value = "hi" + value
        return value 
print(greet(10))
print(greet("10"))
print(greet("nahim"))
print(greet(1000))

    