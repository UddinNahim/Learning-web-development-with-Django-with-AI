from functools import lru_cache
from time import sleep
@lru_cache
def greet(name):
    print("Task - 1")
    print("Task - 2")

    sleep(2)

    return f"Hello {name}"

print(greet("nahim"))
print(greet("Wahia"))
print(greet("nahim"))
print(greet("Sajid"))
print(greet("nahid"))
print(greet("nahim"))