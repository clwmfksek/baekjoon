n = int(input())
li = []
for i in range(n):
    li.append(input())
res = li[0]
result = str(li[0])
for i in range(n):
    for j in range(len(result)):
        if result[j] != str(li[i][j]):
            result = result[:j] + '?' + result[j+1:]
print(result)