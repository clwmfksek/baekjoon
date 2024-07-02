import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,k = map(int, input().split())
lis = list(input())
if n > 1:
	for _ in range(k):
		lis2 = [None for _ in range(n)]
		
		for i in range(n):
			rCnt = gCnt = bCnt = 0
			cur = [i-1, i, i+1]
			
			if i == 0: cur = [0, 1, n-1]
			elif i == n-1: cur = [n-2, n-1, 0]
			
			for j in cur:
				if lis[j] == 'R': rCnt += 1
				elif lis[j] == 'G': gCnt += 1
				else: bCnt += 1
			if rCnt == gCnt == bCnt == 1 or rCnt == 3 or gCnt == 3 or bCnt == 3:
				lis2[i] = 'B'
			elif (rCnt == 2 and gCnt == 1) or (gCnt == 2 and bCnt == 1) or (bCnt == 2 and rCnt == 1):
				lis2[i] = 'R'
			else:
				lis2[i] = 'G'
		lis = lis2
else:
	lis = ["G"]
lis = "".join(lis)
print(lis.count('R'), lis.count('G'), lis.count('B'))