import math
X = int(input())
A = 100
i = 0
while X > A:
    A = math.floor(A * 1.01)
    i += 1
print(i)