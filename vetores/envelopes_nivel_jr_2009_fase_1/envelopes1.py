n = int(input())

a = list(map(int, input().split()))

menor = a[0]

for i in range(1, n):
    if a[i] < menor:
        menor = a[i]

print(menor)