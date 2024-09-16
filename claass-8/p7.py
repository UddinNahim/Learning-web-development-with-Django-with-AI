'''
while loop

while (codition is True):



'''


country = "bangladesh"

count_vowels = 0
count_consonant  = 0
vowels = ['a','e', 'i', 'o', 'u']

character = 0

while character in country:
    if character in vowels:
        count_vowels = count_vowels + 1
    else:
        count_consonant = count_consonant +1


print(f"total vowel = {count_vowels} , total consonant = {count_consonant}")