import math
A, B, C, D = list(map(int, input().split()))

#小数点に注意
#今回の場合は切り上げすること
n = math.ceil(A / D)
m = math.ceil(C / B)
if n >= m:
    print("Yes")
else:
    print("No")