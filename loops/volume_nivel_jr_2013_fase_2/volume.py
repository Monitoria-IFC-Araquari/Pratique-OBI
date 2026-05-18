V, Q = map(int, input().split())
L = list(map(int, input().split()))

volume_atual = V
valor_max = 100
valor_min = 0
excedente = 0

for i in range(Q):
    valor_atual = L[i]
    if volume_atual + valor_atual > valor_max:
        excedente += (volume_atual + valor_atual) - valor_max
        volume_atual = valor_max
    else:
        volume_atual += valor_atual

print(volume_atual)



