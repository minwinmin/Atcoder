A, B, N = list(map(int, input().split()))
x = min(N, B-1)
maxx = int(A*x/B)
print(maxx)

