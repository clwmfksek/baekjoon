N, T = map(int, input().split())
result = []
for _ in range(N):
    S, I, C = map(int, input().split())
    time = [S + (I * c) for c in range(C)]
    if time[-1] < T:
        continue
    start = 0
    end = C - 1
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        if time[mid] >= T:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
    result.append(time[answer] - T)
if result:
    print(min(result))
else:
    print(-1)