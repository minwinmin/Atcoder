"""
隣のマスと比較して、右のマスが高ければ、1マス下げる
左のマス>=右のマス これで最後までいったらYes　
※左のマスが右のマスより2異常だと✖️　NO
左のマス<=右のマス　何もしない
"""
"""
# 自分で書いた微妙なプログラム
# 高い方を1下げていった方が良さそう
N = int(input())
H = list(map(int, input().split()))

for i in range(N-1):
    if H[i+1] - (H[i]-1) > 1:
        print("Yes")
        exit()
print("No")
"""
N = int(input())
H = list(map(int, input().split()))

for i in range(N-1):
    if H[i+1] > H[i]:
        H[i+1] -= 1
    if H[i+1] < H[i]:
        print("No")
        break
else:
        print("Yes")

"""
上記のようにfor文の後にelse文をつけることができる！！！！
新発見
else文をつけると、全ての処理が終わった後に実行される。
while文でも適用可能。
"""