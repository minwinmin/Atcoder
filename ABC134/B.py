N, D = list(map(int, input().split()))
if N % (D*2+1) == 0:
    print(N//(D*2+1))
else:
    print((N//(D*2+1))+1)

"""
1 2 3 4 5 6 D=2
  1     1
  
1 2 3 4 5 6 D=2
  1     1
1 2 3 4 5   
  1     1
1 2 3 4 5 6 7 | 8 9 10 11 12 13 14 D=3
      1                 1
"""
      