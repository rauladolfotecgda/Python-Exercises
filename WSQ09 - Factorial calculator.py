#Raúl Adolfo Torres Vargas
#A01400187
#WSQ09

print("This is a factorial calculator")

def factorial(n):
    x=1
    y=1
    while(x<n):
        x=x+1
        y=y*x
    return y

again=1
while(again==1):
    num=int(input("Please give me a number: "))
    if(num<0):
        print(num, "This number isn't a factorial number ")
        
    else:
        ans = factorial(num)
        print("factorial of ", num, "is", ans)
    again=int(input("Do you wanna try with other number? 1-Yes 0-No, give me a options: "))
    if(again!=1 and again!=2):
         print("This option is invalid ")
         again= int(input("Please try again, 1-Yes 2-No, please close the program: "))
