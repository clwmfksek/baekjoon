import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

t = int(input())
for _ in range(t):
    m,n,k = map(int,input().split())

    graph = []
    visited = []

    for i in range(n):
        v = []
        for j in range(m):
            v.append(0)
        graph.append(v)

    for i in range(n):
        v = [0 for s in range(m)]
        visited.append(v)

    for i in range(k):
        num1,num2 = map(int,input().split())
        graph[num2][num1] = 1

    nx = [-1,0,1,0]
    ny = [0,1,0,-1]
    count = 0

    def bfs(rx,ry):
        global count
        if visited[rx][ry] == 1:
            return
        count += 1
        visited[rx][ry] = 1
        queue = deque([[rx,ry]])
        while(queue):
            temp = queue.popleft()
            for i in range(4):
                x = nx[i] + temp[0]
                y = ny[i] + temp[1]
                if x > n-1 or y > m-1 or x < 0 or y < 0:
                    continue
                if visited[x][y] == 1 or graph[x][y] == 0:
                    continue
                visited[x][y] = 1
                queue.append([x,y])

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                bfs(i,j)
    print(count)