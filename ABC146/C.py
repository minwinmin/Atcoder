"""
参考
https://drken1215.hatenablog.com/entry/2020/01/05/154700
"""

#全探索で1から始めると時間がかかる。
#そこで2分探索を利用する
#0~ と　〜1000000001両端から調べていく。


A, B, X = list(map(int, input().split()))
left = 0
right = 1000000001

#桁数を調べる
#下記はつまりrightm, leftが適切にせばまっている間繰り返す処理。
#境界値チェックみたいな？
while right - left > 1:
    mid = (left + right) // 2
    if A * mid + B * len(str(mid)) > X:
        right = mid
    else:
        left = mid
print(left)