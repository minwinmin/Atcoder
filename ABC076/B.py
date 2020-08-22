"""
操作A,Bごとに最小となる方を最後まで選び続ける。
"""
N = int(input())
K = int(input())
ans = 1

for i in range(N):
    if ans * 2 >= ans + K:
        ans = ans + K
    else:
        ans = ans * 2
print(ans)