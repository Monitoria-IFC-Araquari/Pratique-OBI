n = int(input())
h = [int(input()) for _ in range(n)]
left = [0] * n
right = [0] * n
left[0] = h[0]
for i in range(1, n):
    left[i] = max(left[i-1], h[i])
right[n-1] = h[n-1]
for i in range(n-2, -1, -1):
    right[i] = max(right[i+1], h[i])
ans = 0
for i in range(n):
    if min(left[i], right[i]) > h[i]:
        ans += 1
print(ans)
