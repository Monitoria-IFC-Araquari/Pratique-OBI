A = int(input())
N = list(map(int, input().split()))
MA = int(input())
MB = list(map(int, input().split()))

for i in range(len(MB)):
    N.remove(MB[i])

print(*N, end=' ')