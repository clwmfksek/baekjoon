import sys
input = sys.stdin.readline

while(True):
    try :
        x = int(input())
        n = int(input())

        lis = []
        for i in range(n):
            lis.append(int(input()))
        lis.sort()

        nb = x * 10000000

        start = 0
        end = n-1

        bol = True
        while(start<end):
            sumd = lis[start] + lis[end]
            if sumd == nb:
                print(f"yes {lis[start]} {lis[end]}")
                bol = False
                break
            elif sumd > nb: end -= 1
            else : start += 1
        if bol: print("danger")
    except :
        break