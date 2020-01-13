X = int(input())
tf=True
while tf:
    if X % 2 == 0:
        X+=1
    else:
        for i in range(1,X):
            if X % i == 0:
                X += 1
            else:
                tf = False
print(X)