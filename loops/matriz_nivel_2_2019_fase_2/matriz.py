L, C = map(int, input().split())
M = [list(map(int, input().split())) for _ in range(L)]

if L < 2 or C < 2:
    print(0)
else:
    ok = [[0] * (C - 1) for _ in range(L - 1)]
    for i in range(L - 1):
        for j in range(C - 1):
            if M[i][j] + M[i + 1][j + 1] <= M[i][j + 1] + M[i + 1][j]:
                ok[i][j] = 1

    ans = 0
    h = [0] * (C - 1)
    for i in range(L - 1):
        for j in range(C - 1):
            h[j] = h[j] + 1 if ok[i][j] else 0
        stack = []
        for j in range(C - 1):
            while stack and h[stack[-1]] > h[j]:
                height = h[stack.pop()]
                width = j if not stack else j - stack[-1] - 1
                area = (height + 1) * (width + 1)
                if area > ans:
                    ans = area
            stack.append(j)
        while stack:
            height = h[stack.pop()]
            width = C - 1 if not stack else C - 1 - stack[-1] - 1
            area = (height + 1) * (width + 1)
            if area > ans:
                ans = area
    print(ans)
