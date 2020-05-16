import math

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

n, a, b = list(map(int, input().split()))
t = 0
for N in range(1, n+1):
    if N != a and N != b:
        t += combinations_count(n, N)        
print(t)


"""
for N in range(1, n+1):
    print(N)
    if N == b:
        print(N)
    elif N == a:
        print(N)
    else:
        a += combinations_count(n, N)
print(a%(10**9+7))
        a += 0
        print(a)
    else:
        a += combinations_count(n, N)
        
        n = list(range(1,n+1))
n = n.pop(a)
n = n.pop()
"""