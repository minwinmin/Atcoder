#やり方は間違って無さそうだがTLEがでる
#countが時間を取る
N = int(input())
A = list(map(int, input().split()))
n = [0] * N
#A_2 A_3 ... A_N とA_1をのぞいて続くのでN-1となる
for i in range(N-1):
    n[A[i]-1] += 1

for j in range(N):
    print(n[j])

#ちゃんと紙にかいて考えること！