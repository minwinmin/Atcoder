import sys
import array
import numpy as np

N = int(input())
A = list(map(int, input().split()))

B = np.array(A)

a = 0
for i in range(N):
    a += A[i]*A[i]

dot = np.dot(B,B.T)
print(((dot - a)/2)%())
