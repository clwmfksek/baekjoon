import sys
input = sys.stdin.readline

n = int(input())
lis = list(map(int,input().split()))
lis.sort()

target1 = 1000000000
target2 = 1000000000

start = 0
end = n-1
while(start!=end):
    if abs(lis[start] + lis[end]) < abs(target1+target2):
        target1 = lis[start]
        target2 = lis[end]
    if (lis[start] + lis[end] >= 0) : end -= 1
    else : start += 1
    
print(target1,target2)