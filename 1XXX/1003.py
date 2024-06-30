t = int(input())

for _ in range(t):
    inp = int(input())
    dp1 = [0] * 41
    dp2 = [0] * 41
    dp1[0] = dp2[1] = 1
    dp1[1] = dp2[0] = 0
    for i in range(inp+1):
        if i>1:
            dp1[i] = dp1[i-1] + dp1[i-2]
            dp2[i] = dp2[i-1] + dp2[i-2]
    print(f"{dp1[inp]} {dp2[inp]}")