N = int(input())
for i in range(1,10):
    if N%i==0 and N//i<10:
        print("Yes")
        exit(0)
print("No")

#このリスト内包表記いい感じ
N = int(input())
l = {i*j for i in range(10) for j in range(10)}
print("Yes" if N in l else "No")