C, P, F = list(map(int, input().split()))

qtd = P / F

if(C > qtd):
    print('N')
else:
    print('S')