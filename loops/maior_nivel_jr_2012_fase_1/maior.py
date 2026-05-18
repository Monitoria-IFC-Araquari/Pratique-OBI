nums = list(map(int, input().split()))
ans = 0
for x in nums:
    if x == 0:
        break
    if x > ans:
        ans = x
print(ans)
