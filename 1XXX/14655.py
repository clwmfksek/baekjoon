import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

target,destination = map(int,input().split())
visited = [0] * (destination+1)
def bfs(num):
    count = 0
    queue = deque([num])
    visited[num] = 1
    while(queue):
        number = queue.popleft()
        if number == destination: return visited[number]
        num1 = int(str(number) + '1')
        num2 = number*2
        for i in [num1,num2]:
            if i > destination : continue
            if visited[i] != 0 : continue
            visited[i] = visited[number] + 1
            queue.append(i)
    return -1

print(bfs(target))