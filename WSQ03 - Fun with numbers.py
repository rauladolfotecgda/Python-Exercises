#Raúl Adolfo Torres Vargas
#A01400187
#WSQ03

print("In this program will display the sum, the rest, the product, division and divsion with decimal of two given numbers")

x = int(input("Give me the first number: "))
y = int(input("Give me the second number: "))

r = int(x + y)
t = int(x - y)
s = int(x * y)
w = int(x / y)
e = int(x // y)
m = int(x % y)

print("The sum of",x,"and",y,"is",r)
print("The rest of",x,"and",y,"is",t)
print("The product of",x,"and",y,"is",s)
print("The division with decimals of",x,"and",y,"is",w)
print("The division without decimals of",x,"and",y,"is",e)
print("The remainder of",x,"and",y,"is",m)