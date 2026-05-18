n, B = map(int, input().split())
tams = list(map(int, input().split()))
tams.sort()
i, j = 0, n - 1
pastas = 0
while i <= j:
    if i < j and tams[i] + tams[j] <= B:
        i += 1
    j -= 1
    pastas += 1
print(pastas)
