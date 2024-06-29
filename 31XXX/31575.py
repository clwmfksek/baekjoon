import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

m,n = map(int,input().split())

graph = []
visited = []

for i in range(n):
    graph.append(list(map(int,input().split())))
    visited.append([0 for i in range(m)])

rx = [1,0]
ry = [0,1]

def bfs():
    queue = deque([[0,0]])
    while(queue):
        n1,n2 = queue.popleft()
        if n1 == n-1 and n2 == m-1 : return True
        for i in range(2):
            x = n1 + rx[i]
            y = n2 + ry[i]
            if x >= n or y >= m or x < 0 or y < 0 : continue
            if visited[x][y] == 1 or graph[x][y] == 0 : continue
            visited[x][y] = 1
            if x == n-1 and y == m-1 : return True
            queue.append([x,y])
    return False

if(bfs()): print("Yes")
else : print("No")