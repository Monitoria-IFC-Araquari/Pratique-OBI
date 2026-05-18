bolas = list(map(int, input().split()))

maior = 0

for i in range(10):
    cont = 0
    
    for x in bolas:
        if x == i:
            cont += 1
    
    if cont > maior:
        maior = cont

if maior <= 4:
    print("S")
else:
    print("N")