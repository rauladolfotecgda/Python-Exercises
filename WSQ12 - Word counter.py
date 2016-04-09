#Raúl Adolfo Torres Vargas
#A01400187
#WSQ12

fs= "We have flowers and flowersflowers. Four FlOwErs in fact "
count= 0
fs = fs.lower()
w= "FlOwErs"
w= w.lower()

lf = fs.find(w)

while(lf >= 0):
    print("Found flower at ", lf)
    count = count + 1
    lf = fs.find(w, lf + 1)
print("I found ", count,"of", w)