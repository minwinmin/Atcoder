
"""
n,m=map(int,input().split())
arr=[0]+list(map(int,input().split()))
print(arr)
g=[[] for _ in range(n+1)]
for _ in range(m):
 a,b=map(int,input().split())
 g[a].append(b)
 g[b].append(a)
ans=0
for v in range(1,n+1):
 for u in g[v]: #i番目の展望台から1本の道を通っていけるすべての展望台と高さを比較する
   if arr[u]>=arr[v]:
     break
 else: #i番目の展望台の高さが他のすべての展望台の高さより真に大きければ答えを1増やす
   ans+=1
print(ans)

"""

"""
n, m = map(int, input().split())
h = list(map(int, input().split()))
cnt = [0] * n
chk = [0] * n
ans = 0

for i in range(m):
    a,b = map(int, input().split())
    if h[a-1] > h[b-1]:
        cnt[a-1] += 1

    if h[a-1] < h[b-1]:
        cht[b-1] += 1
    chk[a-1] += 1
    chk[b-1] += 1
print(cnt)
print(chk)
for i in range(n):
    if cnt[i] == chk[i]:
        ans += 1

print(ans)
"""

"""
n, m = map(int,input().split())
h = list(map(int,input().split()))
#フラグを管理するイメージ
li = [1]*n

for i in range(m):
    a, b = map(int,input().split())
    if li[a-1] == 1 and h[a-1] <= h[b-1]:
        li[a-1] = 0
    if li[b-1] == 1 and h[b-1] <= h[a-1]:
        li[b-1] = 0
print(li)
print(sum(li))
"""

#http://osora01.com/?p=507

"""
https://qiita.com/miffy_/items/b4bf596415390b3db451
"""
import copy

n,m=map(int,input().split())
h=list(map(int,input().split()))
l=[]
for i in range(m):
    a,b=map(int,input().split())
    l.append([a,b])

ll=[0]*n

for j in l:
    if h[j[0]-1]>h[j[1]-1]:
        ll[j[1]-1]+=1
    elif h[j[0]-1]==h[j[1]-1]:
        ll[j[1]-1]+=1
        ll[j[0]-1]+=1
    else:
        ll[j[0]-1]+=1

ans=0
#print(ll)
for k in ll:
    if k==0:
        ans+=1
print(ans)
