A = int(input())
P = list(map(int, input().split()))

pode = True

for i in range(A):
    peso = 0
    
    if P[i]  - peso <= 8:
        peso = P[i]
    else:
        pode = False
        break

if pode:
    print("S")
else:
    print("N")