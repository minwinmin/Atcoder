a = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
N = int(input())
S = input()
 
for i in S:
    b = a.index(i) + N
    if b <= 25:
        print(a[b], end="")
    else:
        print(a[b-26], end="")