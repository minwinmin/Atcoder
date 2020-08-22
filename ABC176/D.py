"""
H, W = map(int, input().split())
Ch, Cw = map(int, input().split())
Dh, Dw = map(int, input().split())
ans = 0
S = [input().split() for i in range(H)]

if abs(Dh-Ch)<3 and abs(Dw-Cw)<3:
    ans += 1

if (Dh-Ch)>0 and (Dw-Cw)<0:  #左方向、下方向
    print("2")
elif (Dh-Ch)>0 and (Dw-Cw)>0: #左方向、上方向
    
elif (Dh-Ch)>0 and (Dw-Cw)>0:  #右方向、上方向
    
else: #右方向、下方向
    
"""

from collections import deque
import sys
def input():return sys.stdin.readline().strip()
def main():
    H, W = map(int, input().split())
    sh, sw = map(int, input().split())
    sh -= 1; sw -= 1
    start = (sh+2)*(W+4) + 2 + sw
    dh, dw = map(int, input().split())
    dh -= 1; dw -= 1
    goal = (dh+2)*(W+4) + 2 + dw
 
    field = "#"*(W+4)*2
    field += "##" + "####".join([ input() for _ in range(H)]) + "##"
    field += "#"*(W+4)*2
 
    move = [-1, 1, -(W+4), W+4]
    ex_left = [-2*(W+4)-2, -(W+4)-2, -2, (W+4)-2, 2*(W+4)-2, -(W+4)-1, (W+4)-1]
    ex_right = [-2*(W+4)+2, -(W+4)+2, +2, (W+4)+2, 2*(W+4)+2, -(W+4)+1, (W+4)+1]
    ex_up = [-2*(W+4)-2, -2*(W+4)-1, -2*(W+4), -2*(W+4)+1, -2*(W+4)+2, -(W+4)-1, -(W+4)+1]
    ex_down = [2*(W+4)-2, 2*(W+4)-1, 2*(W+4), 2*(W+4)+1, 2*(W+4)+2, (W+4)-1, (W+4)+1]
 
    INF = 10 ** 18
    num = [INF] * (H+4) * (W+4)
    warped = [False] * (H+4) * (W+4)
 
    def bfs(s):
        q = deque()
        num[s] = 0
        q.append((s, 0))
    
        while q:
            now, cost = q.popleft()
 
            # warpしたものの既に来ていた場合はスルー
            if cost > num[now]:
                continue
            else:
                num[now] = cost
 
            if now == goal:
                return
 
            for i, dx in enumerate(move):
                nx = now + dx
                if field[nx] == "." and num[nx] == INF:
                    q.appendleft((nx, cost))
                    num[nx] = cost
 
                elif field[nx] == "#":
                    if i == 0:
                        ex = ex_left
                    elif i == 1:
                        ex = ex_right
                    elif i == 2:
                        ex = ex_up
                    else:
                        ex = ex_down
 
                    for dx2 in ex:
                        nx2 = now + dx2
                        if field[nx2] == "." and num[nx2] == INF and not warped[nx2]:
                            q.append((nx2, cost+1))
                            warped[nx2] = True
    
    bfs(start)
 
    if num[goal] == INF:
        print(-1)
    else:
        print(num[goal])
 
    
    # for i in range(0, (H+4)*(W+4), W+4):
    #     print(field[i:i+W+4])
    
    # print(start)
    # print(start//(W+4), start%(W+4))
    # print(goal)
    # print(goal//(W+4), goal%(W+4))
    
 
 
if __name__ == "__main__":
    main()