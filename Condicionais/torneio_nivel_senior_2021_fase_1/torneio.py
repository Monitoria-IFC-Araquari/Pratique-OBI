def solve():
    v = sum(1 for _ in range(6) if input().strip() == 'V')
    if v >= 5:
        print(1)
    elif v >= 3:
        print(2)
    elif v >= 1:
        print(3)
    else:
        print(-1)

if __name__ == '__main__':
    solve()
