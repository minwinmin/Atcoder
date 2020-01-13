A, B = list(map(int, input().split()))
#小数点まで求める必要はないので　(A+B)//2 というように//で商のみを求める
result = (A+B)//2 if (A+B)%2 == 0 else "IMPOSSIBLE"
print(result)
