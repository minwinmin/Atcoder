N, K = list(map(int, input().split()))
H = sorted(list(map(int, input().split())), reverse = True)
del H[0:K]
print(sum(H))
    
"""
体力の大きいモンスターを必殺技で先に倒す
soredで大きい順に並び替え
"""