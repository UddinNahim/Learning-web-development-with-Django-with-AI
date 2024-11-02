class Employee:
    #constructor __init__
    def __init__(self , name:str , salary:int, age: int ,year_of_born:int):
        #attributes
        #jegula ke amra assign korsi eigulai attributes
        self.name = name
        self.salary = salary
        self.age = age
        self.year_of_born = year_of_born
e1 = Employee(name="nahim", salary=200000,age = 24 , year_of_born=1990) 
print(e1.year_of_born)

"""eikane inconsistency ache age and dob er majhe.that's why we implement new object which is like :
current_year - self.age = ?year
"""       