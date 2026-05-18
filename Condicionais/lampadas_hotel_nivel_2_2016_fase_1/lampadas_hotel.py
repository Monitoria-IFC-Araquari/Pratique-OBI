ia, ib, fa, fb = map(int, input().split())

if ia == fa and ib == fb:
    print(0)
elif ia != fa and ib == fb:
    print(1)
elif ia == fa and ib != fb:
    print(2)
else:
    print(1)
