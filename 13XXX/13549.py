import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

n,m = map(int,input().split())

def bfs(now):
    queue = deque()

    if now == 0 :
        queue.append(1)
    else :
        queue.append(now)

    while(queue):
        position = queue.popleft()
        if position == m : 
                return visited[position]
        
        for x in [position*2,position-1,position+1]:
            if 0<= x < 100001 and visited[x] == 0:
                if x == position*2:
                    visited[x] = visited[position]
                    queue.appendleft(x)
                else :
                    visited[x] = visited[position] + 1
                    queue.append(x)

visited = [0] * 100001
if n==0:
    if m==0:
        print(0)
    else:
        print(bfs(n)+1)
else :
    print(bfs(n))