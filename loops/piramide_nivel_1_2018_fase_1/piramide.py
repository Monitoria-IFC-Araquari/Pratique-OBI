Q = int(input())
piramide = 0
i = Q
while i > 0:
    i -= 1
    nums = list(map(int, input().split()))
    nums.sort(reverse=True)
    del nums[0:i]
    
    for num in nums:
        piramide += num

print(piramide)