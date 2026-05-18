Q = int(input())

conta = 1

for i in range(Q):
    N, O = map(str, input().split())

    if O == '*':
        conta *= int(N)
    else:
        conta /= int(N)
print(int(conta))