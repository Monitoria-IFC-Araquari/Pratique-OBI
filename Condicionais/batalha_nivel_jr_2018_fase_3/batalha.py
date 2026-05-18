a1 = int(input())
d1 = int(input())
a2 = int(input())
d2 = int(input())
p1_desmaia = d1 != a2
p2_desmaia = d2 != a1
if p1_desmaia and not p2_desmaia:
    print(2)
elif p2_desmaia and not p1_desmaia:
    print(1)
else:
    print(-1)
