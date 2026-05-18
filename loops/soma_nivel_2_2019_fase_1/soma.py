N, P = map(int, input().split())
nums = list(map(int, input().split()))
soma=0
contador = 0

for i in range(N):
  soma=0
  for j in range(N-i):
    soma += nums[i+j]
    if(soma==P):
      contador+=1
    elif soma>P:
      break
print(contador)
