#法則を見つけ出すこと
#勘違いしないこと
N = int(input())
p = list(map(int, input().split()))
c = 0
for i in range(1, N+1):
    if i != p[i-1]:
        c += 1
if c == 0 or c == 2:
    print("YES")
else:
    print("NO")