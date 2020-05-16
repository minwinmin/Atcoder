def change(X, n):
    if (int(X/n)):
        return change(int(X/n), n)+str(X%n)
    return str(X%n)

N, K = list(map(int, input().split()))
x = change(N, K)
print(len(x))
    