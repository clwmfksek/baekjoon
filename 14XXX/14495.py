import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

fibo = [0] * 117
n = int(input())
fibo[0] = 1
fibo[1] = 1
fibo[2] = 1
fibo[3] = 2

for i in range(4,n+1):
    fibo[i] = fibo[i-1] + fibo[i-3]
print(fibo[n-1])