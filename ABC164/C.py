N = int(input())
S = [input() for _ in range(N)]
print(len(set(S)))

#set（）　重複する値がある場合は無視されて一意な値のみが要素として残る