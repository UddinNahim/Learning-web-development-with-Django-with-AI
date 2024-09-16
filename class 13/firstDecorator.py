# Now, I learn about decorator.THere is a quesiton why need decorator?decorator becaase
# Decorators in Python are a powerful and flexible tool that allows you to modify or extend the behavior of functions or methods without permanently modifying their original code. They provide a way to "wrap" another function, allowing you to add extra functionality before or after the execution of the wrapped function. Decorators are often used to implement cross-cutting concerns such as logging, timing, access control, and caching.
def Summing(n):
    sum = 0
    for i in range(1,n):
        sum += i 
    return sum
print("Start")
Summing(5)
print("End")

print("Start")
Summing(10)
print("End")

print("Start")
Summing(20)
print("End")

print("Start")
Summing(9)
print("End")