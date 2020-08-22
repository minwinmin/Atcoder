"""
最善となる手をえらび続ける
勝てる手を選び続ける、もしくは手がない場合、あいこを選ぶ
"""
N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()
score = {"r":P, "s":R, "p":S} 
m = {"r":"p", "s":"r", "p":"s"}
command= []
mm = []
ans = 0
#添字は0から始まることに注意
#r : 0 s : 1 p : 2

"""
for i in range(N):
    if i - K < 0:
        ans += score[T[i]]
        mm.append(m[T[i]])
    else:
        if m[T[i]] != mm[i-2]:
            ans += score[T[i]]
            mm.append(m[T[i]])
        else:
            mm.append("")
                 
print(ans)
"""

"""
あまり複雑に考える必要はなかったのだ...
"""
for i, t in enumerate(T):
    if t == "r":
      c = "p"
      point = P
    elif t == "s":
      c ="r" 
      point = R
    elif t == "p":
      c = "s"
      point = S
    
    if (i - K >= 0) and (command[i - K] == c):
        #下記はポイント、かぶっている場合はなんでも良いので手を出す
        c = ""
        point = 0
    
    ans += point
    command.append(c)
print(ans)


"""
N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = list(input())


ans = 0
commands = [''] * N
for i, t in enumerate(T):
    if t == 'r':
        command = 'p'
        point = P

    elif t == 's':
        command = 'r'
        point = R

    elif t == 'p':
        command = 's'
        point = S

    if (i - K >= 0) and (commands[i -  K] == command):
        command = ''
        point = 0

    ans += point
    commands[i] = command

print(ans)
"""