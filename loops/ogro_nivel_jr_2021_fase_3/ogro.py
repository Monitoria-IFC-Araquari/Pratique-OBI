M = int(input())
direita = ''
esquerda = ''

for i in range(M):
    if(i < 5):
        direita += 'I'
    else:
        esquerda += 'I'

if(M == 0):
    print('*', '*')
elif(M <= 5):
    print(direita, '*')
else:
    print(direita, esquerda)