N = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(1, N+1):
    if (i%2 == 1) and (a[i-1]%2 == 1):
        ans += 1
print(ans)