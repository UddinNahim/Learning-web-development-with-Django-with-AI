# def get_percentage(total, percentage):
#         return (total * percentage / 100)

#dekhte sundor lage na tai amra class e use korbo jeno class er baireo use korte pari eijonno ekta method ache jeitar nam hocche static method
class Employee:
    count = 0
    def __init__(self,name,salary,experince):
        self.name = name
        self.salary = salary
        self.experience = experince
        
        Employee.count += 1
    @property
    def get_designation(self):
        if self.experience <= 0:
            return "Fresher"
        elif self.experience <= 2:
            return "Junior Software Engineer"
        elif self.experience > 2 and self.experience <=5:
            return "Mid senior Software Engineer"
        else: 
               return "Senior Software Engineer"

       #object method

    def bonus(self):
        #(0-2) ; 7 %, (2-5) : 15%, (5-10) : 20 , ():25 
        if self.experience < 0 :
            return 0 
        if self.experience >= 0 or self.experience <= 2:
            amount =self.get_percentage(total=self.salary, percentage=7)
        
        elif self.experience > 2 or self.experience <= 5:
            amount =self.get_percentage(total=self.salary, percentage=15)
        
        elif self.experience >5 or self.experience <= 10:
            amount =self.get_percentage(total=self.salary, percentage=20)

        else:
            amount = (self.salary) * 25 / 100
        return amount

    

    #class method
    @classmethod
    def total_employee(cls):
        return Employee.count
    
    @staticmethod
    def get_percentage(total, percentage):
        return (total * percentage / 100)


class Pet:
    def __init__(self,price):
        self.price =  price + Employee.get_percentage(total= price, percentage=5)
        


e1 = Employee(name="nahim" , salary=20000, experince=0)
e2 = Employee(name="Nafis" , salary=30000, experince=2)
e3 = Employee(name="Nafis" , salary=50000, experince=2)

# print(e1.bonus())
# print(e3.bonus())

# print(e1.get_designation())
print(e1.get_designation)

# Employee.total_employee()
# Employee.total_employee()

# p1 = Pet(price=10000)
# print(p1.price)

# print(Employee.total_employee())

