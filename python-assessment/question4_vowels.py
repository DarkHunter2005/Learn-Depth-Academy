#Write a Python program that takes a string as input and counts the number of vowels (a, e, i, o, u) present in the string.

vowels=['a','e','i','o','u']
count=0
str1=input("enter the string")
for i in str1:
    if i in vowels:
        count+=1
print(f'Vowels ie present in the string is {count}')
