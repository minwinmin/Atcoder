#lambdaを使った場合
N = float(input())
A = list(map(float, input().split()))
a = sum(list(map(lambda x : 1 / x, A)))
print(1/a)
"""
Pythonでは、//で整数の商、%で余り（剰余、mod）が算出できる。
/ は通常の割り算
"""