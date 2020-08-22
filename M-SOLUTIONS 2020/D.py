n = int(input())
A = list(map(int, input().split()))

#最初の所持金
money = 1000
#株の所持数
kabu_c = 0

l = []
#予言で翌日上がるかどうかのリスト
for i in range(n-1):
    if A[i+1] - A[i] > 0:
         l.append(1)
    else:
         l.append(0)

#株の購入
#enumerateを使うと便利、変に勘違いすることもなさそう。
for idx, i in enumerate(l):
    if i == 1 and money - A[idx] >= 0:
        kabu_c = money // A[idx]
        money = money - kabu_c * A[idx]
    if i == 0:
        money = money + kabu_c * A[idx]
        kabu_c = 0

if kabu_c > 0:
    money = money + kabu_c * A[n-1]
print(money)


"""
下記解説の図がとてもわかりやすい
https://blacktanktop.hatenablog.com/entry/2020/07/26/100829
"""