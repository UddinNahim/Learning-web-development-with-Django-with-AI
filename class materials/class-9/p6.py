'''
5 X 1 = 5
5 X 2 = 10
.
.
.
5 X 10 = 50
'''

n1 = 2
n2 = 5

for number in range(n1 , n2+1):
    print(f"{number} er namta : ")

    for j in range(1, 11):
        print(f"{number} X {j} = {number * j}")
    
    print("-------------------------------")
