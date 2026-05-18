def solve():
    cipher = input().strip()
    text = input().strip()
    mapping = {}
    for i, c in enumerate(cipher):
        mapping[chr(ord('a')+i)] = c
    result = ''.join(mapping.get(c, c) for c in text)
    print(result)
solve()