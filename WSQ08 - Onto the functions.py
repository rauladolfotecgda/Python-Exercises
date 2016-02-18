def operations(x,y):
    return(x+y, x-y, x*y, x/y, x//y, x%y)

x = int(input("Please give me the first number: "))
y = int(input("Please give me the second number: "))

print(operations(x,y))