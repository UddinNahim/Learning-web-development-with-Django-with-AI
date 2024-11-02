class Student:
    def __init__(self, sId,studentName,batch,marks):
        self.sId = sId
        self.studentName = studentName
        self.batch = batch
        self.marks = marks
    def __str__(self):
        return f"he is {self.studentName}"
    
student1 = Student(sId=211902019, studentName="Nahim Uddin" , batch=211, marks = 65)


print(student1.__dict__)
print(student1)