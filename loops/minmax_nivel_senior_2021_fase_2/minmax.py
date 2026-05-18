s = int(input())
a = int(input())
b = int(input())

menor = None
maior = None
for x in range(a, b + 1):
    if sum(int(d) for d in str(x)) == s:
        if menor is None:
            menor = x
        maior = x

print(menor)
print(maior)
