"""
for文2回はおそい
"""
N, K = list(map(int, input().split()))
p = list(map(int, input().split()))
pp = []
total = []

for i in range(N):
    k = (1/2*p[i]*(p[i]+1))/p[i]
    pp.append(k)
for j in range(K):
    kk = sum(pp[j:K+j])
    total.append(kk)
print(max(total))


"""
1.5 + 2.5 + 3 = 7

210　55　120　78
10.5　5.5 8 6.5 = 30.5
1/2*n*(n+1) 連番の合計値
期待値　(1/2*n*(n+1))/n
"""