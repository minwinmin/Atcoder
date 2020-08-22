#NをKでわったときの余りと　N - K*商の絶対値を比較する
#前後を比較するイメージ
#問題の範囲だとfor分で回すと計算量オーバーしそう
N, K = list(map(int, input().split()))
a = N // K
b = N % K
print(min(abs(N - K * a), abs(b - K)))
