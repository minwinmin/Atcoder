a, b = map(int, input().split())
N = (a * b) % 2
 
if N == 0:
  print("Even")
else:
  print("Odd")

