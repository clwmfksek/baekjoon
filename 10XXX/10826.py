import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

t = int(input())
for i in range(t):
    sign = list(map(str,input().rstrip().split()))
    for j in sign:
        j = list(j)[::-1]

        print(''.join(j),end = ' ')
    print()