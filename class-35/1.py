import json

user_data = {"id" : 1, "name":"Nahim"}

print(user_data)
print(type(user_data))

# now convert the dict into json file

user_json = json.dumps(user_data)
