#常に小さい方w選んでいく
#A = Bのときはどうする？　つぎをみる,小さいほう選ぶ
N, M, K = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
t = 0
b = 0
i = 0
j = 0
def a(tt, ii, jj):
    if A[ii]<B[jj]:
        tt = tt + A[ii]
        ii = ii + 1
    elif A[ii]>B[jj]:
        tt = tt + B[j]
        jj = jj + 1
    else:
        a(tt, ii+1, jj+1)
    
    return tt
while t <= K:
    a(t, i, j)
        
print(t)