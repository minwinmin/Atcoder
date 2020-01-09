A, B ,K = list(map(int, input().split()))
if A > K:
  print(A-K, B)
else:
  #三項演算子
  #Bがマイナス値にならないように注意する、そのためのif文
  #A B とprintするならprint(A, B)で良い
  b = B-(K-A) if B>(K-A) else "0"
  print(0, B-(K-A))