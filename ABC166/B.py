"""
なるほどなぁって感じ
"""

N, K = map(int, input().split())

#お菓子を持っていない : 1
#お菓子を持っている   : 0
#持っていない人を最終的に導くから
S = [1] * N 

for i in range(K):
    d = int(input())
    t = map(int, input().split())
    for i in t:
        #i-1なのは添字と要素tが1ぶんずれているから
        S[i-1] = 0
print(sum(S))


