import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n,k = map(int,input().split())
    lis = list(map(int,input().split()))
    lis.sort()

    start,end = 0,n-1
    maxx = 1e8*2
    count = 0
    while(start<end):
        sumd = k-(lis[start] + lis[end])
        if abs(sumd) < maxx:
            count = 0
            maxx = abs(sumd)
            count += 1
        elif abs(sumd) == maxx :
            count += 1

        if sumd < 0 : end -= 1
        else : start += 1
    print(count)