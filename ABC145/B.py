N = int(input())
S = input()

if(N%2 == 0):
  #Pythonでは、//で整数の商、%で余り（剰余、mod）が算出
  n = N//2
  #[:n] 0~n-1 [n:] n~最後まで
  if(S[:n] == S[n:]):
    print("Yes")
  else:
    print("No")
else:
  print("No")
  