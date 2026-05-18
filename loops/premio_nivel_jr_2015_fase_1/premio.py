D = int(input())
soma = 0
dias = 0
i = 0
while i < D:
    i += 1
    A = int(input())

    soma += A
     
    if soma >= 1000000:
        dias = i
        break

print(dias)    

