#Raúl Adolfo Torres Vargas
#A01400187
#WSQ05

print("This program will show all formulas for temperature conversion")

F = float(input("Give me please the Farenheit grades: ")) 
C = float(input("Give me please the Celsius grades: "))
K = float(input("Give me please the Kelvin grades: "))

CtF = float((1.8 * C) + 32)
FtC = float((F - 32) / 1.8)
CtK = float(C + 273)
KtC = float(K - 273)

print("The temperature in Celsius",C,"your temperature in Farenheit with decimals is: ",CtF)
print("The temperature in Celsius",C,"your temperature in Farenheit without decimals is: ",round(CtF))

print("The temperature in Farenheit",F,"your temperature in Celsius with decimals is: ",FtC)
print("The temperature in Farenheit",F,"your temperature in Celsius without decimals is: ",round(FtC))

print("The temperature in Celsius",C,"your temperature in Kelvin with decimals is: ",CtK)
print("The temperature in Celsius",C,"your temperature in Kelvin without decimals is: ",round(CtK))

print("The temperature in Kelvin",K,"your temperature in Farenheit with decimals is: ",KtC)
print("The temperature in Kelvin",K,"your temperature in Farenheit without decimals is: ",round(KtC))

if(C >= 100):
    print("The water boils")
else:
    print("The water doesn't boils")