N = int(input())
nums = []
counter = 1

for i in range(N):
    M = int(input())
    nums.append(M)

for i in range(1, len(nums)):
    if nums[i-1] != nums[i]:
        counter += 1
    
print(counter)