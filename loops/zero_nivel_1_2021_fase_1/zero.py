R = int(input())
nums = []

for _ in range(R):
    N = int(input())
    if N == 0:
        nums.pop()
    else:
        nums.append(N)

print(sum(nums))
