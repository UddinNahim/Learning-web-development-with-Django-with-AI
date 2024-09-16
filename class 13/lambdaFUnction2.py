# here we try to use lambda function compressed the problem of lambdaFunction2 problem

ls = [
    ('Alice', 25,"chattogram"),
    ('Bob', 16,"DHaka"),
    ('Marley', 21,"Rongpur"),
    ('Wahia', 2,"Boalkhali"),
]

ls = sorted(ls, key=lambda  ls : ls[1])
# ages = [x[1] for x in ls]
print(ls)
# def get_value(anyList,key):
#     for item in anyList:
#         print(item[key])

# get_value(anyList=ls, key=1)

