import sys
input = sys.stdin.readline

n,m = map(int,input().split())

lis = []
for i in range(n):
    lis.append(int(input().rstrip()))
lis.sort()

start = 0
end = 0

ans = 2000000000

while(start < n and end < n):
    if lis[end] - lis[start] >= m :
        ans = min(ans,lis[end]-lis[start])
        start += 1
    else : end += 1
print(ans)