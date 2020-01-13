N, K, M = list(map(int, input().split()))
A = sum(list(map(int, input().split())))
if K>=(M*N-A)>=0:
    print(M*N-A) 
elif (M*N-A)<0:
    print("0")
else:
    print("-1")

"""
平均点M✖️Nで必要な合計点を計算　1
N~N-1の点数Ai~Ai-の合計を計算　A
2ー1で必要な点を求める、
K+1以上なら-1
"""