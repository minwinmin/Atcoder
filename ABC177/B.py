S = input()
T = input()
c = 0
l = []
for i in range(len(S)-len(T)+1):
    for j in range(len(T)):
        if (T[j] != S[i+j]):
            c += 1       
    l.append(c)
    c = 0
#print(l)
print(min(l))