# Stepping

'''
2 , 4 , 6 , 8, 10
'''

start = int(input("Enter start : ")) 
end = int(input("Enter end : ")) 

for i in range(start , end+1 , 2):
    print(i)


"""
Bug:
    1) If start is an ODD number
"""

# TIPS
'''
start = 30 
start = 3 ---> start = 4
start = 6
start = 31 ---> start = 32
'''