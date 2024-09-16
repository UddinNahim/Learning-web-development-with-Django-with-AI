country = "bangladesh"
count_vowel = 0
count_consonant = 0

vowels = ['a','e', 'i', 'o', 'u']

for character in country :
    if character in vowels:
        count_vowel = count_vowel + 1
    else: 
        count_consonant = count_consonant + 1

print(f"total vowel = {count_vowel} , total consonant = {count_consonant}")