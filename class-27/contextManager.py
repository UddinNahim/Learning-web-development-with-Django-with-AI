class myContext:
    def __init__(self):
        print("COnstructor")
    def __enter__(self):
        print("Enter")
    def __exit__(self,a,b,c):
        print("exit")

with myContext() as ctx:
    print("---here-----")