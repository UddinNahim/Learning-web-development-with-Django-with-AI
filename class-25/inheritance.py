
from datetime import datetime
#parent clss/base class / super class
class User:
    def __init__(self, email):
        self.email = email
        self.joined_at = datetime.now()
    def joined(self):
        return self.joined_at.strftime("%d-%m-%Y")

#child class / derived class 
class UserBio(User):
    def __init__(self, email, profile_image, bio):
        super().__init__(email=email)
        self.profile_image = profile_image
        self.bio = bio

    def intro(self):
        return f"He is the member of INNovative SKill and {self.bio}"

class Employee(User):
    def __init__(self,email, salary):
        super().__init__(email)
        self.salary = salary
        


# u1 = User(email="u1@gamil.com")
# u1Bio = UserBio(profile_image="u1.jpg", bio="A simple Engineer")    
u1 = UserBio(email = "Demo@gmail.com" , profile_image="demo.jpg" , bio="simple")  

print(u1.email)
print(u1.joined_at)

print(u1.intro())
        