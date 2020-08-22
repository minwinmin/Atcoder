N = int(input())
n = len(str(N))
NN = str(N)
array = list(map(int, NN))
c = sum(array)
if c%9==0:
    print("Yes")
else:
    print("No")