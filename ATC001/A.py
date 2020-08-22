"""
深さ探索
https://atcoder.jp/contests/atc001/tasks/dfs_a

- 幅優先探索は幅を優先して探索
- 最短経路問題を解く時には幅優先探索
"""
"""
#スタックとキューをつかった実装方法
import sys
h,w = map(int, input().split())
C = [list(input()) for i in range(h)]
visited = [[0 for i in range(w)] for  i in range(h)]
queue = []

#スタート地点をまず塗り潰し
for i in range(h):
    for j in range(w):
        if C[i][j] == "s":
            queue.append([i, j])
            visited[i][j]=1
            
#移動方向?
dy_dx = [[1,0], [0,1],[-1,0],[0,-1]]

while len(queue) > 0:
    now = queue.pop(0)
    if C[now[0]][now[1]] == "g":
        print("Yed")
        sys.exit()
    for i in range(4):
       y = now[0] + dy_dx[i][0]
       x = now[1] + dy_dx[i][1]
       if 0 <= y < h and 0<= x < w:
           if C[y][x] != "#" and visited[y][x] == 0:
               visited[y][x] = 1
               queue.append([y, x])
print("No")
"""

import sys
h,w = map(int,input().split())
C = [list(input()) for i in range(h)]
visited = [[0 for i in range(w)] for i in range(h)]
queue = []

for i in range(h):
    for j in range(w):
        if C[i][j] == 's':
            queue.append([i,j])
            visited[i][j] = 1
            
dy_dx = [[1,0],[0,1],[-1,0],[0,-1]]

while len(queue) > 0:
    now = queue.pop(0)
    if C[now[0]][now[1]] == 'g':
        print('Yes')
        sys.exit()
    #上下左右の4方向を試している
    for i in range(4):
        y = now[0]+dy_dx[i][0]
        x = now[1]+dy_dx[i][1]
        if 0 <= y < h and 0 <= x < w:
            if C[y][x] != '#' and visited[y][x] == 0:
                visited[y][x] = 1
                queue.append([y,x])
                
print('No')