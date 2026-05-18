P = input().strip()
A = input().strip()
cnt_p = [0] * 26
star = 0
for ch in P:
    cnt_p[ord(ch) - 97] += 1
for ch in A:
    if ch == '*':
        star += 1
    else:
        cnt_p[ord(ch) - 97] -= 1
possible = all(c >= 0 for c in cnt_p) and sum(cnt_p) == star
print('S' if possible else 'N')
