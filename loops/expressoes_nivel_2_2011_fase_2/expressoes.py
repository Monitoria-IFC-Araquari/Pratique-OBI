def solve():
    T = int(input())
    for _ in range(T):
        s = input().strip()
        stack = []
        ok = True
        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                if not stack:
                    ok = False
                    break
                top = stack.pop()
                if (c == ')' and top != '(') or (c == '}' and top != '{') or (c == ']' and top != '['):
                    ok = False
                    break
        if ok and not stack:
            print('S')
        else:
            print('N')
solve()