class Myfile:
    def __init__(self , filename,mode):
        print("COnstructor")
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self,a,b,c):
        self.file.close()

with Myfile(filename='demo.txt' , mode='r') as file:
    context = file.read()
    print(context)