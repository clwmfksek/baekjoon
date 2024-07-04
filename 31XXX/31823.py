import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())
for _ in range(n):
    target = list(map(str,input().rstrip().split()))
    name = target[m]
    result = 0
    count = 0
    for i in range(1,len(target)):
        if target[i] == ".": count += 1
        else : count = 0
        result = max(result,count)
    print(f"{result} {name}")
        