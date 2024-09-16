def my_sum(*args):
    sum =0

    for digit in args:
        if isinstance(digit, (int,float)):
            sum = sum+ digit
    return sum
        

print(my_sum(1,2,3,4,5))
print(my_sum(1,2,3,4,5,6))
print(my_sum(1,2,3,4,'a',5,6))