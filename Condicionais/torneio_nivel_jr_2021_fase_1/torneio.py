P1 = input() 
P2 = input() 
P3 = input() 
P4 = input() 
P5 = input() 
P6 = input() 

v = 0
g = -1

if P1 == "V":
    v += 1

if P2 == "V":
    v += 1

if P3 == "V":
    v += 1

if(P4 == "V"):
    v += 1

if P5 == "V":
    v += 1

if P6 == "V":
    v += 1


if v >= 5 and v <= 6:
    g = 1

elif v >= 3 and  v <= 4:
    g = 2

elif v >= 1 and v <= 2:
    g = 3


print(g)