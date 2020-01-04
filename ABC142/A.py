a = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
S = input()
N = int(input())

for i in S:
  b = a.index(i) + N
  if b<=25:
    print(a[b], end="")
  else:
    print(a[b-26], end="")
#複数の文字列の出力を改行しないで行う