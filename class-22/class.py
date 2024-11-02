from datetime import datetime
from pprint import pprint
class Person:
    def __init__(self, a , b ,c ):
        # print("hello")
        self.first_name = a
        self.last_name = b
        self.email = c
        self.joined = datetime.now()
    def __str__(self):
        return f"he is {self.first_name}"

nahim = Person(a = "Nahim " , b = "Uddin" , c = "nahim.211902019@gmail.com")

# print(nahim.email)
# print(nahim.joined)

# print(nahim.__dict__)
# pprint(nahim.__dict__)
nahim.email = "nahim@yahoo.com"
print(nahim.__dict__)
