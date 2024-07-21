import sys
input = sys.stdin.readline

n,k = map(int,input().split())
lis = [-1 for i in range(n)]
for i in range(n):
    lis[i] = int(input())
target = 0
count = 0
bol = False
for i in range(n):
    target = lis[target]
    count += 1
    if target == k:
        bol = True 
        break
if bol : print(count)
else : print(-1)