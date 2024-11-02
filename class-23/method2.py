from datetime import datetime

#Blueprint class ke bole
class Employee:
    #constructor __init__
    def __init__(self , name:str , salary:int, age: int ):
        #attributes
        #jegula ke amra assign korsi eigulai attributes
        self.name = name
        self.salary = salary
        self.age = age

    def get_year_of_born(self):
        current_year = datetime.now().year

        print(self.age,current_year)

        year_of_born = current_year - self.age

        return year_of_born


e1 = Employee(name="nahim", salary=200000,age = 25 ) 
e2 = Employee(name="Nafis", salary=200000,age = 23 ) 
e3 = Employee(name="Jamoil", salary=200000,age = 29 ) 

e1_year_of_born = e1.get_year_of_born()
print(e1_year_of_born)
e2_year_of_born = e2.get_year_of_born()
print(e2_year_of_born)

e3_year_of_born = e3.get_year_of_born()
print(e3_year_of_born)


