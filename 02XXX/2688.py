import sys
input = sys.stdin.readline

for __ in range(int(input())):
    n = int(input())
    dp = [10,9,8,7,6,5,4,3,2,1]

    for _ in range(n-1):
        for i in range(10):
            dp[i] = sum(dp[i:])
    print(dp[0])