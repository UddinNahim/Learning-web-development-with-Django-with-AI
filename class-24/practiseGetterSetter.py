class Student:
    def __init__(self, name , age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if isinstance(value, str) and value:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")
    @property #access methods like an attributes
    def age(self):
        return self._age

    @age.setter

    def age(self, value):
        if isinstance(value, int) and value:
            self._age = value

        else:
            return ValueError ("age must be a non-negative integer")
    
student = Student("Nahim", 24)
# print(student.name)

student.name = "Jane"

print(student.name)



    

    
        