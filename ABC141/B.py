S = input()
print(S[0::2])
print(S[1::2])
if "L" in S[0::2] or "R" in S[1::2]:
    print("No")
else:
    print("Yes")

# 0-indexed と 1-indexed で偶奇がひっくり返る...!?
    
#今回の場合　S[0::2] 0(始まり、カウント1) 1(カウント2 奇数) 2 3 4
#といったイメージ
# 1 2 3 4　スライスのカウント
# 0 1 2 3 インデックス
#   1   3 S[0::2]
# 0   2   S[1::2]     
#奇数　S[1::2]　偶数
#参考
#https://qiita.com/ycctw1443/items/03f99f3f72a797fdcbf6
#https://qiita.com/c-yan/items/5d5e3a635b4f0f3f5038