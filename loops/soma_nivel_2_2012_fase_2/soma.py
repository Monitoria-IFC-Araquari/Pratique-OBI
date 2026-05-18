N = int(input())
nums = [int(input()) for _ in range(N)]
K = int(input())
i, j = 0, N - 1
while i < j:
    s = nums[i] + nums[j]
    if s == K:
        print(nums[i], nums[j])
        break
    elif s < K:
        i += 1
    else:
        j -= 1
