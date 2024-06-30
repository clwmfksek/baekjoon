import sys
import math
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

x,y,w,h = map(int,input().split())

print(min(x,y,w-x,h-y))