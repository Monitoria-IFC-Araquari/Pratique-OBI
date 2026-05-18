def solve():
    nums = [int(input()) for _ in range(4)]
    total = sum(nums)
    best = total
    for i in range(4):
        for j in range(i + 1, 4):
            team = nums[i] + nums[j]
            diff = abs(total - 2 * team)
            if diff < best:
                best = diff
    print(best)

if __name__ == '__main__':
    solve()
