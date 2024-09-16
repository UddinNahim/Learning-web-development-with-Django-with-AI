
def get_sort_key( ls, key):
    for item in ls:
        print(item[key])

ls =[("sakib" , 10), ("nahim", 20),("wahia" ,2)]

# get_sort_key(ls=ls , key=0)

new_ls =[
    ('computer' , 4000,'India'),
    ('Mobile' , 10000,'China'),
    ('dress' , 20000,'bd')
]

get_sort_key(ls=new_ls , key=0)