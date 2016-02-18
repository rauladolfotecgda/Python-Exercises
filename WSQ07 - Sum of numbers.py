#Raúl Adolfo Torres Vargas
#A01400187
#WSQ07

print("This program will ask you two numbers and sum the numbers within that range")

x = int(input("Please insert the number without decimals which begins the sum: "))
y = int(input("Please insert the number without decimals to reach the sum: "))

t = int(sum(range(x, y + 1)))
print(t)
print("\n")
f = float(input("Please insert the number with decimals which begins the sum: "))
q = float(input("Please insert the number with decimals to reach the sum: "))
r = float(sum(range(f, q + 1)))
print(r)