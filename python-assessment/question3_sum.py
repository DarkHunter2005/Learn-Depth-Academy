#Write a Python program that takes a positive integer N as input and calculates the sum of all numbers from 1 to N.

n=int(input("enter the Number"))
sum1=0
if n>0:
    for i in range(1,n+1,1):
        sum1+=i
    print(f'Sum of 1 to {n} -> {sum1}')
else:
    print("It's no a postive number")
