n1 = 1
n2 = 10

for number in range(n1, n2+1):
    print(f"{number} er namta : ")

    for j in range(1, 11):
        result = number * j
        print(f"{number} X { j} = {result}")

