n = int(input())
divs = list(map(int, input().split()))
total = 0
for d in divs:
    total += d - 1
print(total)
