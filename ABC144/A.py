A, B = map(int, input().split())
if(A>9 or B>9):
  print("-1")
elif(A>10 and B>10):
  print("-1")
else:
  ans=A*B
  print(ans)