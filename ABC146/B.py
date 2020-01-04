N = int(input())
S = input()

if(N%2 == 0):
  n = N//2
  if(S[:(n-1)] == S[n:]):
    print("Yes")
  else:
    print("No")
else:
  print("No")
  