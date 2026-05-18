def solve():
    s = list(input().strip())
    i = len(s)-2
    while i >= 0 and s[i] >= s[i+1]:
        i -= 1
    if i < 0:
        print(0)
        return
    j = len(s)-1
    while s[j] <= s[i]:
        j -= 1
    s[i], s[j] = s[j], s[i]
    s[i+1:] = reversed(s[i+1:])
    print(''.join(s))
solve()