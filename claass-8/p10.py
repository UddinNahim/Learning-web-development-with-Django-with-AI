names = ["nahim", "jamil"]

user_input = input("enter your name:")

for name in names:
    if name ==user_input:
        print("found")
        break
    else:
        print("not found")
        