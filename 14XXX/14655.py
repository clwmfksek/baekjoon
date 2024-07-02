import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
round1 = list(map(int,input().split()))
round2 = list(map(int,input().split()))

round1Result = 0
round2Result = 0

for i in round1:
    round1Result += abs(i)

for i in round2:
    case1 = round2Result + i
    case2 = round2Result + (0 - i)
    if case2 < case1 :
        round2Result = case2
    elif case1 <= case2 :
        round2Result = case1

print(round1Result-round2Result)