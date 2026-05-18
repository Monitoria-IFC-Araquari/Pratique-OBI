def solve():
    linha = input().strip()
    mapping = {}
    grupos = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    digito = 2
    for g in grupos:
        for c in g:
            mapping[c] = str(digito)
        digito += 1
    res = []
    for ch in linha:
        if ch in mapping:
            res.append(mapping[ch])
        else:
            res.append(ch)
    print(''.join(res))

if __name__ == '__main__':
    solve()
