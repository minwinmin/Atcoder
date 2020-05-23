"""
これだとTLEになる
"""

"""
S = int(input())
S = str(S)
n = len(str(S))
nnn = 0

if n>4:
    for i in range(n-3):
        for j in range(i+3, n):
            nn = int(S[i:j+1])
            
            if nn % 2019 == 0:
                nnn += 1
print(nnn)

"""

"""
使う知識
累積和
https://qiita.com/drken/items/56a6b68edef8fc605821

"""

"""
よくわかる解説
https://tamukun.com/atcoder-beginner-contest-164-d/
https://mirucacule.hatenablog.com/entry/2020/04/27/090908
https://at274.hatenablog.com/entry/2020/04/27/235514
"""

s = input()
s = s[::-1] #sを逆にする
n = len(s)

#各インデックス番号にmod2019の値が格納されるリストを想定
count = [0] * 2019

#a_0の分を入れておく
count[0] = 1
#a_iはこのnumver*dで表していく
number = 0
d = 1

for i in s:
    #a_iを表現
    number += int(i)*d
    # a_iのmod2019の値をcountに格納
    count[number%2019] += 1
    # numberで次の桁にしたいから，dを10倍
    d *= 10
    # numberが大きすぎない値になるようにd自体を先にmod2019の値でとる
    d %= 2019
    
ans = 0

for i in count:
    ans += i*(i-1)//2

print(ans)

"""
https://at274.hatenablog.com/entry/2020/04/27/235514
"""

from collections import Counter
S = input()[::-1]
MOD = 2019

"""
for 変数1, 変数2 in enumerate(リスト):
  print(‘{0}:{1}’.format(変数1, 変数2))
  
1行目のfor 変数1, 変数2 in enumerate(list):では、
listをenumerateで取得できる間ずっと、
変数1と変数2に代入し続けるfor文を使用しています。
ここで、変数1に入るのは、listの添字番号になります。
そして、変数2に入るのは、listの値になります。
"""

X = [0]
for i, s in enumerate(S):
    X.append((X[-1] + int(s) * pow(10, i, MOD)) % MOD)

C = Counter(X)
ans = 0
for v in C.values():
    ans += v * (v - 1) // 2
print(ans)




