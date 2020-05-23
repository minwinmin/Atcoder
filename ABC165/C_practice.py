"""
参考
https://drken1215.hatenablog.com/
"""

M = 2
#確かに再帰している
def dfs(A):
    #終端条件：10重ループまで回したら処理して打ち切り
    if len(A) == 10:
        print(A)
        return
    for v in range(M):
        A.append(v)
        #確かに再帰している
        dfs(A)
        #指定した位置の要素を削除し、値を取得: pop()
        #引数を省略して位置を指定しない場合は、末尾（最後）の要素を削除する。
        A.pop() #ポイント
        
dfs([])

"""
長さ N の数列を生成する
数列の各項の値は 0,1,…,M−1 であるようにする
"""

"""
動き

まず A の要素数が N (= 5) かどうかをチェックする → 違うのでスルー
最初に v = 0 について
A に v を push (append) する → A = (2, 0, 1, 0) になる
dfs(A) を再帰呼出しする
A を pop する → A = (2, 0, 1) になる
次に v = 1 について
A に v を push (append) する → A = (2, 0, 1, 1) になる
dfs(A) を再帰呼出しする
A を pop する → A = (2, 0, 1) になる
最後に v = 2 について
A に v を push (append) する → A = (2, 0, 1, 2) になる
dfs(A) を再帰呼出しする
A を pop する → A = (2, 0, 1) になる

"""

#長さ
N = 10
M = 3 #(0,1,2)
def dfs(A):
    #終端条件：10重ループまで回したら処理して打ち切り
    if len(A) == N:
        print(A)
        return
    for v in range(M):
        A.append(v)
        dfs(A)
        A.pop()
        
dfs([])


"""
応用例　ABC165 C
"""

# 入力
N, M, Q = map(int, input().split())
a = [0] * Q
b = [0] * Q
c = [0] * Q
d = [0] * Q
for i in range(Q):
    a[i], b[i], c[i], d[i] = map(int, input().split())
    a[i] -= 1
    b[i] -= 1

# スコア計算
def score(A):
    tmp = 0
    for ai, bi, ci, di in zip(a, b, c, d):
        if A[bi] - A[ai] == ci:
            tmp += di
    return tmp

# DFS
def dfs(A):
    if len(A) == N:
        return score(A) # 数列 A のスコアを返す
    res = 0
    prev_last = A[-1] if len(A) > 0 else 0
    for v in range(prev_last, M):
        A.append(v)
        res = max(res, dfs(A)) # 再帰呼出しながら、スコア最大値も更新
        A.pop()
    return res

# 求める
print(dfs([]))

