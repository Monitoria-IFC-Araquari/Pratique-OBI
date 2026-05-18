i, n = map(int, input().split())
din = {'D': i, 'E': i, 'F': i}

for _ in range(n):
    linha = input().split()
    if linha[0] == 'C':
        j = linha[1]
        x = int(linha[2])
        din[j] -= x
    elif linha[0] == 'V':
        j = linha[1]
        a = int(linha[2])
        din[j] += a
    elif linha[0] == 'A':
        j = linha[1]
        k = linha[2]
        a = int(linha[3])
        din[j] += a
        din[k] -= a

print(din['D'], din['E'], din['F'])
