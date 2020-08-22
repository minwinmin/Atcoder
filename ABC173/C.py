#https://qiita.com/zenrshon/items/c4f3849552348b3dbe67
##a = [list(map(str, input().split())) for l in range(H)]
#print(a)

#import sys
#a = [[int(c) for c in l.strip()] for l in sys.stdin]
#print(a)

"""
解説
ビット全探索
https://note.com/tanon_cp/n/n9b0a77fcda7d#cPxR1
"""


h,w,k=map(int,input().split())
board=[list(input()) for _ in range(h)]
ans=0
for paint_h in range(2**h): #すべての行の塗りつぶし方を2進数で列挙する
 for paint_w in range(2**w): #すべての列の塗りつぶし方を2進数で列挙する
   cnt=0
   for i in range(h): #すべてのi行目j列目の要素についてみる
     for j in range(w):
       if (paint_h>>i)&1==0 and (paint_w>>j)&1==0: #各行のi番目のビットと各列のj番目のビットがともに0であればそのマスは塗りつぶされない
         if board[i][j]=='#': #塗りつぶされないマスが黒マスであれば個数を+1する
           cnt+=1
   if cnt==k: #塗りつぶされない黒マスの個数がKに等しければ答えを+1する
     ans+=1
print(ans)
                