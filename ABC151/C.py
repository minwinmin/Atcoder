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
