"""
全探索
DFS
再帰関数あたりを使う予感

https://qiita.com/tawatawa/items/408b872a7092be0d7b3c
ユークリッドの互覗法
"""
import math
from functools import reduce

gcd_sum = 0

def gcd_list(numbers):
    return reduce(math.gcd, numbers)

def dfs(A):
    
    if len(A) == K:
        return gcd_list(A)

    
    for v in range(K):
        A.append(v)
        dfs(A)
        A.pop()

K = int(input())
gcd = []
gcd = dfs([])
print(gcd)

"""
ふつうにfor文でまわしてみる
これを計算量を少なくするためには？
"""

import math
K = int(input())
ans = 0

for i in range(1, K+1):
    for j in range(1, K+1):
        a = math.gcd(i,j)
        for k in range(1, K+1):
           ans += math.gcd(a, k)
print(ans)
