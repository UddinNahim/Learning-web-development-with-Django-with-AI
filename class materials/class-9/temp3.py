
number1 = 2
number2 = 3

for j in range(number1, number2+1):
    print(j)

    for i in range(1, 11):
        print(f"{j} X {i} = {j * i}")