# Naive Way

start = int(input("Enter start : ")) 
end = int(input("Enter end : ")) 

if start > end:
    print("You are fool!")

else:
    count = 0

    for i in range(start , end+1):
        if (i % 2 == 0):
            count = count + 1
            print(f"The number : {i} & Count is = {count}")

    print(f"Total Even : {count}")