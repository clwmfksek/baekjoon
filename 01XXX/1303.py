import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)



def bfs(i,j,target):
    if visited[i][j] == 1 : return
    visited[i][j] = 1
    global count
    count += 1
    queue = deque([(i,j)])
    while(queue):
        n1,n2 = queue.popleft()
        for i in range(4):
            nx = n1 + rx[i]
            ny = n2 + ry[i]
            if nx >= n or ny >= m or nx < 0 or ny < 0 : continue
            if visited[nx][ny] == 1 or graph[nx][ny] != target : continue
            visited[nx][ny] = 1
            count += 1
            queue.append((nx,ny))
m,n = map(int,input().split())
visited = [[0]*m for i in range(n)]
graph = []

rx = [-1,0,1,0]
ry = [0,1,0,-1]

for i in range(n):
    graph.append(list(input().rstrip()))
result = [0,0]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'W':
            target = 'W'
            count = 0
            bfs(i,j,target)
            result[0] += count**2
        else :
            target = 'B'
            count = 0
            bfs(i,j,target)
            result[1] += count**2
print(*result)