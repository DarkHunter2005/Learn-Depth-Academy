#Write a Python program that accepts three numbers from the user and finds the largest number among them.

a=int(input("Enter the First Number"))
b=int(input("Enter the Second Number"))
c=int(input("Enter the Third Number"))

if a>=b and a>=c:
    print(f'{a} iam the largest number')
elif b>=a and b>=c:
    print(f'{b} iam the largest number')
else:
    print(f'{c} iam the largest number')
