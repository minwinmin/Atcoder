N = int(input())
X = list(map(int, input().split()))

temp = 0
ans = []
for i in range(1,101):
    for j in range(N):
        temp += (X[j] - i) ** 2
        #print(temp)
    ans.append(temp)
    temp = 0
print(min(ans))