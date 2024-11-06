class Employee:
    count = 0
    def __init__(self,name,salary,experince):
        self.name = name
        self.salay = salary
        self.experience = experince
        
        Employee.count += 1
    def get_designation(self):
        if self.experience <= 0:
            return "Fresher"
        elif self.experience <= 2:
            return "Junior Software Engineer"
        elif self.experience > 2 and self.experience <=5:
            return "Mid senior Software Engineer"
        else: 
               return "Senior Software Engineer"
    @classmethod   
    def total_employee(cls):
        return cls.count
    def get_percentage(total,percent):
        return (total *percent)
e1 = Employee(name="nahim" , salary=20000, experince=0)

print(Employee.total_employee)