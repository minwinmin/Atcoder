N = int(input())
 
S, T = map(str, input().split())
 
moji = ""
 
if(len(S) == len(T) == N):
  for i in range(0, N):
    str = (S + T)[i::N]
    moji += str
print(moji)