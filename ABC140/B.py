N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
c = 0

"""
for i in A:
    c += B[i-1]
c = c - B[A[N-1]-1]
if
print(c)
print(B[N-1])
print(C[N-2])
print(c + B[A[N-1]-1] + )
"""

pre = 0
for i in range(N):
    now = A[i] - 1
    c += B[now]
    if i != 0 and pre == now - 1:
        c += C[pre]
    pre = now
print(c)

#参考
#https://qiita.com/vain0x/items/7ed6bfde477f0ce479b8