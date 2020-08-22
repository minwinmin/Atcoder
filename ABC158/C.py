#消費税が100円までの範囲なので、税抜き価格の最大値は1000円
"""
breakで抜け出すか
大きい数から数えていくかのどちらか
"""
A, B = list(map(int, input().split()))
ans = -1
for i in range(1, 1009):
    if int(i*0.08) == A and int(i*0.10) == B:
        ans = i
        break
print(ans)

"""
    if int(i*0.08) == int(i*0.10) and int(i*0.08)>0 and int(i*0.10)>0:
        ans = int(i*1.08)
        print(ans)
        break
"""