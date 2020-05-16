N, M, Q = list(map(int, input().split()))
a = []
b = []
c = []
d = []
M = range(1, N+1, 1)
print(M)
dd = 0
for i in range(Q):
    t = list(map(int, input().split()))
    """
    a.append(t[0])
    b.append(t[1])
    c.append(t[2])
    d.append(t[3])
    a = t[1]
    """
    print(M[t[0]])
    print(M[t[1]]-M[t[0]])
    if M[t[1]]-M[t[0]] == t[3]:
        dd += t[4]

print(dd)

"""
・総当たりで数列をつくって検証していく
・DFSを用いる
https://qiita.com/miffy_/items/9c76b282e5232e4a52db
・itertoolsはとても便利なので使いこすこと。
"""

from itertools import *
n, m, q = map(int, input().split())

aaa = []
for i in range(1, m+1):
    aaa.append(i)
l = []
for i in range(q):
    a = list(map(int, input().split()))
    l.append(a)
    
a = list(combinations_with_replacement(aaa, n))
ans = 0

for i in a:
    aa = 0
    for j in l:
        if i[j[1]-1] - i[j[0]-1] == j[2]:
            aa+=j[3]
        if aa > ans:
            ans = aa
print(ans)

"""
for分でぶん回して数列を作る方法も。全探索。
計算量を要チェックすること！
下記がわかりやすい。
とりあえず、全ての組み合わせの数列を作ってしまう方法
https://atcoder.jp/contests/abc165/submissions/13185361
"""

N, M, Q = map(int, input().split())
#下記の書き方応用できそうだ
arr = [list(map(int, input().split())) for _ in range(Q)]

ans = 0

"""
下記は問題の条件式をみて判断できる1<=M<=10
"""
for i1 in range(1, M+1):
    for i2 in range(i1, M+1):
        for i3 in range(i2, M+1):
            for i4 in range(i3, M+1):
                for i5 in range(i4, M+1):
                    for i6 in range(i5, M+1):
                        for i7 in range(i6, M+1):
                            for i8 in range(i7, M+1):
                                for i9 in range(i8, M+1):
                                    for i10 in range(i9, M+1):
                                        tmp = 0
                                        #添字の順番を合わせるために一つ目に0を代入している感じ。
                                        arrs = [0, i1, i2, i3, i4, i5, i6, i7, i8, i9, i10]
                                        for a, b, c, d in arr:
                                            if arrs[b] - arrs[a] == c:
                                                tmp += d
                                        ans = max(ans, tmp)
                            
print(ans)

"""
こっち
https://atcoder.jp/contests/abc165/submissions/13185361
"""
N,M,Q = map(int, input().split())
 
arr=[list(map(int,input().split())) for _ in range(Q)]
 
# Aの数列を作る。長さがMAX=Nだからとりあえず全探索
 
ans = 0
 
for i1 in range(1, M+1):
    for i2 in range(i1, M+1):
        for i3 in range(i2, M+1):
            for i4 in range(i3, M+1):
                for i5 in range(i4, M+1):
                    for i6 in range(i5, M+1):
                        for i7 in range(i6, M+1):
                            for i8 in range(i7, M+1):
                                for i9 in range(i8, M+1):
                                    for i10 in range(i9, M+1):
                                        tmp = 0
                                        arrs = [0,i1,i2,i3,i4,i5,i6,i7,i8,i9,i10]
                                        for a, b, c, d in arr:
                                            if arrs[b] - arrs[a] ==c:
                                                tmp += d
                                        ans = max(ans, tmp)
print(ans)


"""
dfsをつかった例
https://qiita.com/u2dayo/items/40eae13cffff57471422
"""

def dfs(nums, length, min_lim):
# 返り値は、すべての数列の得点の最大値 ans です。
# numsは数列の本体、lengthは数字の何個目まで決めたか、min_limは次の数字の最小値
    ans = 0
    if length == n:
    # 数列が完成したので、得点を計算します
        score_ret = 0
        for a, b, c, d in req:
            # nums[0]を捨てたので、nums[b-1]...としなくて済みます
            if nums[b] - nums[a] == c:  
                score_ret += d
        return score_ret  # この数列の得点を返します
    else:
        # まだ数列が完成していません
        for nu in range(min_lim, m + 1):
        # 次の数字の下限はmin_limで、上限はmです
            new_nums = nums + [nu]  # 長さ1のリスト[nu]を連結します
            # lengthは1増えて、次の下限は今付け加えた数字nuです
            score = dfs(new_nums, length + 1, nu)
            ans = max(ans, score) # 最大の得点を更新します

    # すべてが終わったので、答えを返します
    return ans


n, m, q = list(map(int, input().split()))

# 問題文のa,b,c,dの「リストのリスト」reqです。[[a1,b1,c1,d1],[a2,b2,c2,d2],[a3,b3,c3,d3]]のようになります。
req = [list(map(int, input().split())) for _ in range(q)]

# 最終的に答えが返ってくるようにします。処理はすべてdfsメソッドでやってもらいます。
# 数列の番号と添字を一致させたいので、適当な長さ1のリストを最初の状態にしておきます。
# 例えばサンプル1の1,3,4は[-1, 1, 3, 4]になります。
ans = dfs([-1], 0, 1)
print(ans)








