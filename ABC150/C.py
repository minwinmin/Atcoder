import itertools
import math
N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
Nl = list(range(1, N+1))
p = list(itertools.permutations(Nl,N))
NN = math.factorial(N)
c1 = 1
c2 = 1
for v in range(NN):
    if list(p[v]) == P:
        break
    else:
        c1 += 1
for v in range(NN):
    if list(p[v]) == Q:
        break
    else:
        c2 += 1
print(abs(c1-c2))

#参考　こんなやり方もある