country = "bangladesh"

count_vowel = 0
count_consonent = 0

vowels = ['a', 'e', 'i', 'o', 'u']

for character in country:
    if character in vowels:
        count_vowel = count_vowel + 1
    else:
        count_consonent = count_consonent + 1

print(f"Total Vowel = {count_vowel}, Total Consonent = {count_consonent}")
