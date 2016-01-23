#Raúl Adolfo Torres Vargas
#A01400187

print("I have a number chosen between 1 and 100.")

import random
name = input("¿What's your name?: ")
y = random.randint(1,101)
n = int(0)
print("Hello",name, "and welcome to my first game on Python")
x = int(input("Please guess me the number that I'm thinking between 1 and 100: "))
while (x != y):
    if (x > y):
        print("I'm sorry, but", x, "is too high, please try again: ")
    else:
        print("I’m sorry but", x, "is too low please try again")
    
    n = n + 1
    x = int(input("Please guess a number between 1 and 100: "))
    print("You got it! at", n,"The right answer is indeed", x)