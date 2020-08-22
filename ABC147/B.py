"""
一番前と後ろから順に比較していく
"""

S = input()
n = len(S)
ans = 0
#半分に割るイメージ、あまりは無視
for i in range(n//2):
    if S[i] != S[n-i-1]:
        ans += 1
print(ans)
