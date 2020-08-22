#総当たり調べる
#3桁なので1000まで
"""
N, M = list(map(int,input().split()))
S = []
C = []
for i in range(1, M+1):
    s, c = map(int,input().split())
    S.append(s)
    C.append(c)
    
if N == 1:
    if M==1:
        print(C[0])
    else:
        print("-1")
#10~99
elif N == 2:
    for k in range(10, 100):
        k = str(k)
    #kの桁とcを比較する
"""
"""
n,m=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(m)]
if n==1: #N=1のときは0から9まで探索
 for i in range(10):
   tmp=str(i) #数字を文字列に変換しておく
   
   flag=True
   for j in range(m): #すべての条件を満たすかどうかをチェックする
     if tmp[arr[j][0]-1]!=str(arr[j][1]):
       flag=False
   if flag==True: #条件を満たす場合はそれを出力し動作を終了する
     print(i)
     break
 else: #条件を満たす数が存在しなかった場合は-1を出力する
   print(-1)
else: #N!=1のときは10**(N-1)から10**N-1まで探索
 for i in range(10**(n-1),10**n):
   tmp=str(i) #数字を文字列に変換しておく
   
   flag=True
   for j in range(m): #すべての条件を満たすかどうかをチェックする
     if tmp[arr[j][0]-1]!=str(arr[j][1]):
       flag=False
   if flag==True: #条件を満たす場合はそれを出力し動作を終了する
     print(i)
     break
 else: #条件を満たす数が存在しなかった場合は-1を出力する
   print(-1)
"""

#下記がシンプルでわかりやすい

N, M = map(int, input().split())
SC = [list(map(int, input().split())) for _ in range(M)]
for X in range(10**N):
  X = str(X)
  #all、全てがtrueなら発動
  #for s, c in SC　って書き方良いね。添字にするより、混乱しない。
  if len(X)==N and all(X[s-1]==str(c) for s, c in SC):
    print(X)
    break
else:
  print(-1)