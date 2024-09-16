'''
3,7

4,6
'''

#Naive  way - সরল একটা সমাধান

start = int(input("Enter Start:  "))
end = int(input("Enter end:  "))

count = 0

for i in range(start, end + 1):
    if(i % 2 != 0):
        print(i)
        count = count + 1

print("total event: ", count)       

    