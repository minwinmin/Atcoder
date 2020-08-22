"""
三角形の成立条件
https://mathtrain.jp/seiritu

三角形の成立条件（存在条件）：三辺の長さが a,b,c である三角形が存在する必要十分条件は，
a+b>c かつ b+c>a かつ c+a>b

http://physics.thick.jp/Mathematics_A/Section5/5-3.html
abs(L[i]-L[j])<L[k]<L[i]+L[j]
"""
def listExcludedIndices(data, indices=[]):
  return [x for i, x in enumerate(data) if i not in indices]

N = int(input())
L = list(map(int, input().split()))

"""
重複なし組み合わせの導出例
https://qiita.com/BlueSilverCat/items/77f4e11d3930d7b8959b
がとても参考になった
"""
n = len(L)
c = 0
result = []
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if L[i]!=L[j] and L[j]!=L[k] and L[i]!=L[k]:
                if L[i]+L[j]>L[k] and L[j]+L[k]>L[i] and L[i]+L[k]>L[j]:
                    #print(L[i], L[j], L[k])
                    c += 1
print(c)


"""
#memo

import sys
 
# B - Making Triangle
import itertools
 
N = int(input())
L = list(map(int, input().split()))
 
combis = list(itertools.combinations(L, 3))
ans = 0
 
for combi in combis:
	a, b, c = combi
 
	if a != b and b != c and c != a:
		if a + b > c and b + c > a and c + a > b:
			ans += 1
 
print(ans)
"""