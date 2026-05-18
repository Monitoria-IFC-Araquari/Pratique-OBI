Q = int(input()) 
E = list(map(int, input().split()))
nums = []

for i in range(Q-1):
    if((E[i+1] + E[Q-i-2]) == (E[i] + E[Q-i-1])):
        nums.append("S")
    else:
        nums.append("N")

if "N" in nums:
    print("N")
else:
    print("S")
