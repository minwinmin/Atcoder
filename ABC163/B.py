N, M = map(int, input().split())
A = list(map(int, input().split()))
total_date = sum(A)
if total_date <= N:
    print(N - total_date)
else:
    print("-1")