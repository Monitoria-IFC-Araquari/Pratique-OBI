N = int(input())

total = 0 

for i in range(N):
    X, Y = map(int, input().split())
    total += X * Y

print(total)