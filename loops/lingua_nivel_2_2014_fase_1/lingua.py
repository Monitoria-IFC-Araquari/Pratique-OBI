msg = input().strip()
out = []
i = 0
while i < len(msg):
    if msg[i] == ' ':
        out.append(' ')
        i += 1
    else:
        i += 1
        if i < len(msg):
            out.append(msg[i])
            i += 1
print(''.join(out))
