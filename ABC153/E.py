"""
動的計画法を使う！
良い勉強だ！
参考：https://atcoder.jp/contests/abc153/submissions/9795468
https://qiita.com/drken/items/ace3142967c4f01d42e9#dijkstra-%E6%B3%95
https://qiita.com/drken/items/a5e6fe22863b7992efdb#%E5%95%8F%E9%A1%8C-2%E3%83%8A%E3%83%83%E3%83%97%E3%82%B5%E3%83%83%E3%82%AF%E5%95%8F%E9%A1%8C

"""

"""
前処理
"""
import numpy as np
H, N = map(int, input().split())
A = []
B = []
for _ in range(N):
    ai, bi = map(int, input().split())
    """
    入力したものをそれぞれリストに格納していく、これは真似ていこう
    """
    A.append(ai)
    B.append(bi)

"""
配列に変換
"""
A = np.array(A)
B = np.array(B)

"""
処理
"""
#0からHまで
dp = np.zeros(H+1, dtype=np.int64) 
dp[0] = 0

for i in range(1, H+1):
    dp[i] = np.amin(dp[np.maximum(i-A, 0)] + B)

"""
output
"""
print(dp[H])