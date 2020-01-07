N, K = map(int, input().split())
d = list(map(int, input().split()))
c = 0

#TypeError: 'map' object is not subscriptable
#map と　リストは違うので
#a = list(map(int, input().split())) とする
for i in range(N):
    if d[i]>= K:
        c += 1
print(c)

