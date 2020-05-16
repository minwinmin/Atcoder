#方針；数の大きい数字から選ぶ
A, B, C, K = list(map(int, input().split()))

if(A-K < 0):
    if((A-K)-B < 0):
        print(A - (K-A-B))
    else:
        print(K-A)
else:
    print(K)
    