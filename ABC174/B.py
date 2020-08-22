import math

N, D = map(int, input().split())
ans = 0
for i in range(N):
    X, Y = map(int, input().split())
    r = math.sqrt(X*X + Y*Y)
    if r <= D:
        ans += 1
print(ans)


