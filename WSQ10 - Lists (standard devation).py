#Raúl Adolfo Torres Vargas
#A01400187
#WSQ10

print("This program will teach you to do the standard devation and the average")

import statistics

def fsuma (n):
    sum1 = 0
    for indice in range(len(n)):
       sum1 = sum1 + n[indice]
    return sum1
def average (n):
    a = suma / 10
    return a
def deviation (n):
    dev = statistics.stdev(A)
    return dev
x = 0
A=[]
while (x < 10):
    x = x + 1
    n = float(input("Give me a number: "))
    A.append(n)
    suma = fsuma(A)
    average2 = average(A)
deviation2 = deviation(A)
print ("Total sum: ",suma)
print ("Average: ", average2)
print ("Standard deviation is: ", deviation2)
