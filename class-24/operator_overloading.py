
class Employee:

    def __init__(self,name,salary,experince):
        self.name = name
        self.salay = salary
        self.experience = experince
    def __eq__(self, value):
        return self.experience == value.experience
    def __add__(self,amount):
        self.salary += amount
        

e1 = Employee(name="nahim" , salary=20000, experince=0)
e2 = Employee(name="fahim" , salary=20000, experince=0)

#+,-, * ,/, <,>
print(e1.experience == e2.experience)
e1 + 1500

print(e1.salary)
