A, B = map(int, input().split())
num = 0
c = 1
if B == 1:
    print("0")
    tf = exit(0)
    
while c < B:
    if c < B:
      c += A - 1
      num += 1
print(num)

"""
思考力大事！
"""
      