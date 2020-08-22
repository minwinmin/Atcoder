S = input()
T = input()
l = len(S)
n = 0
for i in range(l):
    if S[i] != T[i]:
        n = n+1
print(n)