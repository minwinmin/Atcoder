A, B = map(int, input().split())
l = sorted([A+B,A-B,A*B])
print(l[2])
"""
昇順（小→大）と降順（大→小）の意味を間違えないようする

max関数を使えば良い
a, b = map(int, input().split())
print(max(a+b, a-b, a*b))

"""