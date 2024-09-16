#
def some(*args, **kwargs):
    print(args)
    print(kwargs)

some(1,2,4,5, username= 'akib', email = "abc")
