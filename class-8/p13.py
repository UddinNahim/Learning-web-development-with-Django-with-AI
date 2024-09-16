names = [
    "Alice",
    "Bob",
    "Charlie",
    "Diana",
    "Edward",
    "Fiona",
    "George",
    "Hannah",
    "Ian",
    "Jessica",
    "Kyle",
    "Liam",
    "Mia",
    "Nathan",
    "Olivia",
    "Paul",
    "Quinn",
    "Rachel",
    "Sarah",
    "Thomas"
]

user_input = input("Enter friend name : ")

found = 1

for name in names:
    if name == user_input:
        found = 2
        break

if found == 2:
    print("Found")
else:
    print("Not Found")
