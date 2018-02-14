
vowels=set('aeiou')
word=input("please input a word to search for vowels:")

found=vowels.intersection(set(word))

for vowel in found:
    print(vowel)
