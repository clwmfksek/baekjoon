import sys
input = sys.stdin.readline

n = int(input())
lis = list(map(int,input().split()))
lis.sort()

count = 0
for i in range(n):
    target = lis[i]
    start = 0
    end = len(lis)-1

    while(start<end):
        mid = lis[start]+lis[end]
        if mid == target:
            if i == start : start += 1
            elif i == end : end -= 1
            elif i != start and i != end:
                count += 1
                break
        elif mid < target: start += 1
        else : end -= 1
print(count)