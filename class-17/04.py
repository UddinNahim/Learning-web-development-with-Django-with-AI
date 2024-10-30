dc1 = {
    "name" : "salman",
    "age" : 10
}
#dictionary unpacked
dc2 = {**dc1}

dc2['name'] = "nahim"

print(dc1)
print(dc2)