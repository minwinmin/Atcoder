#微妙によくわかっていない
N = int(input())
d = [int(x) for x in input().split()]
t = 0
for i in range(N-1):
    for j in range(i+1, N):
      t += d[i]*d[j]
print(t)