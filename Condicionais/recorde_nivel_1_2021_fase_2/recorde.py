R = int(input())
M = int(input())
L = int(input())
out = []
if R > M:
    out.append("RM")
else:
    out.append("*")
if R > L:
    out.append("RO")
else:
    out.append("*")
print('\n'.join(out))
