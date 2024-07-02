import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
lis = list(map(int,input().split()))
k = int(input())
lis2 = [i for i in range(8)]
while(n>0):
    n -= 1
    for i in range(7):
        for j in range(i+1,8):
            if lis[n] == pow(2,i) + pow(2,j):
                lis2[i],lis2[j] = lis2[j],lis2[i]
for i in range(len(lis2)):
    if lis2[i] == k:
        print(i)