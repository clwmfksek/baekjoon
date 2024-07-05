import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    queue = deque([start])
    visited[start] = 0
    while queue:
        position = queue.popleft()
        for i in graph[position]:
            if visited[i] == -1:
                visited[i] = visited[position] + 1
                queue.append(i)

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [-1] * (n+1)

for _ in range(m):
    num1, num2 = map(int, input().split())
    graph[num1].append(num2)

bfs(x)

result = [i for i in range(1, n+1) if visited[i] == k]

if result:
    for city in result:
        print(city)
else:
    print(-1)
