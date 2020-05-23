import math
#角度の差を求める
A, B, H, M = list(map(int, input().split()))
l = (2*math.pi)/(12*60*60)
s = (2*math.pi)/(60*60)

t = H * 60 * 60 + M * 60
tt = M * 60

lr = l * t
sr = s * tt

x1 = A * math.cos(lr)
y1 = A * math.sin(lr)

x2 = B * math.cos(sr)
y2 = B * math.sin(sr)

print(math.sqrt((x1-x2)**2 + (y1-y2)**2))