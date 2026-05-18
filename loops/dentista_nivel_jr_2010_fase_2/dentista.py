N = int(input())
inicio, termino = 0, 0 
consultas = 0

for i in range(N):
    X, Y = map(int, input().split())

    if X >= termino:
        inicio = X
        termino = Y
        consultas += 1

print(consultas)

