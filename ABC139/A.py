S = input()
T = input()
c = 0

for i in range(len(S)):
    if S[i] == T[i]:
        c += 1
print(c)

#サンプル回答
"""
print(sum(i==j for i,j in zip(input, input())))
"""
"""
zip関数
forループで複数のリストの要素を取得
orループの中で複数のイテラブルオブジェクト（リストやタプルなど）の要素を
同時に取得して使いたい場合は、zip()関数の引数にそれらを指定する。
names = ['Alice', 'Bob', 'Charlie']
ages = [24, 50, 18]

for name, age in zip(names, ages):
    print(name, age)
# Alice 24
# Bob 50
# Charlie 18
https://note.nkmk.me/python-zip-usage-for/
"""