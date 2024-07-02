import sys
from collections import deque
sys.setrecursionlimit(10**6)

n = int(input())

dx = [-1,0,1,0]
dy = [0,1,0,-1]

visited = []
visited2 = []
graph = []

for i in range(n):
    graph.append(list(input()))

for i in range(n):
    temp = [0 for i in range(len(graph))]
    visited.append(temp)

for i in range(n):
    temp = [0 for i in range(len(graph))]
    visited2.append(temp)

count = 0
def bfs1(nx,ny):
    global count
    if visited[nx][ny] == 1:
        return
    visited[nx][ny] = 1
    count += 1

    x = 0
    y = 0

    queue = deque([[nx,ny]])
    while(queue):
        temp = queue.popleft()
        for i in range(4):
            x = temp[0] + dx[i]
            y = temp[1] + dy[i]
            if x > len(graph) - 1 or x < 0 or y > len(graph[0]) - 1 or y < 0:
                continue
            if visited[x][y] == 1 or graph[nx][ny] != graph[x][y]:
                continue
            visited[x][y] = 1
            queue.append([x,y])

count2 = 0
def bfs2(nx,ny):
    global count2
    if visited2[nx][ny] == 1:
        return
    visited2[nx][ny] = 1
    count2 += 1

    x = 0
    y = 0

    queue = deque([[nx,ny]])
    while(queue):
        temp = queue.popleft()
        for i in range(4):
            x = temp[0] + dx[i]
            y = temp[1] + dy[i]
            if x > len(graph) - 1 or x < 0 or y > len(graph[0]) - 1 or y < 0:
                continue
            if visited2[x][y] == 1:
                continue
            if graph[nx][ny] == 'R' or graph[nx][ny] == 'G':
                if graph[x][y] == 'B':
                    continue
            elif graph[nx][ny] == 'B':
                if graph[x][y] != 'B':
                    continue
            visited2[x][y] = 1
            queue.append([x,y])

for i in range(n):
    for j in range(len(graph)):
        bfs1(i,j)
        bfs2(i,j)
print(count,count2)