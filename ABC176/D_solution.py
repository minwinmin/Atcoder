"""
参考
https://marco-note.net/abc-176-work-log/

python3
ではなく
pypy3でつかう。
そうじゃないとTLEになる
"""

from collections import deque

H, W = map(int, input().split())
Ch, Cw = map(lambda x : int(x) - 1, input().split())
Dh, Dw = map(lambda x : int(x) - 1, input().split())
maze = [input() for _ in range(H)]

INF = 10**12
#各マスへの移動コスト
path = [[INF] * W for _ in range(H)]

#walk:移動A、warp:移動B
walk = [(0, 1), (0, -1), (-1, 0), (1,0)]
warp = [(i, j) for i in range(-2, 3) for j in range(-2, 3) if (i, j) not in [(0,0)] + walk]

q = deque()
path[Ch][Cw] = 0
q.append((Ch, Cw, 0))

while q :
    x, y, s = q.popleft()
    #移動A
    for dx, dy in walk:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < H and 0 <= ny < W and maze[nx][ny] == '.' and path[nx][ny] > s:
            path[nx][ny] = s
            #移動Aの場合はコスト0、キューの先頭に追加する
            q.appendleft((nx, ny, s))
    #移動B
    for dx, dy in warp:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < H and 0 <= ny < W and maze[nx][ny] == '.' and path[nx][ny] > s + 1:
            path[nx][ny] = s + 1
            #移動Bの場合はコスト1, キューの最後尾に追加
            q.appendleft((nx, ny, s+1))
            
ans = path[Dh][Dw] if path[Dh][Dw] < INF else '-1'
print(ans)