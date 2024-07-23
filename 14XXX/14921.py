import sys
input = sys.stdin.readline

n = int(input())
lis = list(map(int,input().split()))

start = 0
end = n-1

ans = lis[start] + lis[end]

while(start<end):
    sumd = lis[start]+lis[end]
    if abs(sumd) < abs(ans):
        ans = sumd
    if sumd < 0 : start += 1
    else : end -= 1
print(ans)