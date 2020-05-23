"""
参考
幅優先探索
→迷路の最短経路の探索　などが良い例
https://kakedashi-engineer.appspot.com/2020/05/18/abc168/
写経してみる
"""

import queue
N,M = map(int,input().split())
adj = [[]for i in range(N+1)]
parent = [-1] * (N+1) # -1なら未訪問
for m in range(M):
    a,b = map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)
    print(adj)
q = queue.Queue() # 自分の部屋番号、親の部屋番号

q.put((1,0)) # 部屋1の親は部屋0と考える
while(not q.empty()):
    x, p = q.get()
    print(x)
    if parent[x] != -1: # 訪問済み
        continue
    parent[x] = p
    for next in adj[x]:
        if parent[next] == -1: # 未訪問なら
            q.put((next,x)) # 探索候補に追加
print ('Yes') # 必ず目標は達成できる
for p in parent[2:]: # 部屋2以降の親（前の部屋）
    print(p)
    
    
"""
https://atcoder.jp/contests/abc168/submissions/13351956



# import sys
# import math #sqrt,gcd,pi
# import decimal
import queue # queue
# import bisect
# import heapq # priolity-queue
# import time
# from itertools import product,permutations,\
#     combinations,combinations_with_replacement
# 重複あり順列、順列、組み合わせ、重複あり組み合わせ
# import collections # deque
# from operator import itemgetter,mul
# from fractions import Fraction
# from functools import reduce
 
# mod = int(1e9+7)
mod = 998244353
INF = 1<<29
lINF = 1<<35
 
def readInt():
    return list(map(int,input().split()))
 
def main():
    n,m = readInt()
    # インデックスを部屋番号として、各部屋から繋がっている部屋の番号をリストに持つ
    graph = [[] for i in range(n)]
    for i in range(m):
        x,y = readInt()
        graph[x-1].append(y-1)
        graph[y-1].append(x-1)
    # 各部屋に設定する番号を記録する
    v = [-1 for i in range(n)]
	# 部屋1は -1 以外にしておく
    v[0] = [0]
    # queueを作成し部屋1（インデックスは0）を入れる
    q = queue.Queue()
    q.put(0)
    while not q.empty():
      	# queueの先頭（今いる部屋の番号）を取り出す
        x = q.get()
        # 今いる部屋と繋がっている部屋を順に探索する
        for y in graph[x]:
          	# -1ではない場合は既に探索済みなのでスキップする
            if v[y]!=(-1):
                continue
            # あとで探索する為にqueueに入れておく
            q.put(y)
            v[y] = x
    print("Yes")
    for i in range(1,n):
        print(v[i]+1)
    return
 
if __name__=='__main__':
    main()

"""    
    
    
"""
https://www.charter-blog.com/entry/2020/05/18/163000#D--Double-Dots


import sys
def input(): return sys.stdin.readline().rstrip()
from collections import deque
def main():
    n,m=map(int,input().split())
    #空のリストをつくる
    graph=[[] for _ in range(n)]
    for i in range(m):
        a,b=map(int,input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    queue=deque([0])
    visited=[False]*n
    visited[0]=True
    ans=[0]*n
    while queue:
        node=queue.popleft()
        for xnode in graph[node]:
            if visited[xnode]:continue
            ans[xnode]=node+1
            visited[xnode]=True
            queue.append(xnode)
    print("Yes")
    for a in ans[1:]:
        print(a)
 
 
if __name__=='__main__':
    main()
"""