N = int(input())

resul = 0

for i in range(N):
    A = input()

    pot = int(A[0:len(A) - 1]) ** int(A[len(A) - 1])

    resul += pot

print(resul)