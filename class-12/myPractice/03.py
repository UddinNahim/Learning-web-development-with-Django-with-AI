def greet(username,is_loggedin=None):
    if is_loggedin:
        print(f"Hello {username}")
    else:
        print("please login")
greet(username="nahim")