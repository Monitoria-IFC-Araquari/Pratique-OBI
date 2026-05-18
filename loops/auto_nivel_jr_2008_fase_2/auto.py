c = int(input())
s = input().strip()
painels = 0
for ch in s:
    if ch == 'P':
        painels += 2
    elif ch == 'C':
        painels += 2
    elif ch == 'A':
        painels += 1
print(painels)
