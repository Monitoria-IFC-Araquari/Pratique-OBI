n = int(input())
a = input()
b = input()
ca = [0] * 26
cb = [0] * 26
for ch in a:
    if 'a' <= ch <= 'z':
        ca[ord(ch) - 97] += 1
for ch in b:
    if 'a' <= ch <= 'z':
        cb[ord(ch) - 97] += 1
print('S' if ca == cb else 'N')
