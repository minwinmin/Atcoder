"""自分の解答
N, M = list(map(int, input().split()))
c = 0
p = 0
l = [(lambda s_lst: (int(s_lst[0]), s_lst[1]))(input().split()) for i in range(M)]
ls = list(map(list, set(map(tuple, l))))
print(ls)
for k in ls:
    if k[1] == "AC":
        c += 1
        
for j in range(1, N+1):
    for i in range(M):
        if l[i][0] == j:
            if l[i][1] == "WA":
                p += 1
            else:
                break
print(c, p)
"""

"""
N, M = map(int, input().split())
AC = {}
WA = {}
acNum = 0

for i in range(M):
    p, S = input().split()
    p = int(p)
    if S == "AC":
        if p in AC:
            pass
        else:
            AC[p] = 1
            acNum += 1
    else:
        # S == "WA"
        if not p in AC:
            if not p in WA:
                WA[p] = 0
            WA[p] += 1

peNum = 0
for k, v in WA.items():
    if k in AC:
        peNum += v

print(acNum, peNum)

"""

n,m=map(int,input().split())
ac=[0]*n
wa=[0]*n
for i in range(m):
    p,s=input().split()
    p=int(p)
    if ac[p-1] == 1:#このテストをクリアしていたら飛ばす。
        continue
    
    if s=='AC':#テストをクリアしたらフラグをつける
        ac[p-1] = 1
    else:#テストをクリアするまでは失敗を繰り返す。
        wa[p-1] += 1
        
# 最終的に出力するものを決める
AC=0
WA=0
for i in range(n):
    AC += ac[i]#クリアした回数
    if ac[i] == 1:
      WA += wa[i]#クリアできなかった回数
print("{} {}".format(AC,WA))
