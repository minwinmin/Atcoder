"""
import numpy as np
X, N = list(map(int, input().split()))
p = np.array(list(map(int, input().split())))

pabs = np.absolute(p - X)
pmin = min(np.absolute(pabs - X))

print(min(p[np.where(pabs == pmin)]))
"""



"""
import numpy as np


def getNearestValue(list, num):

    # リスト要素と対象値の差分を計算し最小値のインデックスを取得
    idx = np.abs(np.asarray(list) - num).argmin()
    return list[idx]


if __name__ == "__main__":

    X, N = list(map(int, input().split()))
    p = list(map(int, input().split()))
    print(np.sort(p))
    print(getNearestValue(p, X-1))
    for i in range(np.sort(p)):
"""

"""
全探索でもとめる
・　Xを基準に0, ±1,  ±2...と広げていくやり方でも良い
・　0 < i < 101の間を全探索
"""


"""
いちいち絶対値を計算する必要はない
Xにもっと近くて小さい値を導出できればOK
"""
X, N = map(int, input().split())
p = list(map(int, input().split()))

#set関数　リスト内の重複をなくす、集合を意味する
p = set(p)
for i in range(200):
    if X - i not in p:
        print(X - i)
        break
    if X + i not in p:
        print(X + i)
        break
        

    