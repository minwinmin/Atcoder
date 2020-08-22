"""
import numpy as np
ans = 9999999
K , N = map(int,input().split())
A = np.array(list(map(int,input().split())))
for i in range(N):
    start = np.array([A[i]] * N)
    kyori = np.sum(np.abs(start - A))
    if kyori < ans:
        ans = kyori
print(ans)
"""

"""
キーワードは円環問題
"""

K , N = map(int,input().split())
A = list(map(int,input().split()))
kyori = [0]
A.append(K+A[0])
for i in range(N):
    kyori.append(A[i+1] - A[i])
kyori_max = max(kyori)
print(K-kyori_max)