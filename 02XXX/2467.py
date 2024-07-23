import sys
input = sys.stdin.readline

n = int(input())
lis = list(map(int,input().split()))

start = 0
end = n-1

target1 = 1e9
target2 = 1e9

while(start<end):
    if abs(lis[start]+lis[end]) < abs(target1+target2):
        target1 = lis[start]
        target2 = lis[end]
    if lis[start]+lis[end] < 0 : start += 1
    else : end -= 1
print(target1,target2)