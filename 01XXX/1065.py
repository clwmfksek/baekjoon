N = int(input())
li = []
a = 0
for i in range(1,N+1):
    l = list(map(int,str(i)))
    if(len(l)<=2):
        a += 1
    else:
        if l[0]-l[1] == l[1]-l[2]:
            a += 1
print(a)