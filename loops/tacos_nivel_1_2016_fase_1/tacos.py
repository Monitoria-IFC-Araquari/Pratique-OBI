C = int(input())
queries = list(map(int, input().split()))
stock = set()
ans = 0
for t in queries:
    if t not in stock:
        stock.add(t)
        ans += 2
print(ans)
