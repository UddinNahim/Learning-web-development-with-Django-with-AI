class Employee:
    #constructor __init__
    def __init__(self , name:str , salary:int, age: int):
        #attributes
        #jegula ke amra assign korsi eigulai attributes
        self.name = name
        self.salary = salary
        self.age = age
e1 = Employee(name="nahim", salary=200000,age = 24)
print(e1.salary)

        