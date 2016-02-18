#Raúl Adolfo Torres Vargas
#A01400187
#WSQ06

print("I have a number chosen between 1 and 100.")

import random
name = input("What's your name?: ")
last_name = input("What's your last name?: ")

y = random.randint(1,101)
n = float(0)
print("Hello",name,last_name, "and welcome to my first game on Python")
x = float(input("Please guess me the number that I'm thinking between 1 and 100: "))

while (x != y):
    if (x > y):
        print("I'm sorry, but", x, "is too high, please try again: ")
    else:
        print("I’m sorry but", x, "is too low please try again")
    
    n = n + 1
    x = float(input("Please guess a number between 1 and 100: "))
    print("You got it! at", n,"The right answer is indeed", x)