"""
多重ループでいけそう
Lが1000までだから
"""

L = int(input())
"""
ans = [0]
for i in range(1, 350):
    for j in range(1, 350):
        for k in range(1, 350):
            if i + j + k == L:
                ans.append(i*j*k)
"""
a=b=c=L/3
print(a*b*c)