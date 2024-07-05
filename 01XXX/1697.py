import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

n,m = map(int,input().split())

def bfs(now):
    queue = deque()
    queue.append(now)

    while(queue):
        position = queue.popleft()
        if position == m : return visited[position]

        for x in [position-1,position+1,position*2]:
            if 0 <= x < 100001 and visited[x] == 0:
                if x == position*2:
                    queue.appendleft(x)
                else :
                    queue.append(x)
                visited[x] = visited[position] + 1


visited = [0] * 100001
print(bfs(n))