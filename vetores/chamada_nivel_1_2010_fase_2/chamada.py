n, k = map(int, input().split())
nomes = [input().strip() for _ in range(n)]
nomes.sort()
print(nomes[k-1])
