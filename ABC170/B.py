#総当り？
import sys
X, Y = list(map(int, input().split()))
for i in range(X+1):
    num = i * 2 + (X - i) * 4
    if(num == Y):
        print("Yes")
        exit()
print("No")
