"""
ここのロジック通りにプログラムを組んでいく。
https://qiita.com/drken/items/a5e6fe22863b7992efdb#%E5%95%8F%E9%A1%8C-2%E3%83%8A%E3%83%83%E3%83%97%E3%82%B5%E3%83%83%E3%82%AF%E5%95%8F%E9%A1%8C
http://wakabame.hatenablog.com/entry/2017/09/10/211428
"""

"""
最大和問題
N要素を持つ数列 a[0],a[1],⋯,a[N−1] 
から任意の個数の項を選んで和を取った時の最大値
"""
N = int(input())
a = list(map(int, input().split()))
def max_sum(N,a):
  dp=[0]*(N+1) #0の配列を0〜N用意する、初期値0みたいな感じ
  for i in range(N):
    #イメージするとちゃんとわかる、今回はリストaにマイナス値があると弾かれる感じ
    dp[i+1]=max(dp[i],dp[i]+a[i])
  return dp[N]

print(max_sum(N, a))


"""
ナップザック問題
重さと価値の情報を持つ N 個の荷物を重さが
 W 以下になるように詰め込むとき価値の和を最大化
"""
def knapsack(N, W, weight, value):
    #初期化
    #Pythonでは浮動小数点数float型に無限大を表すinf
    inf = float("inf")
    #２次元配列だから行列みたいな感じ、表を思い受けべよう
    dp = [[-inf for i in range(W+1)] for j in range(N+1)]
    for i in range(W+1):
        dp[0][i]=0 #初期値みたいな感じ
    
    #DP
    for i in range(N):
        for w in range(W+1):
            #dp[i][w-weight[i]]の状態にi番目の荷物が入る可能性がある
            if weight[i]<=w:
                dp[i+1][w]=max(dp[i][w-weight[i]]+value[i], dp[i][w])
            #入る可能性がない
            else:
                dp[i+1][w]=dp[i][w]
    return dp[N][W]

"""
dpは最大化するものをあらわす、例えば価値とか
N = 3 W = 5
(weight,value)=(2,3),(1,2),(3,6)
W j  0 1 2 3 4 5  
N  0 0 0 0 0 0 0
i  1 
   2
   3

i=0 w=0
weight[0]=2 <= w=0
else
dp[1][0] = dp[0][0] = 0

i=0 w=1
weight[0]=2 <= w=1
else
dp[1][0] = dp[0][0] = 0

i=0 w=2
weight[0]=2 <= w=2
if
dp[1][0] = max(dp[0][2-2]+3 = 3, dp[0][3]=0) = 3
・
・
・
と繰り返していく

i=0 w=3
weight[0]=3 <= w=3
if
dp[1][0] = max(dp[0][3-2], dp[0][3]=0)

i=1 w =0
weight[0]=3 <= w=0
else:
    dp[2][0] = dp[1][0]

"""

