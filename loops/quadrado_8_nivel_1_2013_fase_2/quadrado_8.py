N = int(input())
nums = list(map(int, input().split()))
mod_cnt = [0] * 8
mod_cnt[0] = 1
s = 0
ans = 0
for x in nums:
    s = (s + x) % 8
    ans += mod_cnt[s]
    mod_cnt[s] += 1
print(ans)
