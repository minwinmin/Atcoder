import itertools
from operator import mul
from functools import reduce


N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

a = 0

for pair in itertools.combinations(A, K):
    aa = reduce(mul,pair)
    if a <= aa:
        a == aa
print(aa)

