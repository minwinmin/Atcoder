#座標はxは負の場合もあるの絶対値をとること
X, K, D = list(map(int, input().split()))
X = abs(X)
#K回繰り返すことを考慮すること
i = min(X//D, K) #移動回数が最小の方をとる,、ここは柔軟に考えようや。
X = X - i*D
K = K - i

if K > 0:
    if K % 2 == 1:
        X = X - D
print(abs(X))

"""
シンプルに考えよう！
参考
https://qiita.com/u2dayo/items/ce1b420344e451560b42#c%E5%95%8F%E9%A1%8Cwalking-takahashi
"""


                                                                                                