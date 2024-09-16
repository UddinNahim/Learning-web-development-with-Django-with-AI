# **kwargs

def greet(**kwargs):
    username = kwargs.get("username")
    is_loggedin = kwargs.get("is_Loggedin")
    is_subscribe = kwargs.get("is_subscribe")

    if username is not None:
        print(username)
    if is_loggedin is not None:
        print(is_loggedin)
    
    if is_subscribe is not None:
        print(is_subscribe)
    print("==================================")
    

greet()
greet(username ='sakib')
greet(username = 'rakib' , is_Loggedin = True)
greet(username = 'rakib' , is_Loggedin = True , is_subscribe = False)
greet()