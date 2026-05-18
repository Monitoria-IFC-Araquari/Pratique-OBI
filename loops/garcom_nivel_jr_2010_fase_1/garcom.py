T = int(input())
coposQ = 0

for i in range(T):
    L, C = map(int, input().split())

    if L > C:
        coposQ += C

print(coposQ)