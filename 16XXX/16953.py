import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

target,destination = map(int,input().split())
def bfs(num):
    queue = deque([[num,1]])
    while(queue):
        number,count = queue.popleft()
        if number == destination: return count
        num1 = int(str(number) + '1')
        num2 = number*2
        for i in [num1,num2]:
            if i > destination : continue
            tcount = count + 1
            queue.append([i,tcount])
    return -1

print(bfs(target))