V = 0

P1 = input()
P2 = input()
P3 = input()
P4 = input()
P5 = input()
P6 = input()

if P1 == "V":
    V += 1
if P2 == "V":
    V += 1
if P3 == "V":
    V += 1
if P4 == "V":
    V += 1
if P5 == "V":
    V += 1
if P6 == "V":
    V += 1

if 5 <= V <= 6:
    G = 1
elif 3 <= V <= 4:
    G = 2
elif 1 <= V <= 2:
    G = 3
else:
    G = -1

print(G)
