import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lis = list(map(int,input().split())) # 본인의 상사를 알려주는 배열
dp = [0] * (n+1) # 칭찬 받은 정도를 저장하는 배열

for i in range(m):
    num1,num2 = map(int,input().split()) # 칭찬 받은 사람 - num1 / 정도 - num2
    dp[num1] += num2 # 칭찬 받은 사람한테 num2만큼의 칭찬을 해줌

for i in range(2,n+1): # 배열을 사장을 제외한 첫 번째부터 끝까지 순회
    dp[i] += dp[lis[i-1]] # 자기 상사가 칭찬 받은 만큼 자기한테 더해줌

dp.pop(0) # 필요없는 부분 제외
print(*dp)