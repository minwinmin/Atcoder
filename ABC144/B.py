N = int(input())
for i in range(1,10):
    for j in range(1,10):
        ij = i * j
        if(N == i*j):
            print("Yes")
            exit(0)
print("No")