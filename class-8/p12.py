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
    "Charlie",
    "Thomas"
]

user_input = input("Enter friend name : ")

for name in names:
    if name == user_input:
        print(f"{name} ke paoa giyeche")
        break
    else:
        print(f"Not found")

