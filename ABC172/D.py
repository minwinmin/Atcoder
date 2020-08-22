import sympy
N = int(input())
num = 0
t = 0
for i in range(N):
    k = i + 1
    num = k * sympy.divisor_count(k)
    t = t + num
print(t)