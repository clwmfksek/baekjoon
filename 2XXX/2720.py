import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

money = [25,10,5,1]

t = int(input())
for i in range(t):
    target = int(input())
    for j in money:
        print(money//j, end=' ')
        money = money%i