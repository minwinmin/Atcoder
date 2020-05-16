#全探索、bit探索などがキーワード
#部分集合を扱うときは2進数を使うのがよい

"""
N, M, X = list(map(int, input().split()))
C = []
A = []

for i in range(N):
    C.append(list(map(int, input().split())))
print(C[1]+C[2])
"""

"""
入力方法
N M X
C1 A11 A12 ... A1M
:
:
CN AN1 AN2 ... ANN         
"""

N, M, X = map(int, input().split())
C = []
A = []
for  i in range(N):
    t = list(map(int, input().split()))
    C.append(t[0])
    A.append(t[1:])
    
result = -1
"""
<< bit演算に関する演算子
左辺の値を右辺の値だけ左へシフトすることを意味する

https://www.javadrive.jp/python/num/index4.html

下記の場合、1からNまで2真数でシフトしていく感じ
"""

for i in range(1 << N):
    #初期化
    t = [0] * M
    c = 0
    #print(i)
    for j in range(N):
        #print(j)
        if(i >> j ) & 1 == 0 :
            continue
        c += C[j]
        for k in range(M):
            t[k] += A[j][k]
    if all(x >= X for x in t):
        if result == -1:
            result = c
        else:
            result = min(result, c)
print(result)