input()
A = list(map(int, input().split()))
B = list(map(int, input().split()))

disponiveis = set(A)
usados = set()

for b in B:
    if b not in disponiveis:
        print(b)
        break
    for y in usados:
        disponiveis.add(b + y)
    disponiveis.add(b + b)
    usados.add(b)
else:
    print('sim')
