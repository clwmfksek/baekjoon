import sys
n = int(sys.stdin.readline())
sumd = 0

li = list(map(int,sys.stdin.readline().split()))
li2 = list(map(int,sys.stdin.readline().split()))

lis1 = sorted(li,reverse=True)
lis2 = sorted(li2)

for i in range(n):
    sumd += int(lis1[i]) * int(lis2[i]) 
print(sumd)