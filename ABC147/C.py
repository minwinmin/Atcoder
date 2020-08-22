#bit全探索
"""
N = int(input())
A = []
xy = []
for i in range(N):
    a =  int(input())
    A.append(a)
    for j in range(a):
        x, y = map(int, input().split())
        #２次元配列
        xy.append([x, y])
print(xy)

honest = 0

for i in range(1, 2**N):
    flag = 0
    for j in range(N):
        # j番目が正直と仮定する
        if (i>>j)&1 == 1:
            for x,y in xy[j]:
                # j番目は正直だが矛盾を発見
                if (i>>x)&1 != y:
                    flag = 1
                    break
    # 矛盾がある場合はflag == 1になる
    if flag == 0:
        honest = max(honest, bin(i)[2:].count('1'))
print(honest)
"""

"""
参考
https://tane-no-blog.com/766/
"""

"""
正直者、不正直者の組み合わせを2進数でbit全探索する
"""

N = int(input())
 
testimony = [[] for _ in range(N)]
 
for i in range(N):
    num = int(input())
    for j in range(num):
        person, state = map(int, input().split())
        testimony[i].append([person-1, state])

honest = 0
for i in range(1, 2**N):
    flag = 0
    for j in range(N):
        if (i>>j)&1 == 1: # j番目は正直と仮定
            for x,y in testimony[j]:
                if (i>>x)&1 != y: # j番目は正直だが矛盾を発見
                    flag = 1
                    break
    if flag == 0:  # 矛盾がある場合はflag == 1になる
        honest = max(honest, bin(i)[2:].count('1'))  # 1の数をカウントし最大となるものを選択
print(honest)