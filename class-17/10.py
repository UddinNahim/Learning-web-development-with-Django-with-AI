person = {
'name' : 'salman',
'age' : 30,
'email' : 'yahoo.com',
'bio' : 'ML',
}
w = person.setdefault('email' ,'gmail.com')

print(w)
print(person)