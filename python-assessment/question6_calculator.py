#Create a simple calculator using functions.

def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    if num2==0:
        print("It cannot be possible")
    return num1/num2
while(True):
    print(''' 1.Add
            2.Sub
            3.Mul
            4.Div
            5.Exit''')
    ch=int(input("enter the ur choice"))
    if ch==1 :
        num1=int(input("enter the 1'st No:"))
        num2=int(input("enter the 2'nd No:"))
        result=add(num1,num2)
        print(f'Addition->{num1} +{num2} -> {result}')
    elif ch==2:
        
        num1=int(input("enter the 1'st No:"))
        num2=int(input("enter the 2'nd No:"))
        result=sub(num1,num2)
        print(f'Subtraction->{num1} -{num2} -> {result}')
    elif ch==3 :
        num1=int(input("enter the 1'st No:"))
        num2=int(input("enter the 2'nd No:"))
        result=mul(num1,num2)
        print(f'Addition->{num1} *{num2} -> {result}')
    elif  ch==4 :
        num1=int(input("enter the 1'st No:"))
        num2=int(input("enter the 2'nd No:"))
        result=div(num1,num2)
        print(f'Addition->{num1} / {num2} -> {result}')
    elif ch==5:
        break
    else:
        print('ur choice is not correct')
