import sys
n,x=map(int,sys.stdin.readline().split())
l=[sys.stdin.readline().split()]

for i in l[0]:
    if int(i) < x :
        print(f"{i} ",end='')