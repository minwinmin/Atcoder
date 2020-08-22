N, X, T = map(int, input().split())
if N%X == 0:
    n = (N//X) * T
    print(n)
else:
    n = (N//X) * T + T
    print(n)