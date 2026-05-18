n = int(input())
x = list(map(int, input().split()))
soma = sum(x[:4])
max_soma = soma
for i in range(4, n):
    soma += x[i] - x[i - 4]
    if soma > max_soma:
        max_soma = soma
print(max_soma)
