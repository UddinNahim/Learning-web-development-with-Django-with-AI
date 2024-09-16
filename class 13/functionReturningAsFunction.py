# A function returning a function.[__closure__]

def outer():
    print("this is above of inner function")
    def inner():
        print("Hello Nahim.This is from inner function")

    #must return inner function 
    
    return inner

callFromOuter = outer()
callFromOuter()
