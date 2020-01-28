N = int(input())
P = list(map(int, input().split()))
c = 1
for i in range(1, N):
    for j in range(0, i):
        if P[i] > P[j]:
            break
    else:
        c += 1
print(c)