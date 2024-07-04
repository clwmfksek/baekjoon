import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

t = int(input())
for i in range(t):
    num = str(int(input()))
    rev = num[::-1]
    if str(int(num)+int(rev)) == str(int(num)+int(rev))[::-1]:
        print("YES")
    else : print("NO")
